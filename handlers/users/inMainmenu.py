from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.searcherState import Searcher, oyatdanIzlash
from states.searcherState import AyahSearch as holat
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard
from keyboards.default.suralistKeyboard import suraKeyboard1
from keyboards.default.settingsKeyboard import settingsKeyboard

@dp.message_handler(text = 'Umumiy izlash🔎')
async def Izlash(message: types.Message, state: FSMContext):
        await message.answer("Qidirish uchun matn kiriting.\nEtibor bering qidirish tizimi qur'onning arabcha matni va o'zbekcha tarjimasi matnidan izlaydi", reply_markup=mainMenuKeyboard)
        await Searcher.search.set()

@dp.message_handler(text = 'Oyatlar')
async def oyat(msg: types.Message, state: FSMContext):
    await holat.suralar.set()
    await msg.answer('Oʻzingizga kerakli suraning raqamini kiriting, nomini yozing yoki tugmalardan foydalaning', reply_markup=suraKeyboard1)

@dp.message_handler(text = "Sozlamalar")
async def settings(message: types.Message, state: FSMContext):
    await message.answer("Sozlamalar", reply_markup=settingsKeyboard)
    await state.set_state("st")

@dp.message_handler(text = 'Fikr bildirish✍️')
async def feedback(message: types.Message, state: FSMContext):
    await message.answer("Assalomu alaykum. Fikringizni yozib qoldiring. Adminga xabaringiz yuboriladi.", reply_markup=mainMenuKeyboard)
    await state.set_state('feedback')


@dp.message_handler(text = "Suradan izlash")
async def suradan_izlash(message: types.Message, state: FSMContext):
    await message.answer("O'zingizga kerakli surani tanlang.\nEtibor bering qidirish tizimi qur'onning arabcha matni va o'zbekcha tarjimasi matnidan izlaydi", reply_markup=suraKeyboard1)
    await oyatdanIzlash.suralar.set()
