"""Sura raqamini aniqlash va oyat sonini olish."""
import re

from rapidfuzz import fuzz

from data.suralist import suralist
from data.ayah_counts import AYAH_COUNTS

_LEADING_NUM = re.compile(r'^\s*(\d{1,3})')


def resolve_sura(text: str):
    """Matndan sura raqamini aniqlaydi (raqam yoki nom bo'yicha). Topilmasa None."""
    if not text:
        return None
    text = text.strip()
    m = _LEADING_NUM.match(text)
    if m:
        n = int(m.group(1))
        return n if 1 <= n <= 114 else None
    best, best_score = None, 0
    for i, name in enumerate(suralist, start=1):
        score = fuzz.ratio(text.lower(), name.strip().lower())
        if score > best_score:
            best, best_score = i, score
    return best if best_score > 80 else None


def ayah_count(raqam: int) -> int:
    return AYAH_COUNTS.get(raqam, 0)
