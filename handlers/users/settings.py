from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import db
from states.adminState import Settings
from utils.i18n import t, Btn, settings_kb, main_menu_kb, lang_inline_kb
from utils.editions import (
    get_translations, get_reciters, build_page, label_of, LOCAL_TRANS_MAP,
)

settings_router = Router()


@settings_router.message(Command("settings"), StateFilter("*"))
async def settings_cmd(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    await message.answer(t('m_settings', lang), reply_markup=settings_kb(lang))
    await state.set_state(Settings.menu)


# ---------- Interfeys tili ----------
@settings_router.message(Settings.menu, Btn('b_lang'))
async def choose_lang(message: Message):
    await message.answer("Tilni tanlang / Choose language:", reply_markup=lang_inline_kb())


@settings_router.callback_query(F.data.startswith("setlang:"))
async def set_lang(call: CallbackQuery, state: FSMContext):
    code = call.data.split(":", 1)[1]
    db.update_user_ui_lang(code, call.from_user.id)
    await call.message.edit_text(t('m_lang_saved', code))
    await state.clear()
    await call.message.answer(t('m_welcome', code, name=call.from_user.full_name),
                              reply_markup=main_menu_kb(code))
    await call.answer()


# ---------- Tarjima (barcha API tillari) ----------
@settings_router.message(Settings.menu, Btn('b_trans'))
async def choose_trans(message: Message):
    lang = db.get_ui_lang(message.from_user.id)
    items = await get_translations()
    cur = label_of(items, db.get_text_ed(message.from_user.id))
    await message.answer(t('m_choose_trans', lang, cur=cur), reply_markup=build_page(items, 0, 'tr'))


@settings_router.callback_query(F.data.startswith("trp:"))
async def trans_page(call: CallbackQuery):
    page = int(call.data.split(":", 1)[1])
    items = await get_translations()
    await call.message.edit_reply_markup(reply_markup=build_page(items, page, 'tr'))
    await call.answer()


@settings_router.callback_query(F.data.startswith("tri:"))
async def trans_pick(call: CallbackQuery):
    ed = call.data.split(":", 1)[1]
    db.update_user_text_ed(ed, call.from_user.id)
    if ed in LOCAL_TRANS_MAP:
        db.update_user_trans(LOCAL_TRANS_MAP[ed], call.from_user.id)
    items = await get_translations()
    lang = db.get_ui_lang(call.from_user.id)
    await call.message.edit_text(t('m_saved', lang) + f"\n{label_of(items, ed)}")
    await call.answer()


# ---------- Qori (barcha API qorilari) ----------
@settings_router.message(Settings.menu, Btn('b_reciter'))
async def choose_reciter(message: Message):
    lang = db.get_ui_lang(message.from_user.id)
    items = await get_reciters()
    cur = label_of(items, db.get_reciter(message.from_user.id))
    await message.answer(t('m_choose_reciter', lang, cur=cur), reply_markup=build_page(items, 0, 'rc'))


@settings_router.callback_query(F.data.startswith("rcp:"))
async def reciter_page(call: CallbackQuery):
    page = int(call.data.split(":", 1)[1])
    items = await get_reciters()
    await call.message.edit_reply_markup(reply_markup=build_page(items, page, 'rc'))
    await call.answer()


@settings_router.callback_query(F.data.startswith("rci:"))
async def reciter_pick(call: CallbackQuery):
    ed = call.data.split(":", 1)[1]
    db.update_user_reciter(ed, call.from_user.id)
    items = await get_reciters()
    lang = db.get_ui_lang(call.from_user.id)
    await call.message.edit_text(t('m_saved', lang) + f"\n{label_of(items, ed)}")
    await call.answer()


@settings_router.callback_query(F.data == "noop")
async def noop(call: CallbackQuery):
    await call.answer()
