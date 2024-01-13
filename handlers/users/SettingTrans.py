from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.settingsKeyboard import settingsKeyboard
from keyboards.default.forstartKeyboard import startKeyboard
from keyboards.default.tarjimalarKeyboard import tarjimalarKeyboard
from loader import dp, db


@dp.message_handler(Command("settings"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Sozlamalar", reply_markup=settingsKeyboard)
    await state.set_state("st")

@dp.message_handler(text = 'tarjima', state = 'st')
async def tarjima(msg:types.Message, state: FSMContext):
    matn = "O'zingizga kerakli tarjimani tanlang. Hozirgi holat "
    if db.select_user(id = msg.from_user.id)[4]:
        matn += 'Alovuddin Mansur'
    else:
        matn += 'Shayx Muhammad Sodiq Muhammad Yusuf'
    matn += ' tarjimalari'
    await msg.answer(matn, reply_markup=tarjimalarKeyboard)
    await state.set_state('trans')

@dp.message_handler(state="trans", text = 'Shayx Muhammad Sodiq Muhammad Yusuf')
async def enter_trans(message: types.Message, state: FSMContext):
    email = message.text
    db.update_user_trans(trans=0, id=message.from_user.id)
    user = db.select_user(id=message.from_user.id)
    await message.answer(f"Sozlamalar saqlandi", reply_markup=startKeyboard)
    await state.finish()
@dp.message_handler(state="trans", text = 'Alovuddin Mansur')
async def trans_second(message: types.Message, state: FSMContext):
    email = message.text
    db.update_user_trans(trans=1, id=message.from_user.id)
    user = db.select_user(id=message.from_user.id)
    await message.answer(f"Sozlamalar saqlandi", reply_markup=startKeyboard)
    await state.finish()