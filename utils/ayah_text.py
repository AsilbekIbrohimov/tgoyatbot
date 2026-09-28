"""Oyat matnini tanlangan edition bo'yicha qaytaradi (mahalliy yoki API)."""
import asyncio

import requests

from data.qurandict import qurandict
from data.qurandict2 import qurandict2
from data.text_editions import DEFAULT_TEXT_ED

_cache: dict = {}  # (edition, sura, ayah) -> matn


def _fetch_api_text(edition, sura, ayah) -> str:
    url = f"https://api.alquran.cloud/v1/ayah/{sura}:{ayah}/{edition}"
    return requests.get(url, timeout=10).json()['data']['text']


async def get_ayah_text(sura: int, ayah: int, text_ed: str = DEFAULT_TEXT_ED) -> str:
    if text_ed == 'local.sodiq' or not text_ed:
        return qurandict[str(sura)][ayah - 1]['text']
    if text_ed == 'local.mansur':
        return qurandict2[str(sura)][ayah - 1]['text']

    key = (text_ed, sura, ayah)
    if key in _cache:
        return _cache[key]
    try:
        text = await asyncio.to_thread(_fetch_api_text, text_ed, sura, ayah)
    except Exception:
        # API ishlamasa mahalliy o'zbekchaga qaytamiz
        return qurandict[str(sura)][ayah - 1]['text']
    _cache[key] = text
    return text
