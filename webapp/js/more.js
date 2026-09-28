import { API, ALADHAN } from './config.js';
import { jget } from './api.js';
import { S, saveSettings } from './settings.js';
import { detail, show, toast } from './ui.js';
import { openSura } from './suras.js';

/* ---------- Juz ---------- */
function showJuz() {
  detail('<div class="section-title">Juzlar</div><div class="list">' +
    Array.from({ length: 30 }, (_, i) => `<button class="row" data-juz="${i + 1}"><div class="num">${i + 1}</div><div class="t"><div class="en">${i + 1}-juz</div></div><span>›</span></button>`).join('') + '</div>');
  document.getElementById('moreDetail').querySelectorAll('[data-juz]').forEach(b => b.onclick = () => openJuz(+b.dataset.juz));
}

async function openJuz(j) {
  show('reader');
  document.getElementById('readerHead').innerHTML = `<div style="text-align:center" class="big">${j}-juz</div>`;
  document.getElementById('ayahBox').innerHTML = '<div class="spin"></div>';
  try {
    // /juz/{n}/editions/... API'da yo'q — ikkita alohida so'rovni birlashtiramiz
    const [ar, tr] = await Promise.all([
      jget(`${API}/juz/${j}/quran-uthmani`),
      jget(`${API}/juz/${j}/${S.translation}`),
    ]);
    document.getElementById('ayahBox').innerHTML = ar.ayahs.map((a, i) => `<div class="ayah" id="ayah-${a.number}" data-gid="${a.number}">
      <div class="head"><span class="badge">${a.surah.number}:${a.numberInSurah}</span></div>
      ${S.arabic ? `<div class="arabic">${a.text}</div>` : ''}
      <div class="trans">${tr.ayahs[i].text}</div>
      <div class="tools"><button onclick="playGid(${a.number},'${a.surah.number}:${a.numberInSurah}')">▶ Audio</button></div></div>`).join('');
  } catch (e) { document.getElementById('ayahBox').innerHTML = '<div class="err">Juz yuklanmadi.</div>'; }
}

/* ---------- Hijriy sana ---------- */
function showHijri() {
  detail('<div class="spin"></div>');
  const d = new Date(), dd = String(d.getDate()).padStart(2, '0'), mm = String(d.getMonth() + 1).padStart(2, '0');
  jget(`${ALADHAN}/gToH/${dd}-${mm}-${d.getFullYear()}`).then(r => {
    const h = r.hijri;
    detail(`<div class="section-title">Bugungi hijriy sana</div><div class="card" style="padding:20px;text-align:center">
      <div style="font-size:26px;font-weight:700">${h.day} ${h.month.en} ${h.year}</div>
      <div class="ar" style="font-size:22px;margin-top:6px">${h.month.ar}</div>
      <div class="muted" style="margin-top:8px">${h.weekday.en} · ${h.designation.abbreviated}</div></div>`);
  }).catch(() => detail('<div class="err">Sana olinmadi.</div>'));
}

/* ---------- Qibla ---------- */
let qiblaDir = null;
function setNeedle(deg, heading) { const n = document.getElementById('needle'); if (n) n.style.transform = `rotate(${deg - (heading || 0)}deg)`; }
function enableCompass() {
  function handler(e) {
    const h = (e.webkitCompassHeading !== undefined) ? e.webkitCompassHeading : (360 - (e.alpha || 0));
    if (qiblaDir != null) setNeedle(qiblaDir, h);
  }
  if (typeof DeviceOrientationEvent !== 'undefined' && DeviceOrientationEvent.requestPermission) {
    DeviceOrientationEvent.requestPermission().then(s => { if (s === 'granted') window.addEventListener('deviceorientation', handler, true); else toast('Kompasga ruxsat berilmadi'); }).catch(() => toast('Kompas ishlamadi'));
  } else {
    window.addEventListener('deviceorientationabsolute', handler, true);
    window.addEventListener('deviceorientation', handler, true);
  }
}
function showQibla() {
  detail(`<div class="section-title">Qibla yo'nalishi</div>
    <div class="card" style="padding:16px;text-align:center">
      <div class="compass"><div class="kaaba">🕋</div><div class="needle" id="needle"></div></div>
      <div id="qiblaInfo" class="muted">Joylashuvga ruxsat bering</div>
      <button class="btn" id="qiblaGeo" style="margin-top:10px">📍 Yo'nalishni aniqlash</button>
      <button class="btn sec" id="qiblaComp" style="margin-top:8px">🧭 Kompasni yoqish</button>
      <p class="hint">Telefonni tekis ushlang. Ko'k strelka qiblani ko'rsatadi.</p>
    </div>`);
  document.getElementById('qiblaGeo').onclick = () => {
    if (!navigator.geolocation) { toast('Geolokatsiya yo‘q'); return; }
    navigator.geolocation.getCurrentPosition(async p => {
      try {
        const d = await jget(`${ALADHAN}/qibla/${p.coords.latitude}/${p.coords.longitude}`);
        qiblaDir = d.direction;
        document.getElementById('qiblaInfo').textContent = `Qibla: shimoldan ${Math.round(qiblaDir)}°`;
        setNeedle(qiblaDir);
      } catch (e) { document.getElementById('qiblaInfo').textContent = 'Yo\'nalish olinmadi'; }
    }, () => toast('Joylashuv olinmadi'));
  };
  document.getElementById('qiblaComp').onclick = enableCompass;
}

/* ---------- Tasodifiy oyat ---------- */
async function randomAyah() {
  const n = Math.floor(Math.random() * 6236) + 1;
  try {
    const d = await jget(`${API}/ayah/${n}/editions/quran-uthmani,${S.translation}`);
    const ar = d[0], tr = d[1];
    show('more');
    detail(`<div class="section-title">Tasodifiy oyat</div><div class="card" style="padding:16px">
      <div class="badge">${ar.surah.englishName} ${ar.surah.number}:${ar.numberInSurah}</div>
      <div class="arabic" style="font-family:Amiri;direction:rtl;text-align:right;font-size:24px;line-height:2;margin:10px 0">${ar.text}</div>
      <div class="trans">${tr.text}</div>
      <button class="btn" style="margin-top:12px" onclick="openSura(${ar.surah.number})">Surani ochish</button></div>`);
  } catch (e) { toast('Olinmadi'); }
}

/* ---------- Sozlamalar UI ---------- */
function initSettingsUI() {
  document.getElementById('setTrans').onchange = e => { S.translation = e.target.value; saveSettings(); };
  document.getElementById('setReciter').onchange = e => { S.reciter = e.target.value; saveSettings(); };
  const f = document.getElementById('setFont'); f.value = S.font;
  f.onchange = e => { S.font = e.target.value; saveSettings(); };
  const refresh = () => {
    document.getElementById('setTranslit').classList.toggle('on', S.translit);
    document.getElementById('setArabic').classList.toggle('on', S.arabic);
  };
  document.getElementById('setTranslit').onclick = () => { S.translit = !S.translit; saveSettings(); refresh(); };
  document.getElementById('setArabic').onclick = () => { S.arabic = !S.arabic; saveSettings(); refresh(); };
  refresh();
}

export function initMore(showBookmarks) {
  initSettingsUI();
  document.getElementById('mJuz').onclick = showJuz;
  document.getElementById('mQibla').onclick = showQibla;
  document.getElementById('mHijri').onclick = showHijri;
  document.getElementById('mBookmarks').onclick = showBookmarks;
  document.getElementById('randomBtn').onclick = randomAyah;
}
