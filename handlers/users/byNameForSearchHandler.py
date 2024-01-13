        # await msg.answer_chat_action('typing')
        # a = await msg.reply('🔎')
        # if len(msg.text) > 40:
        #     msg.text = msg.text[:40]
        # searched = await search2(raqam, msg.text)
        # if 'қидирув натижаси мавжуд эмас' in searched or 'qidiruv natijasi mavjud emas' in searched:
        #     await msg.answer(searched[0])
        # else:
        #     maked = await make(searched)
        #     users2[str(msg.from_user.id)] = {'last_page': 0,
        #     'msgText': msg.text, 'result': maked, 'lensearched': len(searched), 'lenmaked': len(maked)}
        #     user = users2[str(msg.from_user.id)]
        #     await bot.edit_message_text(f"Natijalar 1-sahifa {user['lenmaked']} dan. {user['lensearched']} ta oyat\n\n"+user['result'][0], message_id=a.message_id,chat_id = msg.chat.id,reply_markup=pages)
# @dp.callback_query_handler(text = ("-1", "1"), state = holat)
# async def bu(call: CallbackQuery):
#     data = call.data
#     user = users2[str(call.from_user.id)]
#     user['last_page'] = user['last_page']+int(data)
#     # users[str(call.from_user.id)] = {"last_page":users[str(call.from_user.id)]["last_page"]+int(data), 'messageText': users[str(call.from_user.id)]['messageText']}
#     if user["last_page"] < 0:
#         user["last_page"] = 0
#     if user['last_page'] == user['lenmaked']:
#         user['last_page'] = user['lenmaked'] - 1
#     await bot.edit_message_text(text = f"Natijalar {user['last_page']+1}-sahifa {user['lenmaked']} dan {user['lensearched']} ta oyat\n\n"+str(user['result'][user["last_page"]]), message_id = call.message.message_id, chat_id = call.message.chat.id, reply_markup=pages)


from fuzzywuzzy import fuzz
from aiogram import types
from states.searcherState import oyatdanIzlash as holat
from aiogram.dispatcher import FSMContext
from loader import dp,bot
from keyboards.default.suralistKeyboard import suraKeyboard1, suraKeyboard2
from aiogram.types import ContentType, CallbackQuery
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard, mainAndbackKeyboard
from keyboards.default.forstartKeyboard import startKeyboard
from data.qurandict import qurandict
from data.qurandict2 import qurandict2
from utils.get_link import get_link
from aiogram.dispatcher.filters import Text
from data.suralist import suralist
from keyboards.inline.changePageKeyboard import pages

users2 = {}

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[0].lower()) > 80, state = holat.suralar)
async def d1(msg: types.Message):
    raqam = 1
    soni = 7
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b1.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[1].lower()) > 80, state = holat.suralar)
async def d2(msg: types.Message):
    raqam = 2
    soni = 286
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b2.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[2].lower()) > 80, state = holat.suralar)
async def d3(msg: types.Message):
    raqam = 3
    soni = 200
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b3.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[3].lower()) > 80, state = holat.suralar)
async def d4(msg: types.Message):
    raqam = 4
    soni = 176
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b4.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[4].lower()) > 80, state = holat.suralar)
async def d5(msg: types.Message):
    raqam = 5
    soni = 120
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b5.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[5].lower()) > 80, state = holat.suralar)
async def d6(msg: types.Message):
    raqam = 6
    soni = 165
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b6.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[6].lower()) > 80, state = holat.suralar)
async def d7(msg: types.Message):
    raqam = 7
    soni = 206
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b7.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[7].lower()) > 80, state = holat.suralar)
async def d8(msg: types.Message):
    raqam = 8
    soni = 75
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b8.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[8].lower()) > 80, state = holat.suralar)
async def d9(msg: types.Message):
    raqam = 9
    soni = 129
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b9.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[9].lower()) > 80, state = holat.suralar)
async def d10(msg: types.Message):
    raqam = 10
    soni = 109
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b10.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[10].lower()) > 80, state = holat.suralar)
async def d11(msg: types.Message):
    raqam = 11
    soni = 123
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b11.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[11].lower()) > 80, state = holat.suralar)
async def d12(msg: types.Message):
    raqam = 12
    soni = 111
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b12.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[12].lower()) > 80, state = holat.suralar)
async def d13(msg: types.Message):
    raqam = 13
    soni = 43
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b13.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[13].lower()) > 80, state = holat.suralar)
async def d14(msg: types.Message):
    raqam = 14
    soni = 52
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b14.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[14].lower()) > 80, state = holat.suralar)
async def d15(msg: types.Message):
    raqam = 15
    soni = 99
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b15.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[15].lower()) > 80, state = holat.suralar)
async def d16(msg: types.Message):
    raqam = 16
    soni = 128
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b16.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[16].lower()) > 80, state = holat.suralar)
async def d17(msg: types.Message):
    raqam = 17
    soni = 111
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b17.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[17].lower()) > 80, state = holat.suralar)
async def d18(msg: types.Message):
    raqam = 18
    soni = 110
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b18.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[18].lower()) > 80, state = holat.suralar)
async def d19(msg: types.Message):
    raqam = 19
    soni = 98
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b19.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[19].lower()) > 80, state = holat.suralar)
async def d20(msg: types.Message):
    raqam = 20
    soni = 135
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b20.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[20].lower()) > 80, state = holat.suralar)
async def d21(msg: types.Message):
    raqam = 21
    soni = 112
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b21.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[21].lower()) > 80, state = holat.suralar)
async def d22(msg: types.Message):
    raqam = 22
    soni = 78
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b22.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[22].lower()) > 80, state = holat.suralar)
async def d23(msg: types.Message):
    raqam = 23
    soni = 118
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b23.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[23].lower()) > 80, state = holat.suralar)
async def d24(msg: types.Message):
    raqam = 24
    soni = 64
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b24.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[24].lower()) > 80, state = holat.suralar)
async def d25(msg: types.Message):
    raqam = 25
    soni = 77
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b25.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[25].lower()) > 80, state = holat.suralar)
async def d26(msg: types.Message):
    raqam = 26
    soni = 227
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b26.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[26].lower()) > 80, state = holat.suralar)
async def d27(msg: types.Message):
    raqam = 27
    soni = 93
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b27.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[27].lower()) > 80, state = holat.suralar)
async def d28(msg: types.Message):
    raqam = 28
    soni = 88
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b28.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[28].lower()) > 80, state = holat.suralar)
async def d29(msg: types.Message):
    raqam = 29
    soni = 69
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b29.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[29].lower()) > 80, state = holat.suralar)
async def d30(msg: types.Message):
    raqam = 30
    soni = 60
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b30.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[30].lower()) > 80, state = holat.suralar)
async def d31(msg: types.Message):
    raqam = 31
    soni = 34
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b31.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[31].lower()) > 80, state = holat.suralar)
async def d32(msg: types.Message):
    raqam = 32
    soni = 30
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b32.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[32].lower()) > 80, state = holat.suralar)
async def d33(msg: types.Message):
    raqam = 33
    soni = 73
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b33.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[33].lower()) > 80, state = holat.suralar)
async def d34(msg: types.Message):
    raqam = 34
    soni = 54
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b34.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[34].lower()) > 80, state = holat.suralar)
async def d35(msg: types.Message):
    raqam = 35
    soni = 45
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b35.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[35].lower()) > 80, state = holat.suralar)
async def d36(msg: types.Message):
    raqam = 36
    soni = 83
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b36.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[36].lower()) > 80, state = holat.suralar)
async def d37(msg: types.Message):
    raqam = 37
    soni = 182
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b37.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[37].lower()) > 80, state = holat.suralar)
async def d38(msg: types.Message):
    raqam = 38
    soni = 88
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b38.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[38].lower()) > 80, state = holat.suralar)
async def d39(msg: types.Message):
    raqam = 39
    soni = 75
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b39.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[39].lower()) > 80, state = holat.suralar)
async def d40(msg: types.Message):
    raqam = 40
    soni = 85
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b40.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[40].lower()) > 80, state = holat.suralar)
async def d41(msg: types.Message):
    raqam = 41
    soni = 54
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b41.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[41].lower()) > 80, state = holat.suralar)
async def d42(msg: types.Message):
    raqam = 42
    soni = 53
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b42.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[42].lower()) > 80, state = holat.suralar)
async def d43(msg: types.Message):
    raqam = 43
    soni = 89
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b43.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[43].lower()) > 80, state = holat.suralar)
async def d44(msg: types.Message):
    raqam = 44
    soni = 59
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b44.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[44].lower()) > 80, state = holat.suralar)
async def d45(msg: types.Message):
    raqam = 45
    soni = 37
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b45.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[45].lower()) > 80, state = holat.suralar)
async def d46(msg: types.Message):
    raqam = 46
    soni = 35
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b46.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[46].lower()) > 80, state = holat.suralar)
async def d47(msg: types.Message):
    raqam = 47
    soni = 38
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b47.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[47].lower()) > 80, state = holat.suralar)
async def d48(msg: types.Message):
    raqam = 48
    soni = 29
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b48.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[48].lower()) > 80, state = holat.suralar)
async def d49(msg: types.Message):
    raqam = 49
    soni = 18
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b49.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[49].lower()) > 80, state = holat.suralar)
async def d50(msg: types.Message):
    raqam = 50
    soni = 45
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b50.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[50].lower()) > 80, state = holat.suralar)
async def d51(msg: types.Message):
    raqam = 51
    soni = 60
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b51.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[51].lower()) > 80, state = holat.suralar)
async def d52(msg: types.Message):
    raqam = 52
    soni = 49
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b52.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[52].lower()) > 80, state = holat.suralar)
async def d53(msg: types.Message):
    raqam = 53
    soni = 62
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b53.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[53].lower()) > 80, state = holat.suralar)
async def d54(msg: types.Message):
    raqam = 54
    soni = 55
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b54.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[54].lower()) > 80, state = holat.suralar)
async def d55(msg: types.Message):
    raqam = 55
    soni = 78
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b55.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[55].lower()) > 80, state = holat.suralar)
async def d56(msg: types.Message):
    raqam = 56
    soni = 96
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b56.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[56].lower()) > 80, state = holat.suralar)
async def d57(msg: types.Message):
    raqam = 57
    soni = 29
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b57.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[57].lower()) > 80, state = holat.suralar)
async def d58(msg: types.Message):
    raqam = 58
    soni = 22
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b58.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[58].lower()) > 80, state = holat.suralar)
async def d59(msg: types.Message):
    raqam = 59
    soni = 24
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b59.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[59].lower()) > 80, state = holat.suralar)
async def d60(msg: types.Message):
    raqam = 60
    soni = 13
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b60.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[60].lower()) > 80, state = holat.suralar)
async def d61(msg: types.Message):
    raqam = 61
    soni = 14
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b61.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[61].lower()) > 80, state = holat.suralar)
async def d62(msg: types.Message):
    raqam = 62
    soni = 11
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b62.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[62].lower()) > 80, state = holat.suralar)
async def d63(msg: types.Message):
    raqam = 63
    soni = 11
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b63.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[63].lower()) > 80, state = holat.suralar)
async def d64(msg: types.Message):
    raqam = 64
    soni = 18
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b64.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[64].lower()) > 80, state = holat.suralar)
async def d65(msg: types.Message):
    raqam = 65
    soni = 12
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b65.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[65].lower()) > 80, state = holat.suralar)
async def d66(msg: types.Message):
    raqam = 66
    soni = 12
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b66.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[66].lower()) > 80, state = holat.suralar)
async def d67(msg: types.Message):
    raqam = 67
    soni = 30
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b67.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[67].lower()) > 80, state = holat.suralar)
async def d68(msg: types.Message):
    raqam = 68
    soni = 52
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b68.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[68].lower()) > 80, state = holat.suralar)
async def d69(msg: types.Message):
    raqam = 69
    soni = 52
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b69.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[69].lower()) > 80, state = holat.suralar)
async def d70(msg: types.Message):
    raqam = 70
    soni = 44
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b70.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[70].lower()) > 80, state = holat.suralar)
async def d71(msg: types.Message):
    raqam = 71
    soni = 28
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b71.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[71].lower()) > 80, state = holat.suralar)
async def d72(msg: types.Message):
    raqam = 72
    soni = 28
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b72.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[72].lower()) > 80, state = holat.suralar)
async def d73(msg: types.Message):
    raqam = 73
    soni = 20
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b73.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[73].lower()) > 80, state = holat.suralar)
async def d74(msg: types.Message):
    raqam = 74
    soni = 56
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b74.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[74].lower()) > 80, state = holat.suralar)
async def d75(msg: types.Message):
    raqam = 75
    soni = 40
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b75.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[75].lower()) > 80, state = holat.suralar)
async def d76(msg: types.Message):
    raqam = 76
    soni = 31
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b76.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[76].lower()) > 80, state = holat.suralar)
async def d77(msg: types.Message):
    raqam = 77
    soni = 50
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b77.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[77].lower()) > 80, state = holat.suralar)
async def d78(msg: types.Message):
    raqam = 78
    soni = 40
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b78.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[78].lower()) > 80, state = holat.suralar)
async def d79(msg: types.Message):
    raqam = 79
    soni = 46
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b79.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[79].lower()) > 80, state = holat.suralar)
async def d80(msg: types.Message):
    raqam = 80
    soni = 42
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b80.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[80].lower()) > 80, state = holat.suralar)
async def d81(msg: types.Message):
    raqam = 81
    soni = 29
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b81.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[81].lower()) > 80, state = holat.suralar)
async def d82(msg: types.Message):
    raqam = 82
    soni = 19
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b82.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[82].lower()) > 80, state = holat.suralar)
async def d83(msg: types.Message):
    raqam = 83
    soni = 36
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b83.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[83].lower()) > 80, state = holat.suralar)
async def d84(msg: types.Message):
    raqam = 84
    soni = 25
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b84.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[84].lower()) > 80, state = holat.suralar)
async def d85(msg: types.Message):
    raqam = 85
    soni = 22
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b85.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[85].lower()) > 80, state = holat.suralar)
async def d86(msg: types.Message):
    raqam = 86
    soni = 17
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b86.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[86].lower()) > 80, state = holat.suralar)
async def d87(msg: types.Message):
    raqam = 87
    soni = 19
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b87.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[87].lower()) > 80, state = holat.suralar)
async def d88(msg: types.Message):
    raqam = 88
    soni = 26
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b88.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[88].lower()) > 80, state = holat.suralar)
async def d89(msg: types.Message):
    raqam = 89
    soni = 30
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b89.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[89].lower()) > 80, state = holat.suralar)
async def d90(msg: types.Message):
    raqam = 90
    soni = 20
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b90.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[90].lower()) > 80, state = holat.suralar)
async def d91(msg: types.Message):
    raqam = 91
    soni = 15
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b91.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[91].lower()) > 80, state = holat.suralar)
async def d92(msg: types.Message):
    raqam = 92
    soni = 21
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b92.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[92].lower()) > 80, state = holat.suralar)
async def d93(msg: types.Message):
    raqam = 93
    soni = 11
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b93.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[93].lower()) > 80, state = holat.suralar)
async def d94(msg: types.Message):
    raqam = 94
    soni = 8
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b94.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[94].lower()) > 80, state = holat.suralar)
async def d95(msg: types.Message):
    raqam = 95
    soni = 8
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b95.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[95].lower()) > 80, state = holat.suralar)
async def d96(msg: types.Message):
    raqam = 96
    soni = 19
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b96.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[96].lower()) > 80, state = holat.suralar)
async def d97(msg: types.Message):
    raqam = 97
    soni = 5
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b97.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[97].lower()) > 80, state = holat.suralar)
async def d98(msg: types.Message):
    raqam = 98
    soni = 8
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b98.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[98].lower()) > 80, state = holat.suralar)
async def d99(msg: types.Message):
    raqam = 99
    soni = 8
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b99.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[99].lower()) > 80, state = holat.suralar)
async def d100(msg: types.Message):
    raqam = 100
    soni = 11
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b100.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[100].lower()) > 80, state = holat.suralar)
async def d101(msg: types.Message):
    raqam = 101
    soni = 11
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b101.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[101].lower()) > 80, state = holat.suralar)
async def d102(msg: types.Message):
    raqam = 102
    soni = 8
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b102.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[102].lower()) > 80, state = holat.suralar)
async def d103(msg: types.Message):
    raqam = 103
    soni = 3
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b103.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[103].lower()) > 80, state = holat.suralar)
async def d104(msg: types.Message):
    raqam = 104
    soni = 9
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b104.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[104].lower()) > 80, state = holat.suralar)
async def d105(msg: types.Message):
    raqam = 105
    soni = 5
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b105.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[105].lower()) > 80, state = holat.suralar)
async def d106(msg: types.Message):
    raqam = 106
    soni = 4
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b106.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[106].lower()) > 80, state = holat.suralar)
async def d107(msg: types.Message):
    raqam = 107
    soni = 7
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b107.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[107].lower()) > 80, state = holat.suralar)
async def d108(msg: types.Message):
    raqam = 108
    soni = 3
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b108.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[108].lower()) > 80, state = holat.suralar)
async def d109(msg: types.Message):
    raqam = 109
    soni = 6
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b109.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[109].lower()) > 80, state = holat.suralar)
async def d110(msg: types.Message):
    raqam = 110
    soni = 3
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b110.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[110].lower()) > 80, state = holat.suralar)
async def d111(msg: types.Message):
    raqam = 111
    soni = 5
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b111.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[111].lower()) > 80, state = holat.suralar)
async def d112(msg: types.Message):
    raqam = 112
    soni = 4
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b112.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[112].lower()) > 80, state = holat.suralar)
async def d113(msg: types.Message):
    raqam = 113
    soni = 5
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b113.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[113].lower()) > 80, state = holat.suralar)
async def d114(msg: types.Message):
    raqam = 114
    soni = 6
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suraning ichidan qidirish uchun matn kiritng yoki ayni bir oyatni olish uchun 1 dan {soni} gacha raqamlardan birini kiriting", reply_markup=mainAndbackKeyboard)
    await holat.b114.set()

