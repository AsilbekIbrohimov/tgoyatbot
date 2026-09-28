import { API } from './config.js';
import { jget } from './api.js';
import { S } from './settings.js';
import { R } from './state.js';
import { show } from './ui.js';
import { haptic } from './telegram.js';
import { playSurah } from './audio.js';
import { isBookmarked } from './bookmarks.js';

let SURAS = [];

export async function initSuras() {
  try {
    SURAS = await jget(API + '/surah');
    renderSuras('');
  } catch (e) {
    document.getElementById('suraList').innerHTML = '<div class="err">Suralar yuklanmadi. Internetni tekshiring.</div>';
  }
}

export function renderSuras(q) {
  const box = document.getElementById('suraList');
  q = (q || '').toLowerCase().trim();
  const items = SURAS.filter(s => !q || String(s.number) === q || s.englishName.toLowerCase().includes(q) || s.name.includes(q));
  box.innerHTML = items.map(s => `<button class="row" data-sura="${s.number}">
      <div class="num">${s.number}</div>
      <div class="t"><div class="en">${s.englishName}</div>
        <div class="sub">${s.englishNameTranslation} · ${s.numberOfAyahs} oyat · ${s.revelationType === 'Meccan' ? 'Makkiy' : 'Madaniy'}</div></div>
      <div class="ar">${s.name}</div></button>`).join('') || '<div class="loading">Topilmadi</div>';
  box.querySelectorAll('[data-sura]').forEach(b => b.onclick = () => { haptic(); openSura(+b.dataset.sura); });
}

function stripBism(text, i, showBism) {
  if (i === 0 && showBism) return text.replace(/^بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\s*/, '');
  return text;
}

function saveLast(n) { try { localStorage.setItem('qlast', n); } catch (e) {} }

export async function openSura(n) {
  R.curSura = n;
  show('reader');
  document.getElementById('ayahBox').innerHTML = '<div class="spin"></div>';
  document.getElementById('readerHead').innerHTML = '';
  const eds = ['quran-uthmani', S.translation];
  if (S.translit) eds.push('en.transliteration');
  try {
    const res = await jget(`${API}/surah/${n}/editions/${eds.join(',')}`);
    const arabic = res[0], trans = res[1], translit = S.translit ? res[2] : null;
    const meta = arabic;
    document.getElementById('readerHead').innerHTML =
      `<div style="text-align:center;margin-bottom:10px">
        <div class="ar" style="font-size:26px">${meta.name}</div>
        <div class="big">${meta.englishName}</div>
        <div class="muted" style="font-size:13px">${meta.englishNameTranslation} · ${meta.numberOfAyahs} oyat</div>
        <button class="chip on" id="playSura" style="margin-top:10px">🎧 Butun surani tinglash</button>
      </div>`;
    document.getElementById('playSura').onclick = () => playSurah(n, meta.englishName);
    R.curAyahs = arabic.ayahs;
    const showBism = n !== 1 && n !== 9;
    let html = showBism ? '<div class="bismillah">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>' : '';
    html += arabic.ayahs.map((a, i) => {
      const no = a.numberInSurah, gid = a.number;
      const bm = isBookmarked(n, no);
      return `<div class="ayah" id="ayah-${no}" data-no="${no}" data-gid="${gid}">
        <div class="head"><span class="badge">${n}:${no}</span></div>
        ${S.arabic ? `<div class="arabic">${stripBism(a.text, i, showBism)}</div>` : ''}
        ${translit ? `<div class="translit">${translit.ayahs[i].text}</div>` : ''}
        <div class="trans">${trans.ayahs[i].text}</div>
        <div class="tools">
          <button onclick="playAyah(${no})">▶ Audio</button>
          <button onclick="toggleBookmark(${n},${no},this)">${bm ? '★ Saqlangan' : '☆ Saqlash'}</button>
          <button onclick="shareAyah(${n},${no})">Ulashish</button>
        </div></div>`;
    }).join('');
    document.getElementById('ayahBox').innerHTML = html;
    saveLast(n);
  } catch (e) {
    document.getElementById('ayahBox').innerHTML = '<div class="err">Sura yuklanmadi.</div>';
  }
}
