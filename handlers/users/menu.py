from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.searcherState import Searcher, OyatRead, SuraSearch
from states.adminState import Feedback, Settings
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard
from keyboards.default.suralistKeyboard import suraKeyboard1
from keyboards.default.settingsKeyboard import settingsKeyboard
from .common import (
    BTN_MAIN, BTN_GENERAL, BTN_OYATLAR, BTN_SURADAN, BTN_SOZLAMALAR, BTN_FIKR,
)
from .start import go_main_menu

menu_router = Router()


@menu_router.message(Command("help"), StateFilter("*"))
async def bot_help(message: Message, state: FSMContext):
    await message.answer(
        "Buyruqlar: \n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam\n"
        "/search - Qidiruv"
    )


@menu_router.message(F.text == BTN_MAIN, StateFilter("*"))
async def to_main(message: Message, state: FSMContext):
    await go_main_menu(message, state)


@menu_router.message(F.text == BTN_GENERAL, StateFilter(None))
async def open_general(message: Message, state: FSMContext):
    await message.answer(
        "Qidirish uchun matn kiriting.\nEtibor bering qidirish tizimi qur'onning "
        "arabcha matni va o'zbekcha tarjimasi matnidan izlaydi",
        reply_markup=mainMenuKeyboard,
    )
    await state.set_state(Searcher.search)


@menu_router.message(F.text == BTN_OYATLAR, StateFilter(None))
async def open_oyatlar(message: Message, state: FSMContext):
    await message.answer(
        "Oʻzingizga kerakli suraning raqamini kiriting, nomini yozing yoki "
        "tugmalardan foydalaning",
        reply_markup=suraKeyboard1,
    )
    await state.set_state(OyatRead.choose_sura)


@menu_router.message(F.text == BTN_SURADAN, StateFilter(None))
async def open_suradan(message: Message, state: FSMContext):
    await message.answer(
        "O'zingizga kerakli surani tanlang.\nEtibor bering qidirish tizimi qur'onning "
        "arabcha matni va o'zbekcha tarjimasi matnidan izlaydi",
        reply_markup=suraKeyboard1,
    )
    await state.set_state(SuraSearch.choose_sura)


@menu_router.message(F.text == BTN_SOZLAMALAR, StateFilter(None))
async def open_settings(message: Message, state: FSMContext):
    await message.answer("Sozlamalar", reply_markup=settingsKeyboard)
    await state.set_state(Settings.menu)


@menu_router.message(F.text == BTN_FIKR, StateFilter(None))
async def open_feedback(message: Message, state: FSMContext):
    await message.answer(
        "Assalomu alaykum. Fikringizni yozib qoldiring. Adminga xabaringiz yuboriladi.",
        reply_markup=mainMenuKeyboard,
    )
    await state.set_state(Feedback.waiting)
