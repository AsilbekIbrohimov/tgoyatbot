import { API } from './config.js';
import { jget } from './api.js';
import { S } from './settings.js';

// Barcha tarjima va qori (audio) edition'larini yuklab, tanlash select'lariga joylaydi
export async function initEditions() {
  try {
    const eds = await jget(API + '/edition?type=translation');
    const sel = document.getElementById('setTrans');
    const pri = ['de.aburida', 'id.indonesian', 'fr.hamidullah', 'ur.jalandhry', 'tr.diyanet', 'ru.kuliev', 'en.sahih', 'uz.sodik'];
    eds.sort((a, b) => (pri.indexOf(b.identifier) - pri.indexOf(a.identifier)) || a.language.localeCompare(b.language));
    sel.innerHTML = eds.map(e => `<option value="${e.identifier}">${e.language.toUpperCase()} — ${e.englishName}</option>`).join('');
    sel.value = S.translation;
  } catch (e) {}

  try {
    const eds = await jget(API + '/edition?format=audio&type=versebyverse');
    const sel = document.getElementById('setReciter');
    sel.innerHTML = eds.map(e => `<option value="${e.identifier}">${e.englishName} (${e.language})</option>`).join('');
    sel.value = S.reciter;
  } catch (e) {}
}
