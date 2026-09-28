import { detail } from './ui.js';
import { haptic } from './telegram.js';
import { openSura } from './suras.js';

export function getBM() { try { return JSON.parse(localStorage.getItem('qbm') || '[]'); } catch (e) { return []; } }
function setBM(a) { try { localStorage.setItem('qbm', JSON.stringify(a)); } catch (e) {} }
export function isBookmarked(n, no) { return getBM().some(b => b.n === n && b.no === no); }

export function toggleBookmark(n, no, btn) {
  let a = getBM();
  const i = a.findIndex(b => b.n === n && b.no === no);
  if (i >= 0) { a.splice(i, 1); btn.textContent = '☆ Saqlash'; }
  else { a.push({ n, no }); btn.textContent = '★ Saqlangan'; haptic(); }
  setBM(a);
}

export function showBookmarks() {
  const a = getBM();
  if (!a.length) { detail('<div class="loading">Xatcho\'plar yo\'q. Oyat o\'qiyotganda ☆ tugmasini bosing.</div>'); return; }
  detail('<div class="section-title">Xatcho\'plar</div><div class="list">' +
    a.map(b => `<button class="row" data-s="${b.n}" data-a="${b.no}"><div class="num">${b.n}:${b.no}</div><div class="t"><div class="en">Sura ${b.n}, oyat ${b.no}</div></div><span>›</span></button>`).join('') + '</div>');
  document.getElementById('moreDetail').querySelectorAll('[data-s]').forEach(b => b.onclick = () =>
    openSura(+b.dataset.s).then(() => { const el = document.getElementById('ayah-' + b.dataset.a); if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' }); }));
}
