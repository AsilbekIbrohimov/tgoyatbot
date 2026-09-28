import re

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery

from loader import db
from data.suralist import suralist
from data.ayah_counts import AYAH_COUNTS
from utils.get_link import get_link
from utils.ayah_text import get_ayah_text

regex_router = Router()

_PATTERN = re.compile(r'^(\d{1,3})[: ](\d{1,3})$')


@regex_router.message(StateFilter("*"), F.text.regexp(_PATTERN))
async def quick_lookup(message: Message):
    m = _PATTERN.match(message.text.strip())
    sura, ayah = int(m.group(1)), int(m.group(2))

    if sura < 1 or sura > 114:
        await message.reply("Sura raqami noto'g'ri kiritildi")
        return
    if ayah < 1 or ayah > AYAH_COUNTS.get(sura, 0):
        await message.reply("Oyat raqami noto'g'ri kiritildi")
        return

    uid = message.from_user.id
    text = await get_ayah_text(sura, ayah, db.get_text_ed(uid))
    link = await get_link(sura, ayah, db.get_reciter(uid))
    await message.reply(f"{suralist[sura - 1]} surasi {ayah}-oyat\n\n{text}{link}")


@regex_router.callback_query(StateFilter("*"), F.data == "delete")
async def delete_message(call: CallbackQuery):
    await call.message.delete()
    await call.answer()
