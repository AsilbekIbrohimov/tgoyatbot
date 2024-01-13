from qurandict import qurandict

# a = """#€
# @dp.message_handler(Text(startswith = '€', ignore_case=True), state = holat.suralar)
# async def b€(msg: types.Message, state: FSMContext):
# await msg.answer('1 dan $ gacha raqam kiriting', reply_markup=Home)
# await holat.a€.set()
# @dp.message_handler(state = holat.a€)
# async def a€(msg: types.Message, state:FSMContext):
# raqam = €
# soni = $
# if msg.text == '⬅️ Orqaga':
# await msg.answer("o'zingizga kerakli surani tanlang", reply_markup=Sura1)
# await holat.suralar.set()
# elif msg.text.isdigit():
# if int(msg.text)<1 or int(msg.text)> soni:
# await msg.answer(f"1 dan {soni} gacha raqam kiriting")
# else:
# await msg.answer(f"{qurandict[str(raqam)][int(msg.text)-1]['text']}")
# else:
# await msg.answer('raqam kiriting')"""
# @dp.message_handler(content_types=types.ContentType.ANY, state = 'feedback', user_id = ADMINS)
# async def feeedbek(message: types.Message, state: FSMContext):
#     if message.text == '🔝 Asosiy Menyu':
#         await bot_start(message, state)
#     else:
#         try:
#             # await bot.send_message(chat_id=message.reply_to_message.forward_from.id, text = f"Admin sizning xabaringizga javob qaytardi\n\n{message.reply_to_message.text}")
#             for Admin in ADMINS:
#                 await bot.send_message(chat_id=Admin, text = f"{message.from_user.full_name} sizning xabaringizga javob qaytardi\n\n{message.reply_to_message.text}")
#                 get_id  = await message.forward(Admin)
#                 db2.add_message(message_id=get_id.message_id, user_id = message.from_user.id)
#         except:
#             for Admin in ADMINS:
#                 await bot.send_message(chat_id=Admin, text = f" {message.from_user.get_mention(as_html=True)} xabar yubordi")
#                 get_id  = await message.forward(Admin)
#                 db2.add_message(message_id=get_id.message_id, user_id = message.from_user.id)
#         finally:
#             await message.reply("xabaringiz yuborildi", reply_markup=startKeyboard)
            
#     await state.finish()

# # msg.reply_to_message.from_user.id ==5268428809  and
# @dp.message_handler(lambda msg: (msg.reply_to_message.forward_from or msg.reply_to_message.forward_sender_name),user_id = ADMINS, content_types=types.ContentType.ANY, state = 'feedback')
# async def echo(message: types.Message):
#     try:
#         if message.reply_to_message.text:
#             text = message.reply_to_message.text
#         else:
#             text = message.reply_to_message.content_type
#         await bot.send_message(chat_id=db2.select_message(message_id = message.reply_to_message.message_id)[1], text = f"Admin savolingizga javob qaytardi\n\n{text}")
#         await bot.copy_message(chat_id=db2.select_message(message_id = message.reply_to_message.message_id)[1], from_chat_id=message.chat.id, message_id=message.message_id)
        
#         await message.reply("xabaringiz yuborildi")
#     except (BotKicked, BotBlocked, UserDeactivated):
#         await message.answer("Foydalanuvchi bloklangan")

# @dp.message_handler(content_types=types.ContentType.ANY, state = 'feedback')
# async def fedbek(message: types.Message, state: FSMContext):
#     if message.text == '🔝 Asosiy Menyu':
#         await bot_start(message, state)
#     else:
#         try:
#             # await bot.send_message(chat_id=message.reply_to_message.forward_from.id, text = f"Admin sizning xabaringizga javob qaytardi\n\n{message.reply_to_message.text}")
#             for Admin in ADMINS:
#                 await bot.send_message(chat_id=Admin, text = f"{message.from_user.full_name} sizning xabaringizga javob qaytardi\n\n{message.reply_to_message.text}")
#                 get_id  = await message.forward(Admin)
#                 db2.add_message(message_id=get_id.message_id, user_id = message.from_user.id)
#         except:
#             for Admin in ADMINS:
#                 await bot.send_message(chat_id=Admin, text = f" {message.from_user.get_mention(as_html=True)} xabar yubordi")
#                 get_id  = await message.forward(Admin)
#                 db2.add_message(message_id=get_id.message_id, user_id = message.from_user.id)
#         finally:
#             await message.reply("xabaringiz yuborildi", reply_markup=startKeyboard)
            
#     await state.finish()


# from loader import bot
# from cgitb import text
# from aiogram.utils.exceptions import BotKicked, BotBlocked, UserDeactivated
# from loader import dp
# from states.state import SetReport
# from aiogram.types import ContentType
# from aiogram import types
# from data.messages import *
# from keyboards.default.ButtonKeyboards import BACK_BUTTON
# from .start import cmd_start
# from aiogram.dispatcher import FSMContext
# from loader import db

a = """#€
@dp.message_handler(Text(startswith = '€', ignore_case=True), state = holat.suralar)
async def e€(msg: types.Message, state: FSMContext):
    raqam = €
    soni = $
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz.\nShu suradan qidirish uchun matn kiritng.", reply_markup=Home)
    await holat.b€.set()

@dp.message_handler(state = holat.a€)
async def a€(msg: types.Message, state:FSMContext):
    raqam = €
    soni = $
    await foroyat(msg, soni, raqam)
"""

res = ''
for i in range(1, 115):
    c = a.replace('€', str(i))
    d = c.replace('$', str(len(qurandict[str(i)])))+'\n\n'
    res+=d

with open('forOyat.txt', 'w',encoding="utf-8") as file:
    file.write(res)
print('yozildi')


# print(suralist[45-1])

# b = """@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[£].lower()) > 80, state = holat.suralar)
# async def d€(msg: types.Message):
#     raqam = €
#     soni = $
#     await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=Home)
#     await holat.b€.set()"""


# res = ''
# for i in range(1, 115):
#     res += b.replace('€', str(i)).replace('$', str(len(qurandict[str(i)]))).replace('£', str(i-1))+'\n\n'

# with open('inoyatsearch.py', 'w',encoding="utf-8") as file:
#     file.write(res)
# print('yozildi')
