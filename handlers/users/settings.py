from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from loader import db
from states.adminState import Settings
from keyboards.default.settingsKeyboard import settingsKeyboard
from keyboards.default.reciterKeyboard import reciterKeyboard
from keyboards.default.textEditionKeyboard import textEditionKeyboard
from data.reciters import LABEL_TO_ID as REC_LABEL_TO_ID, ID_TO_LABEL as REC_ID_TO_LABEL
from data.text_editions import (
    LABEL_TO_ID as TXT_LABEL_TO_ID, ID_TO_LABEL as TXT_ID_TO_LABEL, LOCAL_TRANS,
)
from .start import go_main_menu

settings_router = Router()


@settings_router.message(Command("settings"), StateFilter("*"))
async def settings_cmd(message: Message, state: FSMContext):
    await message.answer("Sozlamalar", reply_markup=settingsKeyboard)
    await state.set_state(Settings.menu)


# --- Tarjima / matn edition ---
@settings_router.message(Settings.menu, F.text == 'tarjima')
async def choose_translation(message: Message, state: FSMContext):
    current = TXT_ID_TO_LABEL.get(db.get_text_ed(message.from_user.id), '—')
    await message.answer(
        f"Hozirgi tarjima: {current}\n\nRo'yxatdan tarjima yoki transliteratsiyani tanlang:",
        reply_markup=textEditionKeyboard,
    )
    await state.set_state(Settings.trans)


@settings_router.message(Settings.trans, F.text.func(lambda t: t in TXT_LABEL_TO_ID))
async def set_translation(message: Message, state: FSMContext):
    ed = TXT_LABEL_TO_ID[message.text]
    db.update_user_text_ed(ed, message.from_user.id)
    # Mahalliy o'zbekcha tanlansa, qidiruv uchun `trans` ni ham moslaymiz
    if ed in LOCAL_TRANS:
        db.update_user_trans(LOCAL_TRANS[ed], message.from_user.id)
    await message.answer(f"Tarjima tanlandi: {message.text} ✅")
    await go_main_menu(message, state)


@settings_router.message(Settings.trans)
async def translation_invalid(message: Message):
    await message.answer("Iltimos ro'yxatdagi tugmalardan birini tanlang.")


# --- Qiroat (qori) ---
@settings_router.message(Settings.menu, F.text == 'Qiroat 🎧')
async def choose_reciter(message: Message, state: FSMContext):
    current = REC_ID_TO_LABEL.get(db.get_reciter(message.from_user.id), '—')
    await message.answer(
        f"Hozirgi qori: {current}\n\nRo'yxatdan qiroatni tanlang:",
        reply_markup=reciterKeyboard,
    )
    await state.set_state(Settings.reciter)


@settings_router.message(Settings.reciter, F.text.func(lambda t: t in REC_LABEL_TO_ID))
async def set_reciter(message: Message, state: FSMContext):
    db.update_user_reciter(REC_LABEL_TO_ID[message.text], message.from_user.id)
    await message.answer(f"Qiroat tanlandi: {message.text} ✅")
    await go_main_menu(message, state)


@settings_router.message(Settings.reciter)
async def reciter_invalid(message: Message):
    await message.answer("Iltimos ro'yxatdagi tugmalardan birini tanlang.")
