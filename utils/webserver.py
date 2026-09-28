# -*- coding: utf-8 -*-
"""Mini App admin backend (aiohttp). Telegram initData ni tekshiradi.

Xavfsizlik: har bir so'rovda `initData` HMAC-SHA256 bilan bot tokeni orqali
tekshiriladi (Telegram WebApp spetsifikatsiyasi). Faqat ADMINS ro'yxatidagi
foydalanuvchilar admin amallarini bajara oladi.
"""
import hmac
import hashlib
import json
import time
from urllib.parse import parse_qsl

from aiohttp import web

from data.config import BOT_TOKEN, ADMINS
from loader import db, db2, bot


def _validate(init_data: str, max_age: int = 86400):
    """initData to'g'ri va yangimi? Ha bo'lsa user dict qaytaradi, aks holda None."""
    if not init_data:
        return None
    try:
        parsed = dict(parse_qsl(init_data, strict_parsing=True))
    except Exception:
        return None
    recv_hash = parsed.pop('hash', None)
    if not recv_hash:
        return None
    data_check = '\n'.join(f"{k}={parsed[k]}" for k in sorted(parsed))
    secret = hmac.new(b"WebAppData", BOT_TOKEN.encode(), hashlib.sha256).digest()
    calc = hmac.new(secret, data_check.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(calc, recv_hash):
        return None
    try:
        if time.time() - int(parsed.get('auth_date', '0')) > max_age:
            return None
    except Exception:
        pass
    try:
        return json.loads(parsed.get('user', '{}'))
    except Exception:
        return None


def _admin(init_data):
    user = _validate(init_data)
    if not user or user.get('id') not in ADMINS:
        return None
    return user


def _cors(resp: web.Response) -> web.Response:
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return resp


async def _options(request):
    return _cors(web.Response())


async def h_me(request):
    data = await request.json()
    user = _admin(data.get('initData', ''))
    return _cors(web.json_response({'admin': bool(user), 'name': user.get('first_name') if user else None}))


async def h_stats(request):
    data = await request.json()
    if not _admin(data.get('initData', '')):
        return _cors(web.json_response({'error': 'forbidden'}, status=403))
    users = db.count_users()[0]
    try:
        msgs = db2.count_messages()[0]
    except Exception:
        msgs = 0
    return _cors(web.json_response({'users': users, 'messages': msgs}))


async def h_broadcast(request):
    data = await request.json()
    if not _admin(data.get('initData', '')):
        return _cors(web.json_response({'error': 'forbidden'}, status=403))
    text = (data.get('text') or '').strip()
    if not text:
        return _cors(web.json_response({'error': 'empty'}, status=400))
    users = db.select_all_users()
    sent = failed = 0
    for u in users:
        try:
            await bot.send_message(chat_id=u[0], text=text)
            sent += 1
        except Exception:
            failed += 1
    return _cors(web.json_response({'sent': sent, 'failed': failed, 'total': len(users)}))


def create_app() -> web.Application:
    app = web.Application()
    app.router.add_post('/api/admin/me', h_me)
    app.router.add_post('/api/admin/stats', h_stats)
    app.router.add_post('/api/admin/broadcast', h_broadcast)
    for path in ('/api/admin/me', '/api/admin/stats', '/api/admin/broadcast'):
        app.router.add_options(path, _options)
    app.router.add_get('/', lambda r: web.Response(text='OK'))
    return app
