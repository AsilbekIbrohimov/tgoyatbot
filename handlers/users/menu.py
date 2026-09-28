from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from loader import db
from states.searcherState import Searcher, OyatRead, SuraSearch
from states.adminState import Feedback, Settings
from utils.i18n import t, Btn, back_main_kb, sura_kb, settings_kb
from .start import go_main_menu

menu_router = Router()


@menu_router.message(Command("help"), StateFilter("*"))
async def bot_help(message: Message, state: FSMContext):
    await message.answer(t('m_help', db.get_ui_lang(message.from_user.id)))


@menu_router.message(Btn('b_main'), StateFilter("*"))
async def to_main(message: Message, state: FSMContext):
    await go_main_menu(message, state)


@menu_router.message(Btn('b_general'), StateFilter(None))
async def open_general(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    await message.answer(t('m_general_prompt', lang), reply_markup=back_main_kb(lang))
    await state.set_state(Searcher.search)


@menu_router.message(Btn('b_oyatlar'), StateFilter(None))
async def open_oyatlar(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    await message.answer(t('m_choose_sura', lang), reply_markup=sura_kb(1, lang))
    await state.set_state(OyatRead.choose_sura)


@menu_router.message(Btn('b_suradan'), StateFilter(None))
async def open_suradan(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    await message.answer(t('m_suradan_prompt', lang), reply_markup=sura_kb(1, lang))
    await state.set_state(SuraSearch.choose_sura)


@menu_router.message(Btn('b_settings'), StateFilter(None))
async def open_settings(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    await message.answer(t('m_settings', lang), reply_markup=settings_kb(lang))
    await state.set_state(Settings.menu)


@menu_router.message(Btn('b_feedback'), StateFilter(None))
async def open_feedback(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    await message.answer(t('m_feedback_prompt', lang), reply_markup=back_main_kb(lang))
    await state.set_state(Feedback.waiting)
