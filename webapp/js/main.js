import './telegram.js';
import { applyFont } from './settings.js';
import { R } from './state.js';
import { show, toast } from './ui.js';
import { haptic } from './telegram.js';
import { initEditions } from './editions.js';
import { initSuras, renderSuras, openSura } from './suras.js';
import { initAudio, playAyah, playGid } from './audio.js';
import { toggleBookmark, showBookmarks } from './bookmarks.js';
import { initSearch } from './search.js';
import { initPrayer } from './prayer.js';
import { initMore } from './more.js';

applyFont();

// Oyatni ulashish (nusxa olish)
function shareAyah(n, no) {
  const a = R.curAyahs.find(x => x.numberInSurah === no);
  const txt = `Qur'on ${n}:${no}\n\n${a ? a.text : ''}`;
  navigator.clipboard.writeText(txt).then(() => toast('Nusxa olindi')).catch(() => toast('Nusxa olinmadi'));
}

// Inline onclick handlerlari uchun window'ga chiqaramiz
window.openSura = openSura;
window.playAyah = playAyah;
window.playGid = playGid;
window.toggleBookmark = toggleBookmark;
window.shareAyah = shareAyah;

// Tab bar / back tugmasi
document.querySelectorAll('.tabbar button').forEach(b => b.onclick = () => { haptic(); show(b.dataset.tab); });
document.getElementById('backBtn').onclick = () => { haptic(); show('suralar'); };
document.getElementById('suraFilter').oninput = e => renderSuras(e.target.value);
document.getElementById('prevSura').onclick = () => { if (R.curSura > 1) openSura(R.curSura - 1); };
document.getElementById('nextSura').onclick = () => { if (R.curSura < 114) openSura(R.curSura + 1); };

// Modullarni ishga tushiramiz
initAudio();
initSearch();
initPrayer();
initMore(showBookmarks);
initEditions();
initSuras();
