import { API } from './config.js';
import { S } from './settings.js';
import { openSura } from './suras.js';

// Matn yozuvi bo'yicha zaxira qidiruv edition'i
function fallbackEdition(q) {
  if (/[؀-ۿ]/.test(q)) return { ed: 'quran-uthmani', lang: 'arabcha' };
  if (/[Ѐ-ӿ]/.test(q)) return { ed: 'ru.kuliev', lang: 'ruscha' };
  return { ed: 'en.sahih', lang: 'inglizcha' };
}

async function rawSearch(q, ed) {
  const r = await fetch(`${API}/search/${encodeURIComponent(q)}/all/${ed}`);
  const j = await r.json();
  return j; // {status, data:{count,matches}} yoki {status:'NOT FOUND', data:'...'}
}

export async function doSearch() {
  const q = document.getElementById('searchInput').value.trim();
  if (!q) return;
  const box = document.getElementById('searchResults');
  box.innerHTML = '<div class="spin"></div>';

  let note = '';
  try {
    let j = await rawSearch(q, S.translation);
    // Tanlangan tarjimada indeks bo'lmasa — matn yozuviga qarab zaxira tilga o'tamiz
    if (j.status !== 'OK' || !j.data || !j.data.count) {
      const fb = fallbackEdition(q);
      if (fb.ed !== S.translation) {
        const j2 = await rawSearch(q, fb.ed);
        if (j2.status === 'OK' && j2.data && j2.data.count) {
          j = j2;
          note = `<div class="hint">Tanlangan tilda qidiruv indeksi yo'q — <b>${fb.lang}</b> matni bo'yicha qidirildi.</div>`;
        }
      }
    }
    if (j.status !== 'OK' || !j.data || !j.data.count) {
      box.innerHTML = '<div class="loading">Natija topilmadi</div>';
      return;
    }
    const res = j.data;
    box.innerHTML = note + `<div class="muted" style="margin:6px 0 8px">${res.count} ta natija</div>` +
      res.matches.slice(0, 50).map(m => `<button class="row" data-s="${m.surah.number}" data-a="${m.numberInSurah}" style="display:block">
        <div class="badge" style="font-size:12px;color:var(--accent)">${m.surah.englishName} ${m.surah.number}:${m.numberInSurah}</div>
        <div class="trans" style="margin-top:6px">${m.text}</div></button>`).join('');
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
