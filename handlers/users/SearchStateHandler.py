from aiogram import types
from loader import dp, db
from states.searcherState import Searcher
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard
from keyboards.default.forstartKeyboard import startKeyboard
from aiogram.dispatcher import FSMContext
from utils import search, make, islatin
from keyboards.inline.changePageKeyboard import pages
from aiogram.types import Message, CallbackQuery
from loader import bot
from aiogram.dispatcher.filters import Regexp
from data.suralist import suralist
from utils.get_link import get_link
from data.config import ADMINS

@dp.message_handler(commands=['search'], state='*')
async def search_handler(message: types.Message, state: FSMContext):
        await message.answer("Qidirish uchun matn kiriting", reply_markup=mainMenuKeyboard)
        await Searcher.search.set()


users = {}


@dp.message_handler(content_types='text', state = Searcher.search) 
async def izla(message: types.Message):
        await message.answer_chat_action('typing')
        a = await message.reply('🔎')
        if len(message.text) > 40:
            message.text = message.text[:40]
        searched = await search(message.text, trans = db.select_user(id = message.from_user.id)[4])
        if 'қидирув натижаси мавжуд эмас' in searched or 'qidiruv natijasi mavjud emas' in searched:
            await message.answer(searched[0])
        else:
            maked = await make(searched)
            users[str(message.from_user.id)] = {'last_page': 0,
            'messageText': message.text, 'result': maked, 'lensearched': len(searched), 'lenmaked': len(maked)}
            user = users[str(message.from_user.id)]
            

            await bot.edit_message_text(f"Natijalar 1-sahifa {user['lenmaked']} dan. {user['lensearched']} ta oyat\n\n"+user['result'][0], message_id=a.message_id,chat_id = message.chat.id,reply_markup=pages)


@dp.edited_message_handler(state = Searcher.search) 
async def look_for(message: types.Message):        
        a = await message.reply('🔎')
        if len(message.text) > 40:
            message.text = message.text[:40]
        searched = await search(message.text)
        if 'қидирув натижаси мавжуд эмас' in searched or 'qidiruv natijasi mavjud emas' in searched:
            await message.answer(searched[0])
        else:
            maked = await make(searched)
            users[str(message.from_user.id)] = {'last_page': 0,
            'messageText': message.text,
            'result': maked,
            'lensearched': len(searched),
            'lenmaked': len(maked)}
            user = users[str(message.from_user.id)]
            await bot.edit_message_text(f"Natijalar 1-sahifa {user['lenmaked']} dan. {user['lensearched']} ta oyat\n\n"+user['result'][0], message_id=a.message_id,chat_id = message.chat.id,reply_markup=pages)



@dp.callback_query_handler(text="delete", state = '*')
async def ourses(call: CallbackQuery):
    await call.message.delete()

@dp.callback_query_handler(text = ("-1", "1"), state = Searcher.search)
async def bu(call: CallbackQuery):
    data = call.data
    user = users[str(call.from_user.id)]
    user['last_page'] = user['last_page']+int(data)
    if user["last_page"] < 0:
        user["last_page"] = 0
    if user['last_page'] == user['lenmaked']:
        user['last_page'] = user['lenmaked'] - 1
    await bot.edit_message_text(text = f"Natijalar {user['last_page']+1}-sahifa {user['lenmaked']} dan {user['lensearched']} ta oyat\n\n"+str(user['result'][user["last_page"]]), message_id = call.message.message_id, chat_id = call.message.chat.id, reply_markup=pages)
