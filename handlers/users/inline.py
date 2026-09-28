import re

from aiogram import Router
from aiogram.types import (
    InlineQuery, InlineQueryResultArticle, InputTextMessageContent,
    InlineQueryResultAudio,
)

from loader import db
from data.suralist import suralist
from data.ayah_counts import AYAH_COUNTS
from utils.ayah_text import get_ayah_text
from utils.searcher import search

inline_router = Router()

_REF = re.compile(r'^\s*(\d{1,3})[:\s.-](\d{1,3})\s*$')
CDN = lambda rec, g: f"https://cdn.islamic.network/quran/audio/128/{rec}/{g}.mp3"


def _global_ayah(sura, ayah):
    return sum(AYAH_COUNTS[s] for s in range(1, sura)) + ayah


@inline_router.inline_query()
async def inline_query(q: InlineQuery):
    uid = q.from_user.id
    text_ed = db.get_text_ed(uid) if db.select_user(id=uid) else 'local.sodiq'
    reciter = db.get_reciter(uid) if db.select_user(id=uid) else 'ar.alafasy'
    query = (q.query or '').strip()
    results = []

    # 1) "sura:ayah" -> oyat + audio
    m = _REF.match(query)
    if m:
        sura, ayah = int(m.group(1)), int(m.group(2))
        if 1 <= sura <= 114 and 1 <= ayah <= AYAH_COUNTS.get(sura, 0):
            text = await get_ayah_text(sura, ayah, text_ed)
            body = f"{suralist[sura - 1]} — {sura}:{ayah}\n\n{text}"
            g = _global_ayah(sura, ayah)
            results.append(InlineQueryResultArticle(
                id=f"a{sura}_{ayah}", title=f"{suralist[sura - 1]} {sura}:{ayah}",
                description=text[:90],
                input_message_content=InputTextMessageContent(message_text=body),
            ))
            results.append(InlineQueryResultAudio(
                id=f"au{sura}_{ayah}", audio_url=CDN(reciter, g),
                title=f"{suralist[sura - 1]} {sura}:{ayah}", performer=reciter,
            ))
            await q.answer(results, cache_time=60, is_personal=True)
            return

    # 2) Matn bo'yicha qidiruv (mahalliy, fuzzy)
    if len(query) >= 2:
        trans = db.get_trans(uid) if db.select_user(id=uid) else 0
        found = await search(query, trans=trans)
        if found and found[0] not in ('қидирув натижаси мавжуд эмас', 'qidiruv natijasi mavjud emas'):
            for i, item in enumerate(found[:20]):
                snippet = item.split('\n', 1)[-1]
                results.append(InlineQueryResultArticle(
                    id=f"s{i}", title=f"Natija {i + 1}", description=snippet[:90],
                    input_message_content=InputTextMessageContent(message_text=snippet),
                ))

    if not results:
        results.append(InlineQueryResultArticle(
            id="help", title="Qidirish: so'z yoki 2:255",
            description="Masalan: rahmat  yoki  2:255",
            input_message_content=InputTextMessageContent(
                message_text="Qur'on boti: @oyatlaruzbot orqali oyat qidiring."),
        ))
    await q.answer(results, cache_time=30, is_personal=True)
