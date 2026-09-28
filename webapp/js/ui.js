import { TG } from './telegram.js';

const views = { suralar: 'v-suralar', reader: 'v-reader', search: 'v-search', prayer: 'v-prayer', more: 'v-more' };
const titles = { suralar: "Qur'on", reader: "Qur'on", search: "Qidiruv", prayer: "Namoz vaqtlari", more: "Ko'proq" };

export function show(tab) {
  Object.values(views).forEach(id => document.getElementById(id).classList.remove('active'));
  document.getElementById(views[tab] || 'v-suralar').classList.add('active');
  document.querySelectorAll('.tabbar button').forEach(b => b.classList.toggle('on', b.dataset.tab === tab));
  document.getElementById('title').textContent = titles[tab] || "Qur'on";
  document.getElementById('backBtn').hidden = tab !== 'reader';
  window.scrollTo(0, 0);
}

export function detail(html) {
  const el = document.getElementById('moreDetail');
  el.innerHTML = html;
  el.scrollIntoView({ behavior: 'smooth' });
}

export function toast(m) {
  if (TG && TG.showToast) { try { TG.showToast(m); return; } catch (e) {} }
  const d = document.createElement('div');
  d.textContent = m;
  d.style.cssText = 'position:fixed;bottom:120px;left:50%;transform:translateX(-50%);background:var(--text);color:var(--bg);padding:8px 16px;border-radius:20px;z-index:99;font-size:13px';
  document.body.appendChild(d);
  setTimeout(() => d.remove(), 1500);
}
