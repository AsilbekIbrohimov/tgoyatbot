import { CDN_AYAH, CDN_SURA } from './config.js';
import { S } from './settings.js';
import { R } from './state.js';

const player = document.getElementById('player');
const audioBar = document.getElementById('audioBar');
let playing = null;

function showBar(t) {
  document.getElementById('apTitle').textContent = t;
  audioBar.classList.add('on');
}

export function playAyah(no) {
  const el = document.getElementById('ayah-' + no);
  if (!el) return;
  document.querySelectorAll('.ayah.playing').forEach(x => x.classList.remove('playing'));
  el.classList.add('playing');
  player.src = CDN_AYAH(S.reciter, el.dataset.gid);
  player.play();
  playing = { type: 'ayah', no };
  showBar(`${R.curSura}:${no} tilovat`);
  document.getElementById('apToggle').textContent = '⏸';
}

export function playSurah(n, name) {
  player.src = CDN_SURA(S.reciter, n);
  player.play();
  playing = { type: 'surah', n };
  showBar(name + ' — butun sura');
  document.getElementById('apToggle').textContent = '⏸';
}

export function playGid(gid, label) {
  player.src = CDN_AYAH(S.reciter, gid);
  player.play();
  showBar(label + ' tilovat');
  document.getElementById('apToggle').textContent = '⏸';
}

export function initAudio() {
  player.onended = () => {
    if (playing && playing.type === 'ayah' && document.getElementById('apAuto').checked) {
      const next = playing.no + 1;
      const el = document.getElementById('ayah-' + next);
      if (el) { playAyah(next); el.scrollIntoView({ behavior: 'smooth', block: 'center' }); return; }
    }
    document.getElementById('apToggle').textContent = '▶';
    document.querySelectorAll('.ayah.playing').forEach(x => x.classList.remove('playing'));
  };
  player.onerror = () => { document.getElementById('apTitle').textContent = 'Audio yuklanmadi (bu qori uchun mavjud emas)'; };
  document.getElementById('apToggle').onclick = () => {
    if (player.paused) { player.play(); document.getElementById('apToggle').textContent = '⏸'; }
    else { player.pause(); document.getElementById('apToggle').textContent = '▶'; }
  };
  document.getElementById('apClose').onclick = () => {
    player.pause();
    audioBar.classList.remove('on');
    document.querySelectorAll('.ayah.playing').forEach(x => x.classList.remove('playing'));
  };
}
