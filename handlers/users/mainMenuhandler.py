from loader import dp
from aiogram.dispatcher import FSMContext
from .startHandler import bot_start
from aiogram import types

@dp.message_handler(text = '🔝 Asosiy Menyu', state = '*')
async def orqaga(message: types.Message, state: FSMContext):
    await state.finish()
    await bot_start(message, state)