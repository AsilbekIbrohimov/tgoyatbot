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
from utils.i18n import t, Btn, read_kb, sura_kb, sura_kb_for
from keyboards.inline.ContinueKeyboard import ContinueKeyboard
from .common import ayah_count, resolve_sura

read_router = Router()

_DIGIT = re.compile(r'^\d{1,3}$')
_RANGE = re.compile(r'^(\d{1,3})-(\d{1,3})$')
_LIST = re.compile(r'^\d{1,3}(,\d{1,3})+$')
PAGE_LIMIT = 50


async def _send_verse(message: Message, sura, ayah, text_ed, reciter):
    text = await get_ayah_text(sura, ayah, text_ed)
    link = await get_link(sura, ayah, reciter)
    await message.answer(f"{suralist[sura - 1]} — {ayah}\n\n{text}{link}")


@read_router.message(OyatRead.choose_sura, Btn('b_next'))
async def next_page(message: Message):
    await message.answer("→", reply_markup=sura_kb(2, db.get_ui_lang(message.from_user.id)))


@read_router.message(OyatRead.choose_sura, Btn('b_prev'))
async def prev_page(message: Message):
    await message.answer("←", reply_markup=sura_kb(1, db.get_ui_lang(message.from_user.id)))


@read_router.message(OyatRead.choose_sura, F.text)
async def choose_sura(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    sura = resolve_sura(message.text)
    if not sura:
        await message.answer(t('m_sura_not_found', lang))
        return
    soni = ayah_count(sura)
    await state.update_data(sura=sura, soni=soni)
    await state.set_state(OyatRead.reading)
    await message.answer(t('m_ayah_info', lang, name=suralist[sura - 1], soni=soni),
                         reply_markup=read_kb(lang))


@read_router.message(OyatRead.reading, Btn('b_back'))
async def back_to_choose(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    data = await state.get_data()
    await state.set_state(OyatRead.choose_sura)
    await message.answer(t('m_choose_sura', lang), reply_markup=sura_kb_for(data.get("sura", 1), lang))


@read_router.message(OyatRead.reading, Btn('b_sura_audio'))
async def surah_audio(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    data = await state.get_data()
    sura = data.get("sura")
    if not sura:
        return
    reciter = db.get_reciter(message.from_user.id)
    for ed in (reciter, reciter.replace('-2', '')):
        url = f"https://cdn.islamic.network/quran/audio-surah/128/{ed}/{sura}.mp3"
        try:
            await message.answer_audio(url, title=f"{suralist[sura - 1]}")
            return
        except Exception:
            continue
    await message.answer(t('m_sura_audio_na', lang))


@read_router.message(OyatRead.reading, F.text)
async def read_ayah(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    data = await state.get_data()
    sura, soni = data.get("sura"), data.get("soni", 0)
    if not sura:
        await state.set_state(OyatRead.choose_sura)
        await message.answer(t('m_choose_sura', lang))
        return

    uid = message.from_user.id
    text_ed = db.get_text_ed(uid)
    reciter = db.get_reciter(uid)
    text = message.text.strip()

    if _DIGIT.match(text):
        n = int(text)
        if n < 1 or n > soni:
            await message.answer(t('m_num_range', lang, soni=soni))
            return
        await _send_verse(message, sura, n, text_ed, reciter)
        return

    m = _RANGE.match(text)
    if m:
        a1, a2 = int(m.group(1)), int(m.group(2))
        if a1 < 1 or a2 > soni or a1 > a2:
            await message.answer(t('m_range_invalid', lang))
            return
        cur = a1
        while cur <= a2:
            await _send_verse(message, sura, cur, text_ed, reciter)
            await asyncio.sleep(1.0)
            if cur % PAGE_LIMIT == 0 and cur != a2:
                await state.update_data(cur=cur + 1, end=a2)
                await message.answer(t('m_continue_q', lang), reply_markup=ContinueKeyboard)
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

    await message.answer(t('m_invalid', lang))


@read_router.callback_query(OyatRead.reading, F.data == "davomi")
async def continue_reading(call: CallbackQuery, state: FSMContext):
    lang = db.get_ui_lang(call.from_user.id)
    data = await state.get_data()
    sura, cur, end = data.get("sura"), data.get("cur"), data.get("end")
    if not (sura and cur and end):
        await call.answer("—", show_alert=True)
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
            await call.message.answer(t('m_continue_q', lang), reply_markup=ContinueKeyboard)
            await call.answer()
            return
        cur += 1
    await call.answer()
