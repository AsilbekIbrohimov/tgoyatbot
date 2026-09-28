import { API } from './config.js';
import { jget } from './api.js';
import { S } from './settings.js';
import { openSura } from './suras.js';

export async function doSearch() {
  const q = document.getElementById('searchInput').value.trim();
  if (!q) return;
  const box = document.getElementById('searchResults');
  box.innerHTML = '<div class="spin"></div>';
  try {
    const res = await jget(`${API}/search/${encodeURIComponent(q)}/all/${S.translation}`);
    if (!res || !res.matches || !res.count) { box.innerHTML = '<div class="loading">Natija topilmadi</div>'; return; }
    box.innerHTML = `<div class="muted" style="margin-bottom:8px">${res.count} ta natija</div>` +
      res.matches.slice(0, 50).map(m => `<button class="row" data-s="${m.surah.number}" data-a="${m.numberInSurah}" style="display:block">
        <div class="badge" style="font-size:12px;color:var(--accent)">${m.surah.englishName} ${m.surah.number}:${m.numberInSurah}</div>
        <div class="trans" style="margin-top:6px">${m.text}</div></button>`).join('');
    box.querySelectorAll('[data-s]').forEach(b => b.onclick = () =>
      openSura(+b.dataset.s).then(() => { const el = document.getElementById('ayah-' + b.dataset.a); if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' }); }));
  } catch (e) {
    box.innerHTML = '<div class="err">Qidiruvda xatolik.</div>';
  }
}

export function initSearch() {
  document.getElementById('searchBtn').onclick = doSearch;
  document.getElementById('searchInput').addEventListener('keydown', e => { if (e.key === 'Enter') doSearch(); });
}
