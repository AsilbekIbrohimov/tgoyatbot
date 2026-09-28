import { ALADHAN } from './config.js';
import { jget } from './api.js';
import { toast } from './ui.js';

function renderPrayer(t) {
  const order = [['Fajr', 'Bomdod'], ['Sunrise', 'Quyosh'], ['Dhuhr', 'Peshin'], ['Asr', 'Asr'], ['Maghrib', 'Shom'], ['Isha', 'Xufton']];
  const now = new Date(), cur = now.getHours() * 60 + now.getMinutes();
  const times = order.map(([k]) => { const [h, m] = t[k].split(':').map(Number); return h * 60 + m; });
  let nextIdx = -1;
  for (let i = 0; i < times.length; i++) { if (times[i] > cur) { nextIdx = i; break; } }
  return `<div class="card">${order.map(([k, uz], i) =>
    `<div class="prayer ${i === nextIdx ? 'next' : ''}"><span class="name">${uz}${i === nextIdx ? ' · keyingi' : ''}</span><span class="time">${t[k]}</span></div>`).join('')}</div>`;
}

async function prayerByCity(city, country) {
  const box = document.getElementById('prayerResult');
  box.innerHTML = '<div class="spin"></div>';
  const m = document.getElementById('pMethod').value;
  try {
    const d = await jget(`${ALADHAN}/timingsByCity?city=${encodeURIComponent(city)}&country=${encodeURIComponent(country || '')}&method=${m}`);
    box.innerHTML = `<div class="section-title">${city}${country ? ', ' + country : ''}</div>` + renderPrayer(d.timings) + `<p class="hint">Hijriy: ${d.date.hijri.date} (${d.date.hijri.month.en})</p>`;
  } catch (e) { box.innerHTML = '<div class="err">Shahar topilmadi.</div>'; }
}

async function prayerByCoords(lat, lng) {
  const box = document.getElementById('prayerResult');
  box.innerHTML = '<div class="spin"></div>';
  const m = document.getElementById('pMethod').value;
  try {
    const d = await jget(`${ALADHAN}/timings?latitude=${lat}&longitude=${lng}&method=${m}`);
    box.innerHTML = `<div class="section-title">Joriy joylashuv</div>` + renderPrayer(d.timings) + `<p class="hint">Hijriy: ${d.date.hijri.date} (${d.date.hijri.month.en})</p>`;
  } catch (e) { box.innerHTML = '<div class="err">Vaqtlar olinmadi.</div>'; }
}

export function initPrayer() {
  document.getElementById('pGo').onclick = () => {
    const c = document.getElementById('pCity').value.trim();
    const co = document.getElementById('pCountry').value.trim();
    if (c) prayerByCity(c, co);
  };
  document.getElementById('geoBtn').onclick = () => {
    if (!navigator.geolocation) { toast('Geolokatsiya yo‘q'); return; }
    navigator.geolocation.getCurrentPosition(
      p => prayerByCoords(p.coords.latitude, p.coords.longitude),
      () => toast('Joylashuv olinmadi'));
  };
}
