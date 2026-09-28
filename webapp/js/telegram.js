// Telegram WebApp SDK integratsiyasi
export const TG = (window.Telegram && window.Telegram.WebApp) ? window.Telegram.WebApp : null;

export function haptic(t) {
  try { TG && TG.HapticFeedback && TG.HapticFeedback.impactOccurred(t || 'light'); } catch (e) {}
}

function applyTgTheme() {
  if (!TG || !TG.themeParams) return;
  const p = TG.themeParams, r = document.documentElement.style;
  if (p.bg_color) r.setProperty('--bg', p.bg_color);
  if (p.secondary_bg_color) r.setProperty('--card', p.secondary_bg_color);
  if (p.text_color) r.setProperty('--text', p.text_color);
  if (p.hint_color) r.setProperty('--muted', p.hint_color);
  if (p.button_color) r.setProperty('--accent', p.button_color);
  if (p.section_separator_color) r.setProperty('--line', p.section_separator_color);
}

if (TG) {
  try { TG.ready(); TG.expand(); applyTgTheme(); TG.onEvent('themeChanged', applyTgTheme); } catch (e) {}
}
