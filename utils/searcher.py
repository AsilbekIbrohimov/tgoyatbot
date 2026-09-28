import asyncio

from rapidfuzz import fuzz

from .is_latin import islatin
from .quranlist import quranlist
from .quranlist2 import quranlist2
from .transliterate import to_cyrillic, to_latin


def _scan(quran, text, accuracy):
    """Og'ir (CPU) qism — alohida oqimda ishlaydi."""
    text_low = text.lower()
    res = {}
    for oyat in quran:
        score = fuzz.partial_ratio(oyat["text"].lower(), text_low)
        if score >= accuracy:
            res[f"{oyat['text']} [{oyat['chapter']}:{oyat['verse']}]"] = score
    return sorted(res.items(), key=lambda item: item[1], reverse=True)


async def search(matn, accuracy=80, trans=0):
    quran = quranlist2 if trans else quranlist
    text = await to_cyrillic(matn)
    res = await asyncio.to_thread(_scan, quran, text, accuracy)

    latin = await islatin(matn)
    answer = []
    for tartib, (line, _score) in enumerate(res, start=1):
        if latin:
            answer.append(f"{tartib}.\n{await to_latin(line)}")
        else:
            answer.append(f"{tartib}.\n{line}")

    if answer:
        return answer
    if latin:
        return ["qidiruv natijasi mavjud emas"]
    return ['қидирув натижаси мавжуд эмас']


async def make(arr, length=4000) -> list:
    res = []
    answer = ''
    for i in arr:
        if len(answer + i) < length:
            answer += i + '\n\n'
        else:
            res.append(answer)
            answer = i + '\n\n'
    if answer:
        res.append(answer)
    return res
