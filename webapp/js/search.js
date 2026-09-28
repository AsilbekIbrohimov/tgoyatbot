import { API } from './config.js';
import { S } from './settings.js';
import { openSura } from './suras.js';

// Butun edition matni keshi (client-side qidiruv uchun)
const editionCache = {};

// Kirill (o'zbek/rus) -> lotin, qidiruvni normallashtirish uchun
const CYR2LAT = {
  'а':'a','б':'b','в':'v','г':'g','ғ':'g','д':'d','е':'e','ё':'yo','ж':'j','з':'z',
  'и':'i','й':'y','к':'k','қ':'q','л':'l','м':'m','н':'n','о':'o','ў':'o','п':'p',
  'р':'r','с':'s','т':'t','у':'u','ф':'f','х':'x','ҳ':'h','ц':'s','ч':'ch','ш':'sh',
  'щ':'sh','ъ':'','ь':'','э':'e','ю':'yu','я':'ya','ъ':'',
};
function normalize(str) {
  let out = '';
  for (const ch of (str || '').toLowerCase()) {
    if (CYR2LAT[ch] !== undefined) out += CYR2LAT[ch];
    else if (/[a-z0-9؀-ۿ ]/.test(ch)) out += ch;
    else out += ' ';
  }
  return out.replace(/[’'`ʻʼ]/g, '').replace(/\s+/g, ' ').trim();
}

async function loadEdition(ed) {
  if (editionCache[ed]) return editionCache[ed];
  const r = await fetch(`${API}/quran/${ed}`);
  const j = await r.json();
  const flat = [];
  (j.data.surahs || []).forEach(s => {
    (s.ayahs || []).forEach(a => flat.push({
      s: s.number, sn: s.englishName, no: a.numberInSurah, text: a.text || '', norm: normalize(a.text || '')
    }));
  });
  editionCache[ed] = flat;
  return flat;
}

async function serverSearch(q, ed) {
  const r = await fetch(`${API}/search/${encodeURIComponent(q)}/all/${ed}`);
  const j = await r.json();
  if (j.status === 'OK' && j.data && j.data.count) {
    return j.data.matches.map(m => ({ s: m.surah.number, sn: m.surah.englishName, no: m.numberInSurah, text: m.text }));
  }
  return null; // indeks yo'q yoki natija yo'q
}

async function clientSearch(q, ed) {
  const flat = await loadEdition(ed);
  const qn = normalize(q);
  if (!qn) return [];
  return flat.filter(a => a.norm.includes(qn));
}

// --- Fuzzy (yaqin moslik) ---
function lev(a, b) {
  const m = a.length, n = b.length;
  if (!m) return n; if (!n) return m;
  let prev = Array.from({ length: n + 1 }, (_, i) => i);
  for (let i = 1; i <= m; i++) {
    let cur = [i];
    for (let j = 1; j <= n; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
    }
    prev = cur;
  }
  return prev[n];
}
function tokenRatio(q, w) {
  const d = lev(q, w);
  return 1 - d / Math.max(q.length, w.length);
}
async function fuzzySearch(q, ed, min = 0.72) {
  const flat = await loadEdition(ed);
  const qTokens = normalize(q).split(' ').filter(Boolean);
  if (!qTokens.length) return [];
  const scored = [];
  for (const a of flat) {
    const words = a.norm.split(' ');
    let total = 0, ok = true;
    for (const qt of qTokens) {
      let best = 0;
      for (const w of words) {
        const r = tokenRatio(qt, w);
        if (r > best) best = r;
        if (best === 1) break;
      }
      if (best < min) { ok = false; break; }
      total += best;
    }
    if (ok) scored.push({ ...a, _score: total / qTokens.length });
  }
  scored.sort((x, y) => y._score - x._score);
  return scored;
}

function highlight(text, q) {
  try {
    const i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) return text;
    return text.slice(0, i) + '<b style="color:var(--accent)">' + text.slice(i, i + q.length) + '</b>' + text.slice(i + q.length);
  } catch (e) { return text; }
}

export async function doSearch() {
  const q = document.getElementById('searchInput').value.trim();
  if (!q) return;
  const box = document.getElementById('searchResults');
  box.innerHTML = '<div class="spin"></div>';
  try {
    // 1) Serverli qidiruv (tez). 2) Bo'lmasa — tanlangan tarjima ichida client-side.
    let results = await serverSearch(q, S.translation);
    let note = '';
    if (!results) {
      box.innerHTML = '<div class="loading">Qidirilmoqda...</div>';
      results = await clientSearch(q, S.translation);
    }
    // Aniq moslik bo'lmasa — fuzzy (yaqin) qidiruv
    if (!results || !results.length) {
      box.innerHTML = '<div class="loading">Yaqin natijalar qidirilmoqda...</div>';
      results = await fuzzySearch(q, S.translation);
      if (results.length) note = '<div class="hint">Aniq moslik topilmadi — yaqin natijalar ko\'rsatildi.</div>';
    }
    if (!results.length) { box.innerHTML = '<div class="loading">Natija topilmadi</div>'; return; }
    box.innerHTML = note + `<div class="muted" style="margin:6px 0 8px">${results.length} ta natija</div>` +
      results.slice(0, 60).map(m => `<button class="row" data-s="${m.s}" data-a="${m.no}" style="display:block">
        <div class="badge" style="font-size:12px;color:var(--accent)">${m.sn} ${m.s}:${m.no}</div>
        <div class="trans" style="margin-top:6px">${highlight(m.text, q)}</div></button>`).join('');
    box.querySelectorAll('[data-s]').forEach(b => b.onclick = () =>
      openSura(+b.dataset.s).then(() => { const el = document.getElementById('ayah-' + b.dataset.a); if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' }); }));
  } catch (e) {
    box.innerHTML = '<div class="err">Qidiruvda xatolik. Internetni tekshiring.</div>';
  }
}

export function initSearch() {
  document.getElementById('searchBtn').onclick = doSearch;
  document.getElementById('searchInput').addEventListener('keydown', e => { if (e.key === 'Enter') doSearch(); });
}
