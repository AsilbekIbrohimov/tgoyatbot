from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import db
from states.searcherState import Searcher
from utils.i18n import t, back_main_kb
from utils.searcher import search, make
from . import pager

global_router = Router()
NO_RESULT = ('қидирув натижаси мавжуд эмас', 'qidiruv natijasi mavjud emas')


@global_router.message(Command("search"), StateFilter("*"))
async def search_cmd(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    await message.answer(t('m_search_prompt', lang), reply_markup=back_main_kb(lang))
    await state.set_state(Searcher.search)


async def _run(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    await message.bot.send_chat_action(message.chat.id, "typing")
    placeholder = await message.reply('🔎')
    searched = await search(message.text[:40], trans=db.get_trans(message.from_user.id))
    if searched[0] in NO_RESULT:
        await placeholder.edit_text(t('m_no_result', lang))
        return
    maked = await make(searched)
    await pager.show_first(placeholder, state, maked, len(searched), lang)


@global_router.message(Searcher.search, F.text)
async def do_search(message: Message, state: FSMContext):
    await _run(message, state)


@global_router.edited_message(Searcher.search, F.text)
async def do_search_edited(message: Message, state: FSMContext):
    await _run(message, state)


@global_router.callback_query(Searcher.search, F.data.in_({"-1", "1"}))
async def paginate(call: CallbackQuery, state: FSMContext):
    await pager.paginate(call, state, db.get_ui_lang(call.from_user.id))
