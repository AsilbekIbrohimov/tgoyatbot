# Oyat — Qur'on Telegram bot + Mini App

Ko'p tilli Qur'on boti (aiogram 3): oyat o'qish, tarjima (barcha API tillari),
qori tanlash, audio, qidiruv, inline rejim, namoz vaqtlari (Mini App), donat (Stars),
admin panel. Ma'lumot manbai: [AlQuran Cloud](https://alquran.cloud) va [Aladhan](https://aladhan.com) API.

## Imkoniyatlar
- 📖 114 sura, oyat/oraliq/ro'yxat bo'yicha o'qish, butun sura audiosi
- 🌍 Interfeys 5 tilda (uz/en/ru/tr/ar), tarjima — barcha API tillari, transliteratsiya
- 🎧 30+ qori, oyat audiosi (yashirin havola)
- 🔎 Qidiruv (fuzzy, kirill/lotin), 🔤 inline rejim (`@bot 2:255` yoki so'z)
- 🕌 Mini App: namoz vaqtlari, qibla, hijriy sana, juz, xatcho'p
- ❤️ Donat (Telegram Stars), 🛠 admin panel (bot + Mini App)

## 1. Lokal ishga tushirish
```bash
pip install -r requirements.txt
cp .env.example .env          # .env ni to'ldiring (BOT_TOKEN majburiy)
python app.py
```

## 2. Server (systemd)
```bash
# kodni /home/ubuntu/oyatbot ga joylang, .env ni to'ldiring
sudo cp deploy/oyatbot.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now oyatbot
journalctl -u oyatbot -f
```

## 3. Mini App (GitHub Pages)
`webapp/` papkasi statik ilova. GitHub Pages: Settings → Pages → Deploy from a branch → `main` / `(root)`.
Manzil: `https://<user>.github.io/<repo>/webapp/`. Botdagi menu tugmasi shu manzilni ochadi (`WEBAPP_URL`).

## 4. Inline rejim
@BotFather → /mybots → bot → Bot Settings → Inline Mode → **Turn on** (placeholder qo'ying).

## 5. Mini App admin paneli (backend)
Bot ichida `aiohttp` server (`WEBAPP_API_PORT`, standart 8080) `initData` ni HMAC bilan tekshiradi.
Mini App (github.io) unga **HTTPS** orqali ulanishi kerak:

- **Nginx + TLS:** `deploy/nginx.conf.example` ga qarang, `certbot` bilan sertifikat oling.
- **Yoki tez sinash:** `cloudflared tunnel --url http://localhost:8080` → bepul HTTPS manzil.

So'ng `webapp/js/config.js` dagi `ADMIN_API` ga o'sha HTTPS manzilni yozing va push qiling.
Admin (ADMINS) Mini App'ni ochsa, "Ko'proq" bo'limida panel avtomatik ko'rinadi.

## Muhim
- `.env`, `data/main.db`, `*.session` — git'ga yuklanmaydi.
- Eski token git tarixida qolgan bo'lsa, @BotFather → **/revoke** bilan yangilang.
