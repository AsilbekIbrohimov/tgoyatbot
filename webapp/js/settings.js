import { DEFAULTS } from './config.js';

function load() {
  try { return Object.assign({}, DEFAULTS, JSON.parse(localStorage.getItem('qset') || '{}')); }
  catch (e) { return { ...DEFAULTS }; }
}

export const S = load();

export function applyFont() {
  document.documentElement.style.setProperty('--fs', S.font);
}

export function saveSettings() {
  try { localStorage.setItem('qset', JSON.stringify(S)); } catch (e) {}
  applyFont();
}
