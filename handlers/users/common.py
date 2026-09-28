"""Handlerlar uchun umumiy konstantalar va yordamchi funksiyalar."""
import re

from rapidfuzz import fuzz

from data.suralist import suralist
from data.ayah_counts import AYAH_COUNTS
from keyboards.default.suralistKeyboard import suraKeyboard1, suraKeyboard2

# Menyu tugmalari matni (bitta joyda saqlanadi)
BTN_MAIN = '🔝 Asosiy Menyu'
BTN_BACK = '⬅️ Orqaga'
BTN_GENERAL = 'Umumiy izlash🔎'
BTN_OYATLAR = 'Oyatlar'
BTN_SURADAN = 'Suradan izlash'
BTN_SOZLAMALAR = 'Sozlamalar'
BTN_FIKR = 'Fikr bildirish✍️'
BTN_NEXT = 'keyingi ➡️'
BTN_PREV = '⬅️ oldingi'

_LEADING_NUM = re.compile(r'^\s*(\d{1,3})')


def sura_keyboard(raqam: int):
    """Sura raqamiga mos klaviatura (1-56 -> 1-jadval, 57+ -> 2-jadval)."""
    return suraKeyboard2 if raqam > 56 else suraKeyboard1


def resolve_sura(text: str):
    """Matndan sura raqamini aniqlaydi (raqam yoki nom bo'yicha). Topilmasa None."""
    if not text:
        return None
    text = text.strip()

    m = _LEADING_NUM.match(text)
    if m:
        n = int(m.group(1))
        if 1 <= n <= 114:
            return n
        return None

    best, best_score = None, 0
    for i, name in enumerate(suralist, start=1):
        score = fuzz.ratio(text.lower(), name.strip().lower())
        if score > best_score:
            best, best_score = i, score
    if best_score > 80:
        return best
    return None


def answertext(soni: int, raqam: int) -> str:
    return (
        f"{suralist[raqam - 1]} surasi {soni} ta oyatdan iborat\n\n"
        "o'qimoqchi bo'lgan oyatingizning raqamini kiriting\n\n"
        "yoki ko'proq oyat o'qimoqchi bo'lsangiz oyatlarni quyidagi ko'rinishda "
        "kiriting\n\n➡️  2,5,12,13 ....\n\nYoki\n\n➡️  1-5 ko'rinishida xabar jo'nating\n\n"
        f"Suraning barcha oyatlarni o'qish uchun 1-{soni} deb xabar jo'nating"
    )


def ayah_count(raqam: int) -> int:
    return AYAH_COUNTS.get(raqam, 0)
