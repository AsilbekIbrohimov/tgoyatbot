from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp,bot
from keyboards.default.suralistKeyboard import suraKeyboard1, suraKeyboard2
from aiogram.types import ContentType
from states.searcherState import AyahSearch as holat
from keyboards.default.mainMenuKeyboard import mainAndbackKeyboard
from keyboards.default.forstartKeyboard import startKeyboard
from data.qurandict import qurandict
from aiogram.dispatcher.filters import Text


@dp.message_handler(text = 'keyingi ➡️', state = holat.suralar)
async def sura2(msg: types.Message, state: FSMContext):
    await msg.answer("O\'zingizga kerakli surani kiriting", reply_markup=suraKeyboard2)

@dp.message_handler(text = '⬅️ oldingi', state = holat.suralar)
async def sura(msg: types.Message, state: FSMContext):
    await msg.answer("O\'zingizga kerakli surani kiriting", reply_markup=suraKeyboard1)
