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
from utils.searcher import make
from utils.searcher2 import search2
from aiogram.dispatcher.filters import Text
from data.suralist import suralist
from keyboards.inline.changePageKeyboard import pages
from loader import db
from .startHandler import bot_start
users2 = {}

async def foroyat(msg, soni, raqam, state):
    keyboard = None
    if raqam > 56:
        keyboard = suraKeyboard2
    else:
        keyboard = suraKeyboard1
    if msg.text == '⬅️ Orqaga':
        await msg.answer("o'zingizga kerakli surani tanlang", reply_markup=keyboard)
        await holat.suralar.set()
        return
    if msg.text == '🔝 Asosiy Menyu':
        await bot_start(msg, state)
        state.finish()
        return
    await msg.answer_chat_action('typing')
    a = await msg.reply('🔎')
    if len(msg.text) > 40:
        msg.text = msg.text[:40]
    searched = await search2(raqam, msg.text, trans = db.select_user(id = msg.from_user.id)[4])
    if 'қидирув натижаси мавжуд эмас' in searched or 'qidiruv natijasi mavjud emas' in searched:
        await msg.answer(searched[0])
    else:
        maked = await make(searched)
        users2[str(msg.from_user.id)] = {'last_page': 0,
        'msgText': msg.text, 'result': maked, 'lensearched': len(searched), 'lenmaked': len(maked)}
        user = users2[str(msg.from_user.id)]
        await bot.edit_message_text(f"Natijalar 1-sahifa {user['lenmaked']} dan. {user['lensearched']} ta oyat\n\n"+user['result'][0], message_id=a.message_id,chat_id = msg.chat.id,reply_markup=pages)

@dp.callback_query_handler(text = ("-1", "1"), state = holat)
async def bujljh(call: CallbackQuery):
    data = call.data
    user = users2[str(call.from_user.id)]
    user['last_page'] = user['last_page']+int(data)
    # users[str(call.from_user.id)] = {"last_page":users[str(call.from_user.id)]["last_page"]+int(data), 'messageText': users[str(call.from_user.id)]['messageText']}
    if user["last_page"] < 0:
        user["last_page"] = 0
    if user['last_page'] == user['lenmaked']:
        user['last_page'] = user['lenmaked'] - 1
    await bot.edit_message_text(text = f"Natijalar {user['last_page']+1}-sahifa {user['lenmaked']} dan {user['lensearched']} ta oyat\n\n"+str(user['result'][user["last_page"]]), message_id = call.message.message_id, chat_id = call.message.chat.id, reply_markup=pages)



@dp.message_handler(text = 'keyingi ➡️', state = holat.suralar)
async def sura2(msg: types.Message, state: FSMContext):
    await msg.answer("O\'zingizga kerakli surani kiriting", reply_markup=suraKeyboard2)


@dp.message_handler(text = '⬅️ oldingi', state = holat.suralar)
async def sura(msg: types.Message, state: FSMContext):
    await msg.answer("O\'zingizga kerakli surani kiriting", reply_markup=suraKeyboard1)

#12
@dp.message_handler(Text(startswith = '12', ignore_case=True), state = holat.suralar)
async def e12(msg: types.Message, state: FSMContext):
    raqam = 12
    soni = 111
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b12.set()

@dp.message_handler(state = holat.b12)
async def a12(msg: types.Message, state:FSMContext):
    raqam = 12
    soni = 111
    await foroyat(msg, soni, raqam, state)


#13
@dp.message_handler(Text(startswith = '13', ignore_case=True), state = holat.suralar)
async def e13(msg: types.Message, state: FSMContext):
    raqam = 13
    soni = 43
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b13.set()

@dp.message_handler(state = holat.b13)
async def a13(msg: types.Message, state:FSMContext):
    raqam = 13
    soni = 43
    await foroyat(msg, soni, raqam, state)


#14
@dp.message_handler(Text(startswith = '14', ignore_case=True), state = holat.suralar)
async def e14(msg: types.Message, state: FSMContext):
    raqam = 14
    soni = 52
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b14.set()

@dp.message_handler(state = holat.b14)
async def a14(msg: types.Message, state:FSMContext):
    raqam = 14
    soni = 52
    await foroyat(msg, soni, raqam, state)


#15
@dp.message_handler(Text(startswith = '15', ignore_case=True), state = holat.suralar)
async def e15(msg: types.Message, state: FSMContext):
    raqam = 15
    soni = 99
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b15.set()

@dp.message_handler(state = holat.b15)
async def a15(msg: types.Message, state:FSMContext):
    raqam = 15
    soni = 99
    await foroyat(msg, soni, raqam, state)


#16
@dp.message_handler(Text(startswith = '16', ignore_case=True), state = holat.suralar)
async def e16(msg: types.Message, state: FSMContext):
    raqam = 16
    soni = 128
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b16.set()

@dp.message_handler(state = holat.b16)
async def a16(msg: types.Message, state:FSMContext):
    raqam = 16
    soni = 128
    await foroyat(msg, soni, raqam, state)


#17
@dp.message_handler(Text(startswith = '17', ignore_case=True), state = holat.suralar)
async def e17(msg: types.Message, state: FSMContext):
    raqam = 17
    soni = 111
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b17.set()

@dp.message_handler(state = holat.b17)
async def a17(msg: types.Message, state:FSMContext):
    raqam = 17
    soni = 111
    await foroyat(msg, soni, raqam, state)


#18
@dp.message_handler(Text(startswith = '18', ignore_case=True), state = holat.suralar)
async def e18(msg: types.Message, state: FSMContext):
    raqam = 18
    soni = 110
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b18.set()

@dp.message_handler(state = holat.b18)
async def a18(msg: types.Message, state:FSMContext):
    raqam = 18
    soni = 110
    await foroyat(msg, soni, raqam, state)


#19
@dp.message_handler(Text(startswith = '19', ignore_case=True), state = holat.suralar)
async def e19(msg: types.Message, state: FSMContext):
    raqam = 19
    soni = 98
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b19.set()

@dp.message_handler(state = holat.b19)
async def a19(msg: types.Message, state:FSMContext):
    raqam = 19
    soni = 98
    await foroyat(msg, soni, raqam, state)


#20
@dp.message_handler(Text(startswith = '20', ignore_case=True), state = holat.suralar)
async def e20(msg: types.Message, state: FSMContext):
    raqam = 20
    soni = 135
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b20.set()

@dp.message_handler(state = holat.b20)
async def a20(msg: types.Message, state:FSMContext):
    raqam = 20
    soni = 135
    await foroyat(msg, soni, raqam, state)


#21
@dp.message_handler(Text(startswith = '21', ignore_case=True), state = holat.suralar)
async def e21(msg: types.Message, state: FSMContext):
    raqam = 21
    soni = 112
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b21.set()

@dp.message_handler(state = holat.b21)
async def a21(msg: types.Message, state:FSMContext):
    raqam = 21
    soni = 112
    await foroyat(msg, soni, raqam, state)


#22
@dp.message_handler(Text(startswith = '22', ignore_case=True), state = holat.suralar)
async def e22(msg: types.Message, state: FSMContext):
    raqam = 22
    soni = 78
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b22.set()

@dp.message_handler(state = holat.b22)
async def a22(msg: types.Message, state:FSMContext):
    raqam = 22
    soni = 78
    await foroyat(msg, soni, raqam, state)


#23
@dp.message_handler(Text(startswith = '23', ignore_case=True), state = holat.suralar)
async def e23(msg: types.Message, state: FSMContext):
    raqam = 23
    soni = 118
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b23.set()

@dp.message_handler(state = holat.b23)
async def a23(msg: types.Message, state:FSMContext):
    raqam = 23
    soni = 118
    await foroyat(msg, soni, raqam, state)


#24
@dp.message_handler(Text(startswith = '24', ignore_case=True), state = holat.suralar)
async def e24(msg: types.Message, state: FSMContext):
    raqam = 24
    soni = 64
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b24.set()

@dp.message_handler(state = holat.b24)
async def a24(msg: types.Message, state:FSMContext):
    raqam = 24
    soni = 64
    await foroyat(msg, soni, raqam, state)


#25
@dp.message_handler(Text(startswith = '25', ignore_case=True), state = holat.suralar)
async def e25(msg: types.Message, state: FSMContext):
    raqam = 25
    soni = 77
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b25.set()

@dp.message_handler(state = holat.b25)
async def a25(msg: types.Message, state:FSMContext):
    raqam = 25
    soni = 77
    await foroyat(msg, soni, raqam, state)


#26
@dp.message_handler(Text(startswith = '26', ignore_case=True), state = holat.suralar)
async def e26(msg: types.Message, state: FSMContext):
    raqam = 26
    soni = 227
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b26.set()

@dp.message_handler(state = holat.b26)
async def a26(msg: types.Message, state:FSMContext):
    raqam = 26
    soni = 227
    await foroyat(msg, soni, raqam, state)


#27
@dp.message_handler(Text(startswith = '27', ignore_case=True), state = holat.suralar)
async def e27(msg: types.Message, state: FSMContext):
    raqam = 27
    soni = 93
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b27.set()

@dp.message_handler(state = holat.b27)
async def a27(msg: types.Message, state:FSMContext):
    raqam = 27
    soni = 93
    await foroyat(msg, soni, raqam, state)


#28
@dp.message_handler(Text(startswith = '28', ignore_case=True), state = holat.suralar)
async def e28(msg: types.Message, state: FSMContext):
    raqam = 28
    soni = 88
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b28.set()

@dp.message_handler(state = holat.b28)
async def a28(msg: types.Message, state:FSMContext):
    raqam = 28
    soni = 88
    await foroyat(msg, soni, raqam, state)


#29
@dp.message_handler(Text(startswith = '29', ignore_case=True), state = holat.suralar)
async def e29(msg: types.Message, state: FSMContext):
    raqam = 29
    soni = 69
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b29.set()

@dp.message_handler(state = holat.b29)
async def a29(msg: types.Message, state:FSMContext):
    raqam = 29
    soni = 69
    await foroyat(msg, soni, raqam, state)


#30
@dp.message_handler(Text(startswith = '30', ignore_case=True), state = holat.suralar)
async def e30(msg: types.Message, state: FSMContext):
    raqam = 30
    soni = 60
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b30.set()

@dp.message_handler(state = holat.b30)
async def a30(msg: types.Message, state:FSMContext):
    raqam = 30
    soni = 60
    await foroyat(msg, soni, raqam, state)


#31
@dp.message_handler(Text(startswith = '31', ignore_case=True), state = holat.suralar)
async def e31(msg: types.Message, state: FSMContext):
    raqam = 31
    soni = 34
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b31.set()

@dp.message_handler(state = holat.b31)
async def a31(msg: types.Message, state:FSMContext):
    raqam = 31
    soni = 34
    await foroyat(msg, soni, raqam, state)


#32
@dp.message_handler(Text(startswith = '32', ignore_case=True), state = holat.suralar)
async def e32(msg: types.Message, state: FSMContext):
    raqam = 32
    soni = 30
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b32.set()

@dp.message_handler(state = holat.b32)
async def a32(msg: types.Message, state:FSMContext):
    raqam = 32
    soni = 30
    await foroyat(msg, soni, raqam, state)


#33
@dp.message_handler(Text(startswith = '33', ignore_case=True), state = holat.suralar)
async def e33(msg: types.Message, state: FSMContext):
    raqam = 33
    soni = 73
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b33.set()

@dp.message_handler(state = holat.b33)
async def a33(msg: types.Message, state:FSMContext):
    raqam = 33
    soni = 73
    await foroyat(msg, soni, raqam, state)


#34
@dp.message_handler(Text(startswith = '34', ignore_case=True), state = holat.suralar)
async def e34(msg: types.Message, state: FSMContext):
    raqam = 34
    soni = 54
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b34.set()

@dp.message_handler(state = holat.b34)
async def a34(msg: types.Message, state:FSMContext):
    raqam = 34
    soni = 54
    await foroyat(msg, soni, raqam, state)


#35
@dp.message_handler(Text(startswith = '35', ignore_case=True), state = holat.suralar)
async def e35(msg: types.Message, state: FSMContext):
    raqam = 35
    soni = 45
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b35.set()

@dp.message_handler(state = holat.b35)
async def a35(msg: types.Message, state:FSMContext):
    raqam = 35
    soni = 45
    await foroyat(msg, soni, raqam, state)


#36
@dp.message_handler(Text(startswith = '36', ignore_case=True), state = holat.suralar)
async def e36(msg: types.Message, state: FSMContext):
    raqam = 36
    soni = 83
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b36.set()

@dp.message_handler(state = holat.b36)
async def a36(msg: types.Message, state:FSMContext):
    raqam = 36
    soni = 83
    await foroyat(msg, soni, raqam, state)


#37
@dp.message_handler(Text(startswith = '37', ignore_case=True), state = holat.suralar)
async def e37(msg: types.Message, state: FSMContext):
    raqam = 37
    soni = 182
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b37.set()

@dp.message_handler(state = holat.b37)
async def a37(msg: types.Message, state:FSMContext):
    raqam = 37
    soni = 182
    await foroyat(msg, soni, raqam, state)


#38
@dp.message_handler(Text(startswith = '38', ignore_case=True), state = holat.suralar)
async def e38(msg: types.Message, state: FSMContext):
    raqam = 38
    soni = 88
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b38.set()

@dp.message_handler(state = holat.b38)
async def a38(msg: types.Message, state:FSMContext):
    raqam = 38
    soni = 88
    await foroyat(msg, soni, raqam, state)


#39
@dp.message_handler(Text(startswith = '39', ignore_case=True), state = holat.suralar)
async def e39(msg: types.Message, state: FSMContext):
    raqam = 39
    soni = 75
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b39.set()

@dp.message_handler(state = holat.b39)
async def a39(msg: types.Message, state:FSMContext):
    raqam = 39
    soni = 75
    await foroyat(msg, soni, raqam, state)


#40
@dp.message_handler(Text(startswith = '40', ignore_case=True), state = holat.suralar)
async def e40(msg: types.Message, state: FSMContext):
    raqam = 40
    soni = 85
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b40.set()

@dp.message_handler(state = holat.b40)
async def a40(msg: types.Message, state:FSMContext):
    raqam = 40
    soni = 85
    await foroyat(msg, soni, raqam, state)


#41
@dp.message_handler(Text(startswith = '41', ignore_case=True), state = holat.suralar)
async def e41(msg: types.Message, state: FSMContext):
    raqam = 41
    soni = 54
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b41.set()

@dp.message_handler(state = holat.b41)
async def a41(msg: types.Message, state:FSMContext):
    raqam = 41
    soni = 54
    await foroyat(msg, soni, raqam, state)


#42
@dp.message_handler(Text(startswith = '42', ignore_case=True), state = holat.suralar)
async def e42(msg: types.Message, state: FSMContext):
    raqam = 42
    soni = 53
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b42.set()

@dp.message_handler(state = holat.b42)
async def a42(msg: types.Message, state:FSMContext):
    raqam = 42
    soni = 53
    await foroyat(msg, soni, raqam, state)


#43
@dp.message_handler(Text(startswith = '43', ignore_case=True), state = holat.suralar)
async def e43(msg: types.Message, state: FSMContext):
    raqam = 43
    soni = 89
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b43.set()

@dp.message_handler(state = holat.b43)
async def a43(msg: types.Message, state:FSMContext):
    raqam = 43
    soni = 89
    await foroyat(msg, soni, raqam, state)


#44
@dp.message_handler(Text(startswith = '44', ignore_case=True), state = holat.suralar)
async def e44(msg: types.Message, state: FSMContext):
    raqam = 44
    soni = 59
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b44.set()

@dp.message_handler(state = holat.b44)
async def a44(msg: types.Message, state:FSMContext):
    raqam = 44
    soni = 59
    await foroyat(msg, soni, raqam, state)


#45
@dp.message_handler(Text(startswith = '45', ignore_case=True), state = holat.suralar)
async def e45(msg: types.Message, state: FSMContext):
    raqam = 45
    soni = 37
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b45.set()

@dp.message_handler(state = holat.b45)
async def a45(msg: types.Message, state:FSMContext):
    raqam = 45
    soni = 37
    await foroyat(msg, soni, raqam, state)


#46
@dp.message_handler(Text(startswith = '46', ignore_case=True), state = holat.suralar)
async def e46(msg: types.Message, state: FSMContext):
    raqam = 46
    soni = 35
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b46.set()

@dp.message_handler(state = holat.b46)
async def a46(msg: types.Message, state:FSMContext):
    raqam = 46
    soni = 35
    await foroyat(msg, soni, raqam, state)


#47
@dp.message_handler(Text(startswith = '47', ignore_case=True), state = holat.suralar)
async def e47(msg: types.Message, state: FSMContext):
    raqam = 47
    soni = 38
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b47.set()

@dp.message_handler(state = holat.b47)
async def a47(msg: types.Message, state:FSMContext):
    raqam = 47
    soni = 38
    await foroyat(msg, soni, raqam, state)


#48
@dp.message_handler(Text(startswith = '48', ignore_case=True), state = holat.suralar)
async def e48(msg: types.Message, state: FSMContext):
    raqam = 48
    soni = 29
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b48.set()

@dp.message_handler(state = holat.b48)
async def a48(msg: types.Message, state:FSMContext):
    raqam = 48
    soni = 29
    await foroyat(msg, soni, raqam, state)


#49
@dp.message_handler(Text(startswith = '49', ignore_case=True), state = holat.suralar)
async def e49(msg: types.Message, state: FSMContext):
    raqam = 49
    soni = 18
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b49.set()

@dp.message_handler(state = holat.b49)
async def a49(msg: types.Message, state:FSMContext):
    raqam = 49
    soni = 18
    await foroyat(msg, soni, raqam, state)


#50
@dp.message_handler(Text(startswith = '50', ignore_case=True), state = holat.suralar)
async def e50(msg: types.Message, state: FSMContext):
    raqam = 50
    soni = 45
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b50.set()

@dp.message_handler(state = holat.b50)
async def a50(msg: types.Message, state:FSMContext):
    raqam = 50
    soni = 45
    await foroyat(msg, soni, raqam, state)


#51
@dp.message_handler(Text(startswith = '51', ignore_case=True), state = holat.suralar)
async def e51(msg: types.Message, state: FSMContext):
    raqam = 51
    soni = 60
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b51.set()

@dp.message_handler(state = holat.b51)
async def a51(msg: types.Message, state:FSMContext):
    raqam = 51
    soni = 60
    await foroyat(msg, soni, raqam, state)


#52
@dp.message_handler(Text(startswith = '52', ignore_case=True), state = holat.suralar)
async def e52(msg: types.Message, state: FSMContext):
    raqam = 52
    soni = 49
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b52.set()

@dp.message_handler(state = holat.b52)
async def a52(msg: types.Message, state:FSMContext):
    raqam = 52
    soni = 49
    await foroyat(msg, soni, raqam, state)


#53
@dp.message_handler(Text(startswith = '53', ignore_case=True), state = holat.suralar)
async def e53(msg: types.Message, state: FSMContext):
    raqam = 53
    soni = 62
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b53.set()

@dp.message_handler(state = holat.b53)
async def a53(msg: types.Message, state:FSMContext):
    raqam = 53
    soni = 62
    await foroyat(msg, soni, raqam, state)


#54
@dp.message_handler(Text(startswith = '54', ignore_case=True), state = holat.suralar)
async def e54(msg: types.Message, state: FSMContext):
    raqam = 54
    soni = 55
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b54.set()

@dp.message_handler(state = holat.b54)
async def a54(msg: types.Message, state:FSMContext):
    raqam = 54
    soni = 55
    await foroyat(msg, soni, raqam, state)


#55
@dp.message_handler(Text(startswith = '55', ignore_case=True), state = holat.suralar)
async def e55(msg: types.Message, state: FSMContext):
    raqam = 55
    soni = 78
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b55.set()

@dp.message_handler(state = holat.b55)
async def a55(msg: types.Message, state:FSMContext):
    raqam = 55
    soni = 78
    await foroyat(msg, soni, raqam, state)


#56
@dp.message_handler(Text(startswith = '56', ignore_case=True), state = holat.suralar)
async def e56(msg: types.Message, state: FSMContext):
    raqam = 56
    soni = 96
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b56.set()

@dp.message_handler(state = holat.b56)
async def a56(msg: types.Message, state:FSMContext):
    raqam = 56
    soni = 96
    await foroyat(msg, soni, raqam, state)


#57
@dp.message_handler(Text(startswith = '57', ignore_case=True), state = holat.suralar)
async def e57(msg: types.Message, state: FSMContext):
    raqam = 57
    soni = 29
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b57.set()

@dp.message_handler(state = holat.b57)
async def a57(msg: types.Message, state:FSMContext):
    raqam = 57
    soni = 29
    await foroyat(msg, soni, raqam, state)


#58
@dp.message_handler(Text(startswith = '58', ignore_case=True), state = holat.suralar)
async def e58(msg: types.Message, state: FSMContext):
    raqam = 58
    soni = 22
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b58.set()

@dp.message_handler(state = holat.b58)
async def a58(msg: types.Message, state:FSMContext):
    raqam = 58
    soni = 22
    await foroyat(msg, soni, raqam, state)


#59
@dp.message_handler(Text(startswith = '59', ignore_case=True), state = holat.suralar)
async def e59(msg: types.Message, state: FSMContext):
    raqam = 59
    soni = 24
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b59.set()

@dp.message_handler(state = holat.b59)
async def a59(msg: types.Message, state:FSMContext):
    raqam = 59
    soni = 24
    await foroyat(msg, soni, raqam, state)


#60
@dp.message_handler(Text(startswith = '60', ignore_case=True), state = holat.suralar)
async def e60(msg: types.Message, state: FSMContext):
    raqam = 60
    soni = 13
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b60.set()

@dp.message_handler(state = holat.b60)
async def a60(msg: types.Message, state:FSMContext):
    raqam = 60
    soni = 13
    await foroyat(msg, soni, raqam, state)


#61
@dp.message_handler(Text(startswith = '61', ignore_case=True), state = holat.suralar)
async def e61(msg: types.Message, state: FSMContext):
    raqam = 61
    soni = 14
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b61.set()

@dp.message_handler(state = holat.b61)
async def a61(msg: types.Message, state:FSMContext):
    raqam = 61
    soni = 14
    await foroyat(msg, soni, raqam, state)


#62
@dp.message_handler(Text(startswith = '62', ignore_case=True), state = holat.suralar)
async def e62(msg: types.Message, state: FSMContext):
    raqam = 62
    soni = 11
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b62.set()

@dp.message_handler(state = holat.b62)
async def a62(msg: types.Message, state:FSMContext):
    raqam = 62
    soni = 11
    await foroyat(msg, soni, raqam, state)


#63
@dp.message_handler(Text(startswith = '63', ignore_case=True), state = holat.suralar)
async def e63(msg: types.Message, state: FSMContext):
    raqam = 63
    soni = 11
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b63.set()

@dp.message_handler(state = holat.b63)
async def a63(msg: types.Message, state:FSMContext):
    raqam = 63
    soni = 11
    await foroyat(msg, soni, raqam, state)


#64
@dp.message_handler(Text(startswith = '64', ignore_case=True), state = holat.suralar)
async def e64(msg: types.Message, state: FSMContext):
    raqam = 64
    soni = 18
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b64.set()

@dp.message_handler(state = holat.b64)
async def a64(msg: types.Message, state:FSMContext):
    raqam = 64
    soni = 18
    await foroyat(msg, soni, raqam, state)


#65
@dp.message_handler(Text(startswith = '65', ignore_case=True), state = holat.suralar)
async def e65(msg: types.Message, state: FSMContext):
    raqam = 65
    soni = 12
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b65.set()

@dp.message_handler(state = holat.b65)
async def a65(msg: types.Message, state:FSMContext):
    raqam = 65
    soni = 12
    await foroyat(msg, soni, raqam, state)


#66
@dp.message_handler(Text(startswith = '66', ignore_case=True), state = holat.suralar)
async def e66(msg: types.Message, state: FSMContext):
    raqam = 66
    soni = 12
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b66.set()

@dp.message_handler(state = holat.b66)
async def a66(msg: types.Message, state:FSMContext):
    raqam = 66
    soni = 12
    await foroyat(msg, soni, raqam, state)


#67
@dp.message_handler(Text(startswith = '67', ignore_case=True), state = holat.suralar)
async def e67(msg: types.Message, state: FSMContext):
    raqam = 67
    soni = 30
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b67.set()

@dp.message_handler(state = holat.b67)
async def a67(msg: types.Message, state:FSMContext):
    raqam = 67
    soni = 30
    await foroyat(msg, soni, raqam, state)


#68
@dp.message_handler(Text(startswith = '68', ignore_case=True), state = holat.suralar)
async def e68(msg: types.Message, state: FSMContext):
    raqam = 68
    soni = 52
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b68.set()

@dp.message_handler(state = holat.b68)
async def a68(msg: types.Message, state:FSMContext):
    raqam = 68
    soni = 52
    await foroyat(msg, soni, raqam, state)


#69
@dp.message_handler(Text(startswith = '69', ignore_case=True), state = holat.suralar)
async def e69(msg: types.Message, state: FSMContext):
    raqam = 69
    soni = 52
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b69.set()

@dp.message_handler(state = holat.b69)
async def a69(msg: types.Message, state:FSMContext):
    raqam = 69
    soni = 52
    await foroyat(msg, soni, raqam, state)


#70
@dp.message_handler(Text(startswith = '70', ignore_case=True), state = holat.suralar)
async def e70(msg: types.Message, state: FSMContext):
    raqam = 70
    soni = 44
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b70.set()

@dp.message_handler(state = holat.b70)
async def a70(msg: types.Message, state:FSMContext):
    raqam = 70
    soni = 44
    await foroyat(msg, soni, raqam, state)


#71
@dp.message_handler(Text(startswith = '71', ignore_case=True), state = holat.suralar)
async def e71(msg: types.Message, state: FSMContext):
    raqam = 71
    soni = 28
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b71.set()

@dp.message_handler(state = holat.b71)
async def a71(msg: types.Message, state:FSMContext):
    raqam = 71
    soni = 28
    await foroyat(msg, soni, raqam, state)


#72
@dp.message_handler(Text(startswith = '72', ignore_case=True), state = holat.suralar)
async def e72(msg: types.Message, state: FSMContext):
    raqam = 72
    soni = 28
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b72.set()

@dp.message_handler(state = holat.b72)
async def a72(msg: types.Message, state:FSMContext):
    raqam = 72
    soni = 28
    await foroyat(msg, soni, raqam, state)


#73
@dp.message_handler(Text(startswith = '73', ignore_case=True), state = holat.suralar)
async def e73(msg: types.Message, state: FSMContext):
    raqam = 73
    soni = 20
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b73.set()

@dp.message_handler(state = holat.b73)
async def a73(msg: types.Message, state:FSMContext):
    raqam = 73
    soni = 20
    await foroyat(msg, soni, raqam, state)


#74
@dp.message_handler(Text(startswith = '74', ignore_case=True), state = holat.suralar)
async def e74(msg: types.Message, state: FSMContext):
    raqam = 74
    soni = 56
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b74.set()

@dp.message_handler(state = holat.b74)
async def a74(msg: types.Message, state:FSMContext):
    raqam = 74
    soni = 56
    await foroyat(msg, soni, raqam, state)


#75
@dp.message_handler(Text(startswith = '75', ignore_case=True), state = holat.suralar)
async def e75(msg: types.Message, state: FSMContext):
    raqam = 75
    soni = 40
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b75.set()

@dp.message_handler(state = holat.b75)
async def a75(msg: types.Message, state:FSMContext):
    raqam = 75
    soni = 40
    await foroyat(msg, soni, raqam, state)


#76
@dp.message_handler(Text(startswith = '76', ignore_case=True), state = holat.suralar)
async def e76(msg: types.Message, state: FSMContext):
    raqam = 76
    soni = 31
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b76.set()

@dp.message_handler(state = holat.b76)
async def a76(msg: types.Message, state:FSMContext):
    raqam = 76
    soni = 31
    await foroyat(msg, soni, raqam, state)


#77
@dp.message_handler(Text(startswith = '77', ignore_case=True), state = holat.suralar)
async def e77(msg: types.Message, state: FSMContext):
    raqam = 77
    soni = 50
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b77.set()

@dp.message_handler(state = holat.b77)
async def a77(msg: types.Message, state:FSMContext):
    raqam = 77
    soni = 50
    await foroyat(msg, soni, raqam, state)


#78
@dp.message_handler(Text(startswith = '78', ignore_case=True), state = holat.suralar)
async def e78(msg: types.Message, state: FSMContext):
    raqam = 78
    soni = 40
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b78.set()

@dp.message_handler(state = holat.b78)
async def a78(msg: types.Message, state:FSMContext):
    raqam = 78
    soni = 40
    await foroyat(msg, soni, raqam, state)


#79
@dp.message_handler(Text(startswith = '79', ignore_case=True), state = holat.suralar)
async def e79(msg: types.Message, state: FSMContext):
    raqam = 79
    soni = 46
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b79.set()

@dp.message_handler(state = holat.b79)
async def a79(msg: types.Message, state:FSMContext):
    raqam = 79
    soni = 46
    await foroyat(msg, soni, raqam, state)


#80
@dp.message_handler(Text(startswith = '80', ignore_case=True), state = holat.suralar)
async def e80(msg: types.Message, state: FSMContext):
    raqam = 80
    soni = 42
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b80.set()

@dp.message_handler(state = holat.b80)
async def a80(msg: types.Message, state:FSMContext):
    raqam = 80
    soni = 42
    await foroyat(msg, soni, raqam, state)


#81
@dp.message_handler(Text(startswith = '81', ignore_case=True), state = holat.suralar)
async def e81(msg: types.Message, state: FSMContext):
    raqam = 81
    soni = 29
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b81.set()

@dp.message_handler(state = holat.b81)
async def a81(msg: types.Message, state:FSMContext):
    raqam = 81
    soni = 29
    await foroyat(msg, soni, raqam, state)


#82
@dp.message_handler(Text(startswith = '82', ignore_case=True), state = holat.suralar)
async def e82(msg: types.Message, state: FSMContext):
    raqam = 82
    soni = 19
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b82.set()

@dp.message_handler(state = holat.b82)
async def a82(msg: types.Message, state:FSMContext):
    raqam = 82
    soni = 19
    await foroyat(msg, soni, raqam, state)


#83
@dp.message_handler(Text(startswith = '83', ignore_case=True), state = holat.suralar)
async def e83(msg: types.Message, state: FSMContext):
    raqam = 83
    soni = 36
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b83.set()

@dp.message_handler(state = holat.b83)
async def a83(msg: types.Message, state:FSMContext):
    raqam = 83
    soni = 36
    await foroyat(msg, soni, raqam, state)


#84
@dp.message_handler(Text(startswith = '84', ignore_case=True), state = holat.suralar)
async def e84(msg: types.Message, state: FSMContext):
    raqam = 84
    soni = 25
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b84.set()

@dp.message_handler(state = holat.b84)
async def a84(msg: types.Message, state:FSMContext):
    raqam = 84
    soni = 25
    await foroyat(msg, soni, raqam, state)


#85
@dp.message_handler(Text(startswith = '85', ignore_case=True), state = holat.suralar)
async def e85(msg: types.Message, state: FSMContext):
    raqam = 85
    soni = 22
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b85.set()

@dp.message_handler(state = holat.b85)
async def a85(msg: types.Message, state:FSMContext):
    raqam = 85
    soni = 22
    await foroyat(msg, soni, raqam, state)


#86
@dp.message_handler(Text(startswith = '86', ignore_case=True), state = holat.suralar)
async def e86(msg: types.Message, state: FSMContext):
    raqam = 86
    soni = 17
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b86.set()

@dp.message_handler(state = holat.b86)
async def a86(msg: types.Message, state:FSMContext):
    raqam = 86
    soni = 17
    await foroyat(msg, soni, raqam, state)


#87
@dp.message_handler(Text(startswith = '87', ignore_case=True), state = holat.suralar)
async def e87(msg: types.Message, state: FSMContext):
    raqam = 87
    soni = 19
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b87.set()

@dp.message_handler(state = holat.b87)
async def a87(msg: types.Message, state:FSMContext):
    raqam = 87
    soni = 19
    await foroyat(msg, soni, raqam, state)


#88
@dp.message_handler(Text(startswith = '88', ignore_case=True), state = holat.suralar)
async def e88(msg: types.Message, state: FSMContext):
    raqam = 88
    soni = 26
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b88.set()

@dp.message_handler(state = holat.b88)
async def a88(msg: types.Message, state:FSMContext):
    raqam = 88
    soni = 26
    await foroyat(msg, soni, raqam, state)


#89
@dp.message_handler(Text(startswith = '89', ignore_case=True), state = holat.suralar)
async def e89(msg: types.Message, state: FSMContext):
    raqam = 89
    soni = 30
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b89.set()

@dp.message_handler(state = holat.b89)
async def a89(msg: types.Message, state:FSMContext):
    raqam = 89
    soni = 30
    await foroyat(msg, soni, raqam, state)


#90
@dp.message_handler(Text(startswith = '90', ignore_case=True), state = holat.suralar)
async def e90(msg: types.Message, state: FSMContext):
    raqam = 90
    soni = 20
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b90.set()

@dp.message_handler(state = holat.b90)
async def a90(msg: types.Message, state:FSMContext):
    raqam = 90
    soni = 20
    await foroyat(msg, soni, raqam, state)


#91
@dp.message_handler(Text(startswith = '91', ignore_case=True), state = holat.suralar)
async def e91(msg: types.Message, state: FSMContext):
    raqam = 91
    soni = 15
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b91.set()

@dp.message_handler(state = holat.b91)
async def a91(msg: types.Message, state:FSMContext):
    raqam = 91
    soni = 15
    await foroyat(msg, soni, raqam, state)


#92
@dp.message_handler(Text(startswith = '92', ignore_case=True), state = holat.suralar)
async def e92(msg: types.Message, state: FSMContext):
    raqam = 92
    soni = 21
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b92.set()

@dp.message_handler(state = holat.b92)
async def a92(msg: types.Message, state:FSMContext):
    raqam = 92
    soni = 21
    await foroyat(msg, soni, raqam, state)


#93
@dp.message_handler(Text(startswith = '93', ignore_case=True), state = holat.suralar)
async def e93(msg: types.Message, state: FSMContext):
    raqam = 93
    soni = 11
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b93.set()

@dp.message_handler(state = holat.b93)
async def a93(msg: types.Message, state:FSMContext):
    raqam = 93
    soni = 11
    await foroyat(msg, soni, raqam, state)


#94
@dp.message_handler(Text(startswith = '94', ignore_case=True), state = holat.suralar)
async def e94(msg: types.Message, state: FSMContext):
    raqam = 94
    soni = 8
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b94.set()

@dp.message_handler(state = holat.b94)
async def a94(msg: types.Message, state:FSMContext):
    raqam = 94
    soni = 8
    await foroyat(msg, soni, raqam, state)


#95
@dp.message_handler(Text(startswith = '95', ignore_case=True), state = holat.suralar)
async def e95(msg: types.Message, state: FSMContext):
    raqam = 95
    soni = 8
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b95.set()

@dp.message_handler(state = holat.b95)
async def a95(msg: types.Message, state:FSMContext):
    raqam = 95
    soni = 8
    await foroyat(msg, soni, raqam, state)


#96
@dp.message_handler(Text(startswith = '96', ignore_case=True), state = holat.suralar)
async def e96(msg: types.Message, state: FSMContext):
    raqam = 96
    soni = 19
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b96.set()

@dp.message_handler(state = holat.b96)
async def a96(msg: types.Message, state:FSMContext):
    raqam = 96
    soni = 19
    await foroyat(msg, soni, raqam, state)


#97
@dp.message_handler(Text(startswith = '97', ignore_case=True), state = holat.suralar)
async def e97(msg: types.Message, state: FSMContext):
    raqam = 97
    soni = 5
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b97.set()

@dp.message_handler(state = holat.b97)
async def a97(msg: types.Message, state:FSMContext):
    raqam = 97
    soni = 5
    await foroyat(msg, soni, raqam, state)


#98
@dp.message_handler(Text(startswith = '98', ignore_case=True), state = holat.suralar)
async def e98(msg: types.Message, state: FSMContext):
    raqam = 98
    soni = 8
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b98.set()

@dp.message_handler(state = holat.b98)
async def a98(msg: types.Message, state:FSMContext):
    raqam = 98
    soni = 8
    await foroyat(msg, soni, raqam, state)


#99
@dp.message_handler(Text(startswith = '99', ignore_case=True), state = holat.suralar)
async def e99(msg: types.Message, state: FSMContext):
    raqam = 99
    soni = 8
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b99.set()

@dp.message_handler(state = holat.b99)
async def a99(msg: types.Message, state:FSMContext):
    raqam = 99
    soni = 8
    await foroyat(msg, soni, raqam, state)


#100
@dp.message_handler(Text(startswith = '100', ignore_case=True), state = holat.suralar)
async def e100(msg: types.Message, state: FSMContext):
    raqam = 100
    soni = 11
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b100.set()

@dp.message_handler(state = holat.b100)
async def a100(msg: types.Message, state:FSMContext):
    raqam = 100
    soni = 11
    await foroyat(msg, soni, raqam, state)


#101
@dp.message_handler(Text(startswith = '101', ignore_case=True), state = holat.suralar)
async def e101(msg: types.Message, state: FSMContext):
    raqam = 101
    soni = 11
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b101.set()

@dp.message_handler(state = holat.b101)
async def a101(msg: types.Message, state:FSMContext):
    raqam = 101
    soni = 11
    await foroyat(msg, soni, raqam, state)


#102
@dp.message_handler(Text(startswith = '102', ignore_case=True), state = holat.suralar)
async def e102(msg: types.Message, state: FSMContext):
    raqam = 102
    soni = 8
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b102.set()

@dp.message_handler(state = holat.b102)
async def a102(msg: types.Message, state:FSMContext):
    raqam = 102
    soni = 8
    await foroyat(msg, soni, raqam, state)


#103
@dp.message_handler(Text(startswith = '103', ignore_case=True), state = holat.suralar)
async def e103(msg: types.Message, state: FSMContext):
    raqam = 103
    soni = 3
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b103.set()

@dp.message_handler(state = holat.b103)
async def a103(msg: types.Message, state:FSMContext):
    raqam = 103
    soni = 3
    await foroyat(msg, soni, raqam, state)


#104
@dp.message_handler(Text(startswith = '104', ignore_case=True), state = holat.suralar)
async def e104(msg: types.Message, state: FSMContext):
    raqam = 104
    soni = 9
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b104.set()

@dp.message_handler(state = holat.b104)
async def a104(msg: types.Message, state:FSMContext):
    raqam = 104
    soni = 9
    await foroyat(msg, soni, raqam, state)


#105
@dp.message_handler(Text(startswith = '105', ignore_case=True), state = holat.suralar)
async def e105(msg: types.Message, state: FSMContext):
    raqam = 105
    soni = 5
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b105.set()

@dp.message_handler(state = holat.b105)
async def a105(msg: types.Message, state:FSMContext):
    raqam = 105
    soni = 5
    await foroyat(msg, soni, raqam, state)


#106
@dp.message_handler(Text(startswith = '106', ignore_case=True), state = holat.suralar)
async def e106(msg: types.Message, state: FSMContext):
    raqam = 106
    soni = 4
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b106.set()

@dp.message_handler(state = holat.b106)
async def a106(msg: types.Message, state:FSMContext):
    raqam = 106
    soni = 4
    await foroyat(msg, soni, raqam, state)


#107
@dp.message_handler(Text(startswith = '107', ignore_case=True), state = holat.suralar)
async def e107(msg: types.Message, state: FSMContext):
    raqam = 107
    soni = 7
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b107.set()

@dp.message_handler(state = holat.b107)
async def a107(msg: types.Message, state:FSMContext):
    raqam = 107
    soni = 7
    await foroyat(msg, soni, raqam, state)


#108
@dp.message_handler(Text(startswith = '108', ignore_case=True), state = holat.suralar)
async def e108(msg: types.Message, state: FSMContext):
    raqam = 108
    soni = 3
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b108.set()

@dp.message_handler(state = holat.b108)
async def a108(msg: types.Message, state:FSMContext):
    raqam = 108
    soni = 3
    await foroyat(msg, soni, raqam, state)


#109
@dp.message_handler(Text(startswith = '109', ignore_case=True), state = holat.suralar)
async def e109(msg: types.Message, state: FSMContext):
    raqam = 109
    soni = 6
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b109.set()

@dp.message_handler(state = holat.b109)
async def a109(msg: types.Message, state:FSMContext):
    raqam = 109
    soni = 6
    await foroyat(msg, soni, raqam, state)


#110
@dp.message_handler(Text(startswith = '110', ignore_case=True), state = holat.suralar)
async def e110(msg: types.Message, state: FSMContext):
    raqam = 110
    soni = 3
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b110.set()

@dp.message_handler(state = holat.b110)
async def a110(msg: types.Message, state:FSMContext):
    raqam = 110
    soni = 3
    await foroyat(msg, soni, raqam, state)


#111
@dp.message_handler(Text(startswith = '111', ignore_case=True), state = holat.suralar)
async def e111(msg: types.Message, state: FSMContext):
    raqam = 111
    soni = 5
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b111.set()

@dp.message_handler(state = holat.b111)
async def a111(msg: types.Message, state:FSMContext):
    raqam = 111
    soni = 5
    await foroyat(msg, soni, raqam, state)


#112
@dp.message_handler(Text(startswith = '112', ignore_case=True), state = holat.suralar)
async def e112(msg: types.Message, state: FSMContext):
    raqam = 112
    soni = 4
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b112.set()

@dp.message_handler(state = holat.b112)
async def a112(msg: types.Message, state:FSMContext):
    raqam = 112
    soni = 4
    await foroyat(msg, soni, raqam, state)


#113
@dp.message_handler(Text(startswith = '113', ignore_case=True), state = holat.suralar)
async def e113(msg: types.Message, state: FSMContext):
    raqam = 113
    soni = 5
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b113.set()

@dp.message_handler(state = holat.b113)
async def a113(msg: types.Message, state:FSMContext):
    raqam = 113
    soni = 5
    await foroyat(msg, soni, raqam, state)


#114
@dp.message_handler(Text(startswith = '114', ignore_case=True), state = holat.suralar)
async def e114(msg: types.Message, state: FSMContext):
    raqam = 114
    soni = 6
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b114.set()

@dp.message_handler(state = holat.b114)
async def a114(msg: types.Message, state:FSMContext):
    raqam = 114
    soni = 6
    await foroyat(msg, soni, raqam, state)



#2
@dp.message_handler(Text(startswith = '2', ignore_case=True), state = holat.suralar)
async def e2(msg: types.Message, state: FSMContext):
    raqam = 2
    soni = 286
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b2.set()

@dp.message_handler(state = holat.b2)
async def a2(msg: types.Message, state:FSMContext):
    raqam = 2
    soni = 286
    await foroyat(msg, soni, raqam, state)


#3
@dp.message_handler(Text(startswith = '3', ignore_case=True), state = holat.suralar)
async def e3(msg: types.Message, state: FSMContext):
    raqam = 3
    soni = 200
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b3.set()

@dp.message_handler(state = holat.b3)
async def a3(msg: types.Message, state:FSMContext):
    raqam = 3
    soni = 200
    await foroyat(msg, soni, raqam, state)


#4
@dp.message_handler(Text(startswith = '4', ignore_case=True), state = holat.suralar)
async def e4(msg: types.Message, state: FSMContext):
    raqam = 4
    soni = 176
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b4.set()

@dp.message_handler(state = holat.b4)
async def a4(msg: types.Message, state:FSMContext):
    raqam = 4
    soni = 176
    await foroyat(msg, soni, raqam, state)


#5
@dp.message_handler(Text(startswith = '5', ignore_case=True), state = holat.suralar)
async def e5(msg: types.Message, state: FSMContext):
    raqam = 5
    soni = 120
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b5.set()

@dp.message_handler(state = holat.b5)
async def a5(msg: types.Message, state:FSMContext):
    raqam = 5
    soni = 120
    await foroyat(msg, soni, raqam, state)


#6
@dp.message_handler(Text(startswith = '6', ignore_case=True), state = holat.suralar)
async def e6(msg: types.Message, state: FSMContext):
    raqam = 6
    soni = 165
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b6.set()

@dp.message_handler(state = holat.b6)
async def a6(msg: types.Message, state:FSMContext):
    raqam = 6
    soni = 165
    await foroyat(msg, soni, raqam, state)


#7
@dp.message_handler(Text(startswith = '7', ignore_case=True), state = holat.suralar)
async def e7(msg: types.Message, state: FSMContext):
    raqam = 7
    soni = 206
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b7.set()

@dp.message_handler(state = holat.b7)
async def a7(msg: types.Message, state:FSMContext):
    raqam = 7
    soni = 206
    await foroyat(msg, soni, raqam, state)


#8
@dp.message_handler(Text(startswith = '8', ignore_case=True), state = holat.suralar)
async def e8(msg: types.Message, state: FSMContext):
    raqam = 8
    soni = 75
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b8.set()

@dp.message_handler(state = holat.b8)
async def a8(msg: types.Message, state:FSMContext):
    raqam = 8
    soni = 75
    await foroyat(msg, soni, raqam, state)


#9
@dp.message_handler(Text(startswith = '9', ignore_case=True), state = holat.suralar)
async def e9(msg: types.Message, state: FSMContext):
    raqam = 9
    soni = 129
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b9.set()

@dp.message_handler(state = holat.b9)
async def a9(msg: types.Message, state:FSMContext):
    raqam = 9
    soni = 129
    await foroyat(msg, soni, raqam, state)


#10
@dp.message_handler(Text(startswith = '10', ignore_case=True), state = holat.suralar)
async def e10(msg: types.Message, state: FSMContext):
    raqam = 10
    soni = 109
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b10.set()

@dp.message_handler(state = holat.b10)
async def a10(msg: types.Message, state:FSMContext):
    raqam = 10
    soni = 109
    await foroyat(msg, soni, raqam, state)


#11
@dp.message_handler(Text(startswith = '11', ignore_case=True), state = holat.suralar)
async def e11(msg: types.Message, state: FSMContext):
    raqam = 11
    soni = 123
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz. Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b11.set()

@dp.message_handler(state = holat.b11)
async def a11(msg: types.Message, state:FSMContext):
    raqam = 11
    soni = 123
    await foroyat(msg, soni, raqam, state)

#1
@dp.message_handler(Text(startswith = '1', ignore_case=True), state = holat.suralar)
async def e1(msg: types.Message, state: FSMContext):
    raqam = 1
    soni = 7
    await msg.answer(f"Siz {suralist[raqam-1]} surasini tanladingiz.Shu suradan qidirish uchun matn kiritng.", reply_markup=mainAndbackKeyboard)
    await holat.b1.set()

@dp.message_handler(state = holat.b1)
async def a1(msg: types.Message, state:FSMContext):
    raqam = 1
    soni = 7
    await foroyat(msg, soni, raqam, state)
