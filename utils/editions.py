# -*- coding: utf-8 -*-
"""API'dagi barcha tarjima va qori (audio) edition'lari — olish, kesh va sahifali klaviatura."""
import asyncio
import requests

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

_API = "https://api.alquran.cloud/v1/edition"
_cache = {"trans": None, "rec": None}
PER_PAGE = 8

# Mahalliy (tez, oflayn) o'zbekcha tarjimalar — API ro'yxati oldiga qo'shiladi
LOCAL_TRANS = [
    ('local.sodiq', "O'zbek — Shayx M. Sodiq (mahalliy)"),
    ('local.mansur', "O'zbek — Alovuddin Mansur (mahalliy)"),
]
LOCAL_TRANS_MAP = {'local.sodiq': 0, 'local.mansur': 1}


def _fetch(kind):
    if kind == 'trans':
        data = requests.get(_API + "?type=translation", timeout=15).json()['data']
        items = [(e['identifier'], f"{e['language'].upper()} — {e['englishName']}") for e in data]
        items.sort(key=lambda x: x[1])
        return LOCAL_TRANS + items
    else:
        data = requests.get(_API + "?format=audio&type=versebyverse", timeout=15).json()['data']
        return [(e['identifier'], f"{e['englishName']} ({e['language']})") for e in data]


async def get_translations():
    if _cache['trans'] is None:
        _cache['trans'] = await asyncio.to_thread(_fetch, 'trans')
    return _cache['trans']


async def get_reciters():
    if _cache['rec'] is None:
        _cache['rec'] = await asyncio.to_thread(_fetch, 'rec')
    return _cache['rec']


def label_of(items, ident, default='—'):
    for i, lbl in items:
        if i == ident:
            return lbl
    return default


def build_page(items, page: int, prefix: str) -> InlineKeyboardMarkup:
    total = len(items)
    pages = max(1, (total + PER_PAGE - 1) // PER_PAGE)
    page = max(0, min(page, pages - 1))
    chunk = items[page * PER_PAGE:(page + 1) * PER_PAGE]
    rows = [[InlineKeyboardButton(text=lbl, callback_data=f"{prefix}i:{ident}")] for ident, lbl in chunk]
    nav = []
    if page > 0:
        nav.append(InlineKeyboardButton(text="◀️", callback_data=f"{prefix}p:{page-1}"))
    nav.append(InlineKeyboardButton(text=f"{page+1}/{pages}", callback_data="noop"))
    if page < pages - 1:
        nav.append(InlineKeyboardButton(text="▶️", callback_data=f"{prefix}p:{page+1}"))
    rows.append(nav)
    return InlineKeyboardMarkup(inline_keyboard=rows)
