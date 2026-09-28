// API manzillari va umumiy konstantalar
export const API = "https://api.alquran.cloud/v1";
export const ALADHAN = "https://api.aladhan.com/v1";
export const CDN_AYAH = (rec, n) => `https://cdn.islamic.network/quran/audio/128/${rec}/${n}.mp3`;
export const CDN_SURA = (rec, n) => `https://cdn.islamic.network/quran/audio-surah/128/${rec}/${n}.mp3`;

export const DEFAULTS = {
  translation: 'uz.sodik',
  reciter: 'ar.alafasy',
  translit: true,   // lotincha o'qilishi standart yoqilgan
  arabic: true,
  font: '1',
};
