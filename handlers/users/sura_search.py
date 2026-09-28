from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import db
from states.searcherState import SuraSearch
from data.suralist import suralist
from utils.searcher import make
from utils.searcher2 import search2
from utils.i18n import t, Btn, read_kb, sura_kb, sura_kb_for
from .common import ayah_count, resolve_sura
from . import pager

sura_search_router = Router()
NO_RESULT = ('қидирув натижаси мавжуд эмас', 'qidiruv natijasi mavjud emas')


@sura_search_router.message(SuraSearch.choose_sura, Btn('b_next'))
async def next_page(message: Message):
    await message.answer("→", reply_markup=sura_kb(2, db.get_ui_lang(message.from_user.id)))


@sura_search_router.message(SuraSearch.choose_sura, Btn('b_prev'))
async def prev_page(message: Message):
    await message.answer("←", reply_markup=sura_kb(1, db.get_ui_lang(message.from_user.id)))


@sura_search_router.message(SuraSearch.choose_sura, F.text)
async def choose_sura(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    sura = resolve_sura(message.text)
    if not sura:
        await message.answer(t('m_sura_not_found', lang))
        return
    await state.update_data(sura=sura, soni=ayah_count(sura))
    await state.set_state(SuraSearch.searching)
    await message.answer(t('m_search_prompt', lang), reply_markup=read_kb(lang))


@sura_search_router.message(SuraSearch.searching, Btn('b_back'))
async def back_to_choose(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    data = await state.get_data()
    await state.set_state(SuraSearch.choose_sura)
    await message.answer(t('m_choose_sura', lang), reply_markup=sura_kb_for(data.get("sura", 1), lang))


@sura_search_router.message(SuraSearch.searching, F.text)
async def do_search(message: Message, state: FSMContext):
    lang = db.get_ui_lang(message.from_user.id)
    data = await state.get_data()
    sura = data.get("sura")
    if not sura:
        await state.set_state(SuraSearch.choose_sura)
        await message.answer(t('m_choose_sura', lang))
        return
    await message.bot.send_chat_action(message.chat.id, "typing")
    placeholder = await message.reply('🔎')
    searched = await search2(sura, message.text[:40], trans=db.get_trans(message.from_user.id))
    if searched[0] in NO_RESULT:
        await placeholder.edit_text(t('m_no_result', lang))
        return
    maked = await make(searched)
    await pager.show_first(placeholder, state, maked, len(searched), lang)


@sura_search_router.callback_query(SuraSearch.searching, F.data.in_({"-1", "1"}))
async def paginate(call: CallbackQuery, state: FSMContext):
    await pager.paginate(call, state, db.get_ui_lang(call.from_user.id))
