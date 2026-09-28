import asyncio
import re

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import db
from states.searcherState import OyatRead
from data.suralist import suralist
from utils.get_link import get_link
from utils.ayah_text import get_ayah_text
from keyboards.default.readKeyboard import readKeyboard
from keyboards.inline.ContinueKeyboard import ContinueKeyboard
from .common import (
    BTN_BACK, BTN_NEXT, BTN_PREV, answertext, ayah_count, resolve_sura, sura_keyboard,
)
from keyboards.default.suralistKeyboard import suraKeyboard1, suraKeyboard2

read_router = Router()

BTN_SURA_AUDIO = '🎧 Butun sura audiosi'

_DIGIT = re.compile(r'^\d{1,3}$')
_RANGE = re.compile(r'^(\d{1,3})-(\d{1,3})$')
_LIST = re.compile(r'^\d{1,3}(,\d{1,3})+$')
PAGE_LIMIT = 50  # 50 oyatdan keyin "Davomi..." taklif qilamiz


async def _send_verse(message: Message, sura, ayah, text_ed, reciter):
    text = await get_ayah_text(sura, ayah, text_ed)
    link = await get_link(sura, ayah, reciter)
    await message.answer(f"{suralist[sura - 1]} surasi {ayah}-oyat\n\n{text}{link}")


# --- Sura tanlash ---
@read_router.message(OyatRead.choose_sura, F.text == BTN_NEXT)
async def next_page(message: Message):
    await message.answer("O'zingizga kerakli surani kiriting", reply_markup=suraKeyboard2)


@read_router.message(OyatRead.choose_sura, F.text == BTN_PREV)
async def prev_page(message: Message):
    await message.answer("O'zingizga kerakli surani kiriting", reply_markup=suraKeyboard1)


@read_router.message(OyatRead.choose_sura, F.text)
async def choose_sura(message: Message, state: FSMContext):
    sura = resolve_sura(message.text)
    if not sura:
        await message.answer("Sura topilmadi. Raqam (1-114) yoki nomini kiriting.")
        return
    soni = ayah_count(sura)
    await state.update_data(sura=sura, soni=soni)
    await state.set_state(OyatRead.reading)
    await message.answer(answertext(soni, sura), reply_markup=readKeyboard)


# --- Oyat o'qish ---
@read_router.message(OyatRead.reading, F.text == BTN_BACK)
async def back_to_choose(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.set_state(OyatRead.choose_sura)
    await message.answer(
        "o'zingizga kerakli surani tanlang",
        reply_markup=sura_keyboard(data.get("sura", 1)),
    )


@read_router.message(OyatRead.reading, F.text == BTN_SURA_AUDIO)
async def surah_audio(message: Message, state: FSMContext):
    data = await state.get_data()
    sura = data.get("sura")
    if not sura:
        return
    reciter = db.get_reciter(message.from_user.id)
    # audio-surah CDN faqat asosiy edition'larni qo'llaydi ('-2' variantsiz)
    for ed in (reciter, reciter.replace('-2', '')):
        url = f"https://cdn.islamic.network/quran/audio-surah/128/{ed}/{sura}.mp3"
        try:
            await message.answer_audio(url, title=f"{suralist[sura - 1]} surasi")
            return
        except Exception:
            continue
    await message.answer(
        "Bu qori uchun butun sura audiosi mavjud emas yoki sura juda uzun. "
        "Sozlamalar → Qiroat orqali boshqa qorini tanlab ko'ring."
    )


@read_router.message(OyatRead.reading, F.text)
async def read_ayah(message: Message, state: FSMContext):
    data = await state.get_data()
    sura, soni = data.get("sura"), data.get("soni", 0)
    if not sura:
        await message.answer("Avval surani tanlang.")
        await state.set_state(OyatRead.choose_sura)
        return

    uid = message.from_user.id
    text_ed = db.get_text_ed(uid)
    reciter = db.get_reciter(uid)
    text = message.text.strip()

    if _DIGIT.match(text):
        n = int(text)
        if n < 1 or n > soni:
            await message.answer(f"1 dan {soni} gacha raqam kiriting")
            return
        await _send_verse(message, sura, n, text_ed, reciter)
        return

    m = _RANGE.match(text)
    if m:
        start_a, end_a = int(m.group(1)), int(m.group(2))
        if start_a < 1 or end_a > soni or start_a > end_a:
            await message.answer("Nato'g'ri kiritdingiz")
            return
        cur = start_a
        while cur <= end_a:
            await _send_verse(message, sura, cur, text_ed, reciter)
            await asyncio.sleep(1.0)
            if cur % PAGE_LIMIT == 0 and cur != end_a:
                await state.update_data(cur=cur + 1, end=end_a)
                await message.answer("Davomomini ko'rishni xoxlaysizmi?", reply_markup=ContinueKeyboard)
                return
            cur += 1
        return

    if _LIST.match(text):
        for part in text.split(','):
            n = int(part)
            if 1 <= n <= soni:
                await _send_verse(message, sura, n, text_ed, reciter)
                await asyncio.sleep(0.4)
        return

    await message.answer("Natog'ri kiritdingiz")


@read_router.callback_query(OyatRead.reading, F.data == "davomi")
async def continue_reading(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    sura, cur, end = data.get("sura"), data.get("cur"), data.get("end")
    if not (sura and cur and end):
        await call.answer("Davomi topilmadi.", show_alert=True)
        return
    await call.message.delete()
    uid = call.from_user.id
    text_ed = db.get_text_ed(uid)
    reciter = db.get_reciter(uid)
    while cur <= end:
        await _send_verse(call.message, sura, cur, text_ed, reciter)
        await asyncio.sleep(0.4)
        if cur % PAGE_LIMIT == 0 and cur != end:
            await state.update_data(cur=cur + 1, end=end)
            await call.message.answer("Davomomini ko'rishni xoxlaysizmi?", reply_markup=ContinueKeyboard)
            await call.answer()
            return
        cur += 1
    await call.answer()
