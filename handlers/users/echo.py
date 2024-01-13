from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from keyboards.default.forstartKeyboard import startKeyboard
from filters.group_chat import IsGroup
from filters.private_chat import IsPrivate

@dp.message_handler(IsPrivate(),state='*')
async def bot_echo(message: types.Message):
    await message.reply('Iltimos botdan foydalanish uchun tugma va buyruqlardan foydalaning')
