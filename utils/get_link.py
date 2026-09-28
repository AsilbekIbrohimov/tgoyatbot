import asyncio
import requests

from data.reciters import DEFAULT_RECITER


def _fetch_link(sura, oyat, edition) -> str:
    url = f"https://api.alquran.cloud/v1/ayah/{sura}:{oyat}/{edition}"
    audio = requests.get(url, timeout=10).json()['data']['audio']
    return f"<a href='{audio}'>{chr(8203)}</a>"


async def get_link(sura, oyat, edition: str = DEFAULT_RECITER) -> str:
    """Oyatning audio havolasini (yashirin link) qaytaradi.

    `edition` — qiroat identifikatori (masalan 'ar.alafasy', 'uz.sodik-audio').
    Tarmoq bloklamasligi uchun alohida oqimda ishlaydi; xatoda bo'sh qaytaradi.
    """
    try:
        return await asyncio.to_thread(_fetch_link, sura, oyat, edition)
    except Exception:
        return ""
