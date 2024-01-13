
from states.adminState import AdminState
from aiogram.types import ContentType
from loader import bot
import asyncio
from keyboards.default.forstartKeyboard import startKeyboard
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard, mainAndbackKeyboard
from keyboards.default.adminkeyboards import Adminkeyboard
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from loader import dp, db, bot
from aiogram.types import InputFile
@dp.message_handler(text="/admin", user_id=ADMINS, state = '*')
async def parol(message: types.Message, state: FSMContext):
    await message.answer("parolni kiriting", reply_markup=mainMenuKeyboard)
    await state.set_state('parol')



@dp.message_handler(text="rtwgjmja", user_id=ADMINS, state = 'parol')
async def admin(message: types.Message):
    await message.delete()
    await message.answer("Admin panel\n\nAdmin komandalar\n/allusers - bazadagi obunachilar soni, txt va db fayllari\n/checkusers - botdagi faol va o'chirilgan akkauntlar sonini aniqlash\n/reklama - reklama tarqatish, sekundiga 20 ta reklama\ncleandb - bazani tozalash", reply_markup=Adminkeyboard)
    await AdminState.admin.set()

@dp.message_handler(user_id=ADMINS, state = 'parol')
async def FalsePassword(message: types.Message):
    # await bot. #(text = "parol nato'g'ri")

    a = await message.answer("parol nato'g'ri")
    await asyncio.sleep(2)
    await message.delete()
    await a.delete()



@dp.message_handler(text=["Allusers", '/allusers'], state=AdminState.admin)
async def allusers(message: types.Message):
    users = db.select_all_users()
    await message.answer(f"Bazada {len(users)} ta foydalanuvchi bor.")
    with open('users.txt', 'w',encoding="utf-8") as file:
        file.write(str(users))
    await message.answer_document(InputFile('users.txt'))
    await message.answer_document(InputFile(path_or_bytesio='data/main.db'))
    # await message.answer(users)

@dp.message_handler(text=["Check users", '/checkusers'], state=AdminState.admin)
async def checkusers(message: types.Message):
    await message.answer("Tekshirish boshlandi")
    users = db.select_all_users()
    sended = 0
    unsended = 0
    for user in users:
        userid = user[0]
        try:
            await bot.send_chat_action(chat_id = userid, action="typing")
            sended +=1
            await asyncio.sleep(0.05)
        except Exception as err:
            unsended +=1
            print(err)
        
    
    await message.answer(f"{sended} ta foydalanuvchi aktiv. {unsended} ta foydalanuvchi o'chirilgan.")
@dp.message_handler(text=["/reklama", "Reklama"], user_id=ADMINS, state = AdminState.admin)
async def send_ad_to_all(message: types.Message, state = FSMContext):
    await message.answer('reklama yuboring', reply_markup=mainMenuKeyboard)

    await state.set_state('reklama')
@dp.message_handler(state = 'reklama', content_types=ContentType.ANY)
async def send_ad(message: types.Message, state = FSMContext):
    users = db.select_all_users()
    sended = 0
    unsended = 0
    for user in users:
        userid = user[0]
        try:
            await message.send_copy(chat_id = userid)
            sended +=1
            await asyncio.sleep(0.05)
        except Exception as err:
            unsended +=1
            # await bot.send_message(chat_id = ADMINS[0], text = f"{err}")
            print(err)
    await message.answer(f"reklama {sended} ta odamga yuborildi, {unsended} ta odamga yuborib bo'lmadi", reply_markup=Adminkeyboard)
    await AdminState.admin.set()

@dp.message_handler(text="/cleandb", user_id=ADMINS, state=AdminState.admin)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
