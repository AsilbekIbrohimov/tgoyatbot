import { ADMIN_API } from './config.js';
import { TG } from './telegram.js';
import { toast } from './ui.js';

async function api(path, body) {
  const r = await fetch(ADMIN_API + path, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  return r.json();
}

function render(initData) {
  const host = document.getElementById('adminCard');
  if (!host) return;
  host.hidden = false;
  host.innerHTML = `
    <div class="section-title">🛠 Admin panel</div>
    <div class="card" style="padding:14px">
      <button class="btn sec" id="aStats">📊 Statistika</button>
      <div id="aStatsOut" class="muted" style="margin:10px 0"></div>
      <hr style="border:none;border-top:1px solid var(--line);margin:12px 0">
      <div class="lab" style="font-size:13px;color:var(--muted);margin-bottom:6px">📢 Reklama (barcha foydalanuvchilarga)</div>
      <textarea id="aText" rows="3" style="width:100%;border-radius:11px;border:1px solid var(--line);background:var(--card);color:var(--text);padding:10px" placeholder="Xabar matni..."></textarea>
      <button class="btn" id="aSend" style="margin-top:8px">Yuborish</button>
      <div id="aSendOut" class="muted" style="margin-top:8px"></div>
    </div>`;

  document.getElementById('aStats').onclick = async () => {
    document.getElementById('aStatsOut').textContent = 'Yuklanmoqda...';
    try {
      const j = await api('/api/admin/stats', { initData });
      document.getElementById('aStatsOut').innerHTML = `👥 Foydalanuvchilar: <b>${j.users}</b> · ✉️ Xabarlar: <b>${j.messages}</b>`;
    } catch (e) { document.getElementById('aStatsOut').textContent = 'Xatolik'; }
  };

  document.getElementById('aSend').onclick = async () => {
    const text = document.getElementById('aText').value.trim();
    if (!text) { toast('Matn kiriting'); return; }
    document.getElementById('aSendOut').textContent = 'Yuborilmoqda...';
    try {
      const j = await api('/api/admin/broadcast', { initData, text });
      document.getElementById('aSendOut').innerHTML = `✅ Yuborildi: <b>${j.sent}</b> · 🚫 Xato: <b>${j.failed}</b>`;
    } catch (e) { document.getElementById('aSendOut').textContent = 'Xatolik'; }
  };
}

export async function initAdmin() {
  if (!ADMIN_API) return;                       // backend sozlanmagan
  const initData = TG && TG.initData;
  if (!initData) return;                        // Telegram ichida emas
  try {
    const j = await api('/api/admin/me', { initData });
    if (j.admin) render(initData);
  } catch (e) { /* backend yo'q — jim */ }
}
