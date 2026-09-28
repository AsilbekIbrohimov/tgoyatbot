import asyncio

from rapidfuzz import fuzz

from .is_latin import islatin
from data.qurandict import qurandict
from data.qurandict2 import qurandict2
from .transliterate import to_cyrillic, to_latin


def _scan(oyatlar, text, accuracy):
    text_low = text.lower()
    res = {}
    for oyat in oyatlar:
        score = fuzz.partial_ratio(oyat["text"].lower(), text_low)
        if score >= accuracy:
            res[f"{oyat['text']} [{oyat['chapter']}:{oyat['verse']}]"] = score
    return sorted(res.items(), key=lambda item: item[1], reverse=True)


async def search2(sura, matn, accuracy=70, trans=0):
    quran = qurandict2 if trans else qurandict
    text = await to_cyrillic(matn)
    res = await asyncio.to_thread(_scan, quran[str(sura)], text, accuracy)

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
