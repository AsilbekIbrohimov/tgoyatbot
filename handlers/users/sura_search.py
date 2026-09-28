from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import db
from states.searcherState import SuraSearch
from data.suralist import suralist
from utils.searcher import make
from utils.searcher2 import search2
from keyboards.default.mainMenuKeyboard import mainAndbackKeyboard
from keyboards.default.suralistKeyboard import suraKeyboard1, suraKeyboard2
from .common import BTN_BACK, BTN_NEXT, BTN_PREV, ayah_count, resolve_sura, sura_keyboard
from . import pager

sura_search_router = Router()

NO_RESULT = ('қидирув натижаси мавжуд эмас', 'qidiruv natijasi mavjud emas')


@sura_search_router.message(SuraSearch.choose_sura, F.text == BTN_NEXT)
async def next_page(message: Message):
    await message.answer("O'zingizga kerakli surani kiriting", reply_markup=suraKeyboard2)


@sura_search_router.message(SuraSearch.choose_sura, F.text == BTN_PREV)
async def prev_page(message: Message):
    await message.answer("O'zingizga kerakli surani kiriting", reply_markup=suraKeyboard1)


@sura_search_router.message(SuraSearch.choose_sura, F.text)
async def choose_sura(message: Message, state: FSMContext):
    sura = resolve_sura(message.text)
    if not sura:
        await message.answer("Sura topilmadi. Raqam (1-114) yoki nomini kiriting.")
        return
    await state.update_data(sura=sura, soni=ayah_count(sura))
    await state.set_state(SuraSearch.searching)
    await message.answer(
        f"Siz {suralist[sura - 1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiriting.",
        reply_markup=mainAndbackKeyboard,
    )


@sura_search_router.message(SuraSearch.searching, F.text == BTN_BACK)
async def back_to_choose(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.set_state(SuraSearch.choose_sura)
    await message.answer(
        "o'zingizga kerakli surani tanlang",
        reply_markup=sura_keyboard(data.get("sura", 1)),
    )


@sura_search_router.message(SuraSearch.searching, F.text)
async def do_search(message: Message, state: FSMContext):
    data = await state.get_data()
    sura = data.get("sura")
    if not sura:
        await state.set_state(SuraSearch.choose_sura)
        await message.answer("Avval surani tanlang.")
        return
    await message.bot.send_chat_action(message.chat.id, "typing")
    placeholder = await message.reply('🔎')
    text = message.text[:40]
    searched = await search2(sura, text, trans=db.get_trans(message.from_user.id))
    if searched[0] in NO_RESULT:
        await placeholder.edit_text(searched[0])
        return
    maked = await make(searched)
    await pager.show_first(placeholder, state, maked, len(searched))


@sura_search_router.callback_query(SuraSearch.searching, F.data.in_({"-1", "1"}))
async def paginate(call: CallbackQuery, state: FSMContext):
    await pager.paginate(call, state)
