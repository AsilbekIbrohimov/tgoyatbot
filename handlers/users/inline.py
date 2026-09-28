import re

from aiogram import Router
from aiogram.types import (
    InlineQuery, InlineQueryResultArticle, InputTextMessageContent,
)

from loader import db
from data.suralist import suralist
from data.ayah_counts import AYAH_COUNTS
from utils.ayah_text import get_ayah_text
from utils.searcher import search

inline_router = Router()

_REF = re.compile(r'^\s*(\d{1,3})[:\s.-](\d{1,3})\s*$')
CDN = lambda rec, g: f"https://cdn.islamic.network/quran/audio/128/{rec}/{g}.mp3"
# Arab yozuvi (harflar + diakritik belgilar) — inline natijadan olib tashlanadi
_ARABIC = re.compile(r'[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]+')


def _strip_arabic(s: str) -> str:
    s = _ARABIC.sub('', s)
    return re.sub(r'\s+', ' ', s).strip()


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
            g = _global_ayah(sura, ayah)
            # Audio — ko'rinmas belgi (zero-width) tagidagi yashirin havola
            hidden = f"<a href='{CDN(reciter, g)}'>{chr(8203)}</a>"
            body = f"{suralist[sura - 1]} — {sura}:{ayah}\n\n{text}{hidden}"
            results.append(InlineQueryResultArticle(
                id=f"a{sura}_{ayah}", title=f"{suralist[sura - 1]} {sura}:{ayah}",
                description=text[:90],
                input_message_content=InputTextMessageContent(
                    message_text=body, parse_mode="HTML"),
            ))
            await q.answer(results, cache_time=60, is_personal=True)
            return

    # 2) Matn bo'yicha qidiruv (mahalliy, fuzzy)
    if len(query) >= 2:
        trans = db.get_trans(uid) if db.select_user(id=uid) else 0
        found = await search(query, trans=trans)
        if found and found[0] not in ('қидирув натижаси мавжуд эмас', 'qidiruv natijasi mavjud emas'):
            for i, item in enumerate(found[:20]):
                full = item.split('\n', 1)[-1]          # arabcha + tarjima (yuboriladi)
                preview = _strip_arabic(full)            # faqat qidirilgan til (ro'yxatda)
                if not preview:
                    continue
                results.append(InlineQueryResultArticle(
                    id=f"s{i}", title=f"{i + 1}. {preview[:40]}", description=preview[:100],
                    input_message_content=InputTextMessageContent(message_text=full),
                ))

    if not results:
        results.append(InlineQueryResultArticle(
            id="help", title="Qidirish: so'z yoki 2:255",
            description="Masalan: rahmat  yoki  2:255",
            input_message_content=InputTextMessageContent(
                message_text="Qur'on boti: @oyatlaruzbot orqali oyat qidiring."),
        ))
    await q.answer(results, cache_time=30, is_personal=True)
