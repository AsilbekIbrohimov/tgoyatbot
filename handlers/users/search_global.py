from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import db
from states.searcherState import Searcher
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard
from utils.searcher import search, make
from . import pager

global_router = Router()

NO_RESULT = ('қидирув натижаси мавжуд эмас', 'qidiruv natijasi mavjud emas')


@global_router.message(Command("search"), StateFilter("*"))
async def search_cmd(message: Message, state: FSMContext):
    await message.answer("Qidirish uchun matn kiriting", reply_markup=mainMenuKeyboard)
    await state.set_state(Searcher.search)


async def _run_search(message: Message, state: FSMContext):
    await message.bot.send_chat_action(message.chat.id, "typing")
    placeholder = await message.reply('🔎')
    text = message.text[:40]
    searched = await search(text, trans=db.get_trans(message.from_user.id))
    if searched[0] in NO_RESULT:
        await placeholder.edit_text(searched[0])
        return
    maked = await make(searched)
    await pager.show_first(placeholder, state, maked, len(searched))


@global_router.message(Searcher.search, F.text)
async def do_search(message: Message, state: FSMContext):
    await _run_search(message, state)


@global_router.edited_message(Searcher.search, F.text)
async def do_search_edited(message: Message, state: FSMContext):
    await _run_search(message, state)


@global_router.callback_query(Searcher.search, F.data.in_({"-1", "1"}))
async def paginate(call: CallbackQuery, state: FSMContext):
    await pager.paginate(call, state)
