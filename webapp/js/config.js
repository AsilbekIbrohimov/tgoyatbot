// API manzillari va umumiy konstantalar
export const API = "https://api.alquran.cloud/v1";
export const ALADHAN = "https://api.aladhan.com/v1";
export const CDN_AYAH = (rec, n) => `https://cdn.islamic.network/quran/audio/128/${rec}/${n}.mp3`;
export const CDN_SURA = (rec, n) => `https://cdn.islamic.network/quran/audio-surah/128/${rec}/${n}.mp3`;

// Bot admin backend manzili (HTTPS). Bo'sh bo'lsa admin panel ko'rinmaydi.
// Botni serveringizda ishga tushirib, bu yerga public HTTPS manzilni yozing.
// Masalan: "https://bot.sizningdomen.uz"
export const ADMIN_API = "";

export const DEFAULTS = {
  translation: 'uz.sodik',
  reciter: 'ar.alafasy',
  translit: true,   // lotincha o'qilishi standart yoqilgan
  arabic: true,
  font: '1',
};
