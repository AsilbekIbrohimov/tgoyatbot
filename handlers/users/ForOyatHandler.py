
# from fuzzywuzzy import fuzz
import asyncio
import re
from aiogram import types
from aiogram.utils import exceptions
from states.searcherState import AyahSearch as holat
from aiogram.dispatcher import FSMContext
from loader import dp,bot, db
from keyboards.default.suralistKeyboard import suraKeyboard1, suraKeyboard2
from keyboards.inline.ContinueKeyboard import ContinueKeyboard
from aiogram.types import ContentType, CallbackQuery
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard, mainAndbackKeyboard
from keyboards.default.forstartKeyboard import startKeyboard
from data.qurandict import qurandict
from data.qurandict2 import qurandict2
from utils.get_link import get_link
from aiogram.dispatcher.filters import Text
from data.suralist import suralist
from keyboards.inline.changePageKeyboard import pages
from utils.searcher import make

def answertext(soni, raqam):
    return f"{suralist[raqam-1]} surasi {soni} ta oyatdan iborat\n\no'qimoqchi bo'lgan oyatingizning raqamini kiriting\n\nyoki ko'proq oyat o'qimoqchi bo'lsangiz oyatlarni quyidagi ko'rinishda kiriting\n\n➡️  2,5,12,13 ....\n\nYoki\n\n➡️  1-5 ko'rinishida xabar jo'nating\n\nSuraning barcha oyatlarni o'qish uchun 1-{soni} deb xabar jo'nating"

users3 = {}

async def foroyat(msg: types.Message, soni, raqam):
    keyboard = None
    if raqam > 56:
        keyboard = suraKeyboard2
    else:
        keyboard = suraKeyboard1
    quran = {}
    if db.select_user(id = msg.from_user.id)[4]:
        quran = qurandict2
    else:
        quran = qurandict
    if msg.text == '⬅️ Orqaga':
        await msg.answer("o'zingizga kerakli surani tanlang", reply_markup=keyboard)
        await holat.suralar.set()
    elif msg.text.isdigit():
        if int(msg.text)<1 or int(msg.text)> soni:
            await msg.answer(f"1 dan {soni} gacha raqam kiriting")
        else:
            await msg.answer(f"{suralist[raqam-1]} surasi {msg.text}-oyat\n\n{quran[str(raqam)][int(msg.text)-1]['text']}{await get_link(raqam, msg.text)}")
    elif re.search("^[\d]{1,3}[-][\d]{1,3}$", msg.text):
    
        list_order = msg.text.split('-')
        tartib_raqami = int(list_order[0])
        if int(list_order[1]) > soni:
            await msg.answer("Nato'g'ri kiritdingiz")
        else:
            users3[msg.from_user.id] = [list_order, tartib_raqami, raqam]
            for i in quran[str(raqam)][int(list_order[0])-1:int(list_order[1])]:
                await msg.answer(f"{suralist[raqam-1]} surasi {users3[msg.from_user.id][1]}-oyat\n\n{i['text']}{await get_link(raqam, tartib_raqami)}")
                await asyncio.sleep(1.4)
                if users3[msg.from_user.id][1]%50==0:
                    await msg.answer('Davomomini ko\'rishni xoxlaysizmi?', reply_markup=ContinueKeyboard)
                    break
                users3[msg.from_user.id][1]+=1
                tartib_raqami+=1
            
            del tartib_raqami
    else:
        await msg.answer("Natog'ri kiritidingiz")

@dp.callback_query_handler(text="davomi", state = '*')
async def davomi(call: CallbackQuery):
    users3[call.from_user.id][1]+=1
    await call.message.delete()
    user_id = call.from_user.id
    user = users3[call.from_user.id]
    raqam = user[2]
    list_order = user[0]
    tartib_raqami = user[1]
    quran = {}
    if db.select_user(id = call.from_user.id)[4]:
        quran = qurandict2
    else:
        quran = qurandict
    for i in quran[str(raqam)][tartib_raqami-1:int(list_order[1])]:
                length = f"""{suralist[raqam-1]} surasi {user[1]}-oyat\n\n{i['text']}{await get_link(raqam, user[1])}"""
                await bot.send_message(chat_id = user_id, text = length)
                await asyncio.sleep(0.4)
                if user[1]%50==0:
                    await bot.send_message(text = 'Davomomini ko\'rishni xoxlaysizmi?', chat_id = user_id, reply_markup=ContinueKeyboard)
                    break
                user[1]+=1


@dp.errors_handler(exception=exceptions.RetryAfter)
async def exception_handler(update: types.Update, exception: exceptions.RetryAfter):
    # Do something
    return True

#12
@dp.message_handler(Text(startswith = '12', ignore_case=True), state = holat.suralar)
async def b12(msg: types.Message, state: FSMContext):
    raqam = 12
    soni = 111
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a12.set()

@dp.message_handler(state = holat.a12)
async def a12(msg: types.Message, state:FSMContext):
    raqam = 12
    soni = 111
    await foroyat(msg, soni, raqam)


#13
@dp.message_handler(Text(startswith = '13', ignore_case=True), state = holat.suralar)
async def b13(msg: types.Message, state: FSMContext):
    raqam = 13
    soni = 43
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a13.set()

@dp.message_handler(state = holat.a13)
async def a13(msg: types.Message, state:FSMContext):
    raqam = 13
    soni = 43
    await foroyat(msg, soni, raqam)


#14
@dp.message_handler(Text(startswith = '14', ignore_case=True), state = holat.suralar)
async def b14(msg: types.Message, state: FSMContext):
    raqam = 14
    soni = 52
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a14.set()

@dp.message_handler(state = holat.a14)
async def a14(msg: types.Message, state:FSMContext):
    raqam = 14
    soni = 52
    await foroyat(msg, soni, raqam)


#15
@dp.message_handler(Text(startswith = '15', ignore_case=True), state = holat.suralar)
async def b15(msg: types.Message, state: FSMContext):
    raqam = 15
    soni = 99
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a15.set()

@dp.message_handler(state = holat.a15)
async def a15(msg: types.Message, state:FSMContext):
    raqam = 15
    soni = 99
    await foroyat(msg, soni, raqam)


#16
@dp.message_handler(Text(startswith = '16', ignore_case=True), state = holat.suralar)
async def b16(msg: types.Message, state: FSMContext):
    raqam = 16
    soni = 128
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a16.set()

@dp.message_handler(state = holat.a16)
async def a16(msg: types.Message, state:FSMContext):
    raqam = 16
    soni = 128
    await foroyat(msg, soni, raqam)


#17
@dp.message_handler(Text(startswith = '17', ignore_case=True), state = holat.suralar)
async def b17(msg: types.Message, state: FSMContext):
    raqam = 17
    soni = 111
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a17.set()

@dp.message_handler(state = holat.a17)
async def a17(msg: types.Message, state:FSMContext):
    raqam = 17
    soni = 111
    await foroyat(msg, soni, raqam)


#18
@dp.message_handler(Text(startswith = '18', ignore_case=True), state = holat.suralar)
async def b18(msg: types.Message, state: FSMContext):
    raqam = 18
    soni = 110
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a18.set()

@dp.message_handler(state = holat.a18)
async def a18(msg: types.Message, state:FSMContext):
    raqam = 18
    soni = 110
    await foroyat(msg, soni, raqam)


#19
@dp.message_handler(Text(startswith = '19', ignore_case=True), state = holat.suralar)
async def b19(msg: types.Message, state: FSMContext):
    raqam = 19
    soni = 98
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a19.set()

@dp.message_handler(state = holat.a19)
async def a19(msg: types.Message, state:FSMContext):
    raqam = 19
    soni = 98
    await foroyat(msg, soni, raqam)


#20
@dp.message_handler(Text(startswith = '20', ignore_case=True), state = holat.suralar)
async def b20(msg: types.Message, state: FSMContext):
    raqam = 20
    soni = 135
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a20.set()

@dp.message_handler(state = holat.a20)
async def a20(msg: types.Message, state:FSMContext):
    raqam = 20
    soni = 135
    await foroyat(msg, soni, raqam)


#21
@dp.message_handler(Text(startswith = '21', ignore_case=True), state = holat.suralar)
async def b21(msg: types.Message, state: FSMContext):
    raqam = 21
    soni = 112
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a21.set()

@dp.message_handler(state = holat.a21)
async def a21(msg: types.Message, state:FSMContext):
    raqam = 21
    soni = 112
    await foroyat(msg, soni, raqam)


#22
@dp.message_handler(Text(startswith = '22', ignore_case=True), state = holat.suralar)
async def b22(msg: types.Message, state: FSMContext):
    raqam = 22
    soni = 78
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a22.set()

@dp.message_handler(state = holat.a22)
async def a22(msg: types.Message, state:FSMContext):
    raqam = 22
    soni = 78
    await foroyat(msg, soni, raqam)


#23
@dp.message_handler(Text(startswith = '23', ignore_case=True), state = holat.suralar)
async def b23(msg: types.Message, state: FSMContext):
    raqam = 23
    soni = 118
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a23.set()

@dp.message_handler(state = holat.a23)
async def a23(msg: types.Message, state:FSMContext):
    raqam = 23
    soni = 118
    await foroyat(msg, soni, raqam)


#24
@dp.message_handler(Text(startswith = '24', ignore_case=True), state = holat.suralar)
async def b24(msg: types.Message, state: FSMContext):
    raqam = 24
    soni = 64
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a24.set()

@dp.message_handler(state = holat.a24)
async def a24(msg: types.Message, state:FSMContext):
    raqam = 24
    soni = 64
    await foroyat(msg, soni, raqam)


#25
@dp.message_handler(Text(startswith = '25', ignore_case=True), state = holat.suralar)
async def b25(msg: types.Message, state: FSMContext):
    raqam = 25
    soni = 77
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a25.set()

@dp.message_handler(state = holat.a25)
async def a25(msg: types.Message, state:FSMContext):
    raqam = 25
    soni = 77
    await foroyat(msg, soni, raqam)


#26
@dp.message_handler(Text(startswith = '26', ignore_case=True), state = holat.suralar)
async def b26(msg: types.Message, state: FSMContext):
    raqam = 26
    soni = 227
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a26.set()

@dp.message_handler(state = holat.a26)
async def a26(msg: types.Message, state:FSMContext):
    raqam = 26
    soni = 227
    await foroyat(msg, soni, raqam)


#27
@dp.message_handler(Text(startswith = '27', ignore_case=True), state = holat.suralar)
async def b27(msg: types.Message, state: FSMContext):
    raqam = 27
    soni = 93
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a27.set()

@dp.message_handler(state = holat.a27)
async def a27(msg: types.Message, state:FSMContext):
    raqam = 27
    soni = 93
    await foroyat(msg, soni, raqam)


#28
@dp.message_handler(Text(startswith = '28', ignore_case=True), state = holat.suralar)
async def b28(msg: types.Message, state: FSMContext):
    raqam = 28
    soni = 88
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a28.set()

@dp.message_handler(state = holat.a28)
async def a28(msg: types.Message, state:FSMContext):
    raqam = 28
    soni = 88
    await foroyat(msg, soni, raqam)


#29
@dp.message_handler(Text(startswith = '29', ignore_case=True), state = holat.suralar)
async def b29(msg: types.Message, state: FSMContext):
    raqam = 29
    soni = 69
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a29.set()

@dp.message_handler(state = holat.a29)
async def a29(msg: types.Message, state:FSMContext):
    raqam = 29
    soni = 69
    await foroyat(msg, soni, raqam)


#30
@dp.message_handler(Text(startswith = '30', ignore_case=True), state = holat.suralar)
async def b30(msg: types.Message, state: FSMContext):
    raqam = 30
    soni = 60
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a30.set()

@dp.message_handler(state = holat.a30)
async def a30(msg: types.Message, state:FSMContext):
    raqam = 30
    soni = 60
    await foroyat(msg, soni, raqam)


#31
@dp.message_handler(Text(startswith = '31', ignore_case=True), state = holat.suralar)
async def b31(msg: types.Message, state: FSMContext):
    raqam = 31
    soni = 34
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a31.set()

@dp.message_handler(state = holat.a31)
async def a31(msg: types.Message, state:FSMContext):
    raqam = 31
    soni = 34
    await foroyat(msg, soni, raqam)


#32
@dp.message_handler(Text(startswith = '32', ignore_case=True), state = holat.suralar)
async def b32(msg: types.Message, state: FSMContext):
    raqam = 32
    soni = 30
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a32.set()

@dp.message_handler(state = holat.a32)
async def a32(msg: types.Message, state:FSMContext):
    raqam = 32
    soni = 30
    await foroyat(msg, soni, raqam)


#33
@dp.message_handler(Text(startswith = '33', ignore_case=True), state = holat.suralar)
async def b33(msg: types.Message, state: FSMContext):
    raqam = 33
    soni = 73
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a33.set()

@dp.message_handler(state = holat.a33)
async def a33(msg: types.Message, state:FSMContext):
    raqam = 33
    soni = 73
    await foroyat(msg, soni, raqam)


#34
@dp.message_handler(Text(startswith = '34', ignore_case=True), state = holat.suralar)
async def b34(msg: types.Message, state: FSMContext):
    raqam = 34
    soni = 54
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a34.set()

@dp.message_handler(state = holat.a34)
async def a34(msg: types.Message, state:FSMContext):
    raqam = 34
    soni = 54
    await foroyat(msg, soni, raqam)


#35
@dp.message_handler(Text(startswith = '35', ignore_case=True), state = holat.suralar)
async def b35(msg: types.Message, state: FSMContext):
    raqam = 35
    soni = 45
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a35.set()

@dp.message_handler(state = holat.a35)
async def a35(msg: types.Message, state:FSMContext):
    raqam = 35
    soni = 45
    await foroyat(msg, soni, raqam)


#36
@dp.message_handler(Text(startswith = '36', ignore_case=True), state = holat.suralar)
async def b36(msg: types.Message, state: FSMContext):
    raqam = 36
    soni = 83
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a36.set()

@dp.message_handler(state = holat.a36)
async def a36(msg: types.Message, state:FSMContext):
    raqam = 36
    soni = 83
    await foroyat(msg, soni, raqam)


#37
@dp.message_handler(Text(startswith = '37', ignore_case=True), state = holat.suralar)
async def b37(msg: types.Message, state: FSMContext):
    raqam = 37
    soni = 182
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a37.set()

@dp.message_handler(state = holat.a37)
async def a37(msg: types.Message, state:FSMContext):
    raqam = 37
    soni = 182
    await foroyat(msg, soni, raqam)


#38
@dp.message_handler(Text(startswith = '38', ignore_case=True), state = holat.suralar)
async def b38(msg: types.Message, state: FSMContext):
    raqam = 38
    soni = 88
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a38.set()

@dp.message_handler(state = holat.a38)
async def a38(msg: types.Message, state:FSMContext):
    raqam = 38
    soni = 88
    await foroyat(msg, soni, raqam)


#39
@dp.message_handler(Text(startswith = '39', ignore_case=True), state = holat.suralar)
async def b39(msg: types.Message, state: FSMContext):
    raqam = 39
    soni = 75
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a39.set()

@dp.message_handler(state = holat.a39)
async def a39(msg: types.Message, state:FSMContext):
    raqam = 39
    soni = 75
    await foroyat(msg, soni, raqam)


#40
@dp.message_handler(Text(startswith = '40', ignore_case=True), state = holat.suralar)
async def b40(msg: types.Message, state: FSMContext):
    raqam = 40
    soni = 85
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a40.set()

@dp.message_handler(state = holat.a40)
async def a40(msg: types.Message, state:FSMContext):
    raqam = 40
    soni = 85
    await foroyat(msg, soni, raqam)


#41
@dp.message_handler(Text(startswith = '41', ignore_case=True), state = holat.suralar)
async def b41(msg: types.Message, state: FSMContext):
    raqam = 41
    soni = 54
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a41.set()

@dp.message_handler(state = holat.a41)
async def a41(msg: types.Message, state:FSMContext):
    raqam = 41
    soni = 54
    await foroyat(msg, soni, raqam)


#42
@dp.message_handler(Text(startswith = '42', ignore_case=True), state = holat.suralar)
async def b42(msg: types.Message, state: FSMContext):
    raqam = 42
    soni = 53
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a42.set()

@dp.message_handler(state = holat.a42)
async def a42(msg: types.Message, state:FSMContext):
    raqam = 42
    soni = 53
    await foroyat(msg, soni, raqam)


#43
@dp.message_handler(Text(startswith = '43', ignore_case=True), state = holat.suralar)
async def b43(msg: types.Message, state: FSMContext):
    raqam = 43
    soni = 89
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a43.set()

@dp.message_handler(state = holat.a43)
async def a43(msg: types.Message, state:FSMContext):
    raqam = 43
    soni = 89
    await foroyat(msg, soni, raqam)


#44
@dp.message_handler(Text(startswith = '44', ignore_case=True), state = holat.suralar)
async def b44(msg: types.Message, state: FSMContext):
    raqam = 44
    soni = 59
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a44.set()

@dp.message_handler(state = holat.a44)
async def a44(msg: types.Message, state:FSMContext):
    raqam = 44
    soni = 59
    await foroyat(msg, soni, raqam)


#45
@dp.message_handler(Text(startswith = '45', ignore_case=True), state = holat.suralar)
async def b45(msg: types.Message, state: FSMContext):
    raqam = 45
    soni = 37
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a45.set()

@dp.message_handler(state = holat.a45)
async def a45(msg: types.Message, state:FSMContext):
    raqam = 45
    soni = 37
    await foroyat(msg, soni, raqam)


#46
@dp.message_handler(Text(startswith = '46', ignore_case=True), state = holat.suralar)
async def b46(msg: types.Message, state: FSMContext):
    raqam = 46
    soni = 35
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a46.set()

@dp.message_handler(state = holat.a46)
async def a46(msg: types.Message, state:FSMContext):
    raqam = 46
    soni = 35
    await foroyat(msg, soni, raqam)


#47
@dp.message_handler(Text(startswith = '47', ignore_case=True), state = holat.suralar)
async def b47(msg: types.Message, state: FSMContext):
    raqam = 47
    soni = 38
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a47.set()

@dp.message_handler(state = holat.a47)
async def a47(msg: types.Message, state:FSMContext):
    raqam = 47
    soni = 38
    await foroyat(msg, soni, raqam)


#48
@dp.message_handler(Text(startswith = '48', ignore_case=True), state = holat.suralar)
async def b48(msg: types.Message, state: FSMContext):
    raqam = 48
    soni = 29
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a48.set()

@dp.message_handler(state = holat.a48)
async def a48(msg: types.Message, state:FSMContext):
    raqam = 48
    soni = 29
    await foroyat(msg, soni, raqam)


#49
@dp.message_handler(Text(startswith = '49', ignore_case=True), state = holat.suralar)
async def b49(msg: types.Message, state: FSMContext):
    raqam = 49
    soni = 18
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a49.set()

@dp.message_handler(state = holat.a49)
async def a49(msg: types.Message, state:FSMContext):
    raqam = 49
    soni = 18
    await foroyat(msg, soni, raqam)


#50
@dp.message_handler(Text(startswith = '50', ignore_case=True), state = holat.suralar)
async def b50(msg: types.Message, state: FSMContext):
    raqam = 50
    soni = 45
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a50.set()

@dp.message_handler(state = holat.a50)
async def a50(msg: types.Message, state:FSMContext):
    raqam = 50
    soni = 45
    await foroyat(msg, soni, raqam)


#51
@dp.message_handler(Text(startswith = '51', ignore_case=True), state = holat.suralar)
async def b51(msg: types.Message, state: FSMContext):
    raqam = 51
    soni = 60
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a51.set()

@dp.message_handler(state = holat.a51)
async def a51(msg: types.Message, state:FSMContext):
    raqam = 51
    soni = 60
    await foroyat(msg, soni, raqam)


#52
@dp.message_handler(Text(startswith = '52', ignore_case=True), state = holat.suralar)
async def b52(msg: types.Message, state: FSMContext):
    raqam = 52
    soni = 49
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a52.set()

@dp.message_handler(state = holat.a52)
async def a52(msg: types.Message, state:FSMContext):
    raqam = 52
    soni = 49
    await foroyat(msg, soni, raqam)


#53
@dp.message_handler(Text(startswith = '53', ignore_case=True), state = holat.suralar)
async def b53(msg: types.Message, state: FSMContext):
    raqam = 53
    soni = 62
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a53.set()

@dp.message_handler(state = holat.a53)
async def a53(msg: types.Message, state:FSMContext):
    raqam = 53
    soni = 62
    await foroyat(msg, soni, raqam)


#54
@dp.message_handler(Text(startswith = '54', ignore_case=True), state = holat.suralar)
async def b54(msg: types.Message, state: FSMContext):
    raqam = 54
    soni = 55
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a54.set()

@dp.message_handler(state = holat.a54)
async def a54(msg: types.Message, state:FSMContext):
    raqam = 54
    soni = 55
    await foroyat(msg, soni, raqam)


#55
@dp.message_handler(Text(startswith = '55', ignore_case=True), state = holat.suralar)
async def b55(msg: types.Message, state: FSMContext):
    raqam = 55
    soni = 78
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a55.set()

@dp.message_handler(state = holat.a55)
async def a55(msg: types.Message, state:FSMContext):
    raqam = 55
    soni = 78
    await foroyat(msg, soni, raqam)


#56
@dp.message_handler(Text(startswith = '56', ignore_case=True), state = holat.suralar)
async def b56(msg: types.Message, state: FSMContext):
    raqam = 56
    soni = 96
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a56.set()

@dp.message_handler(state = holat.a56)
async def a56(msg: types.Message, state:FSMContext):
    raqam = 56
    soni = 96
    await foroyat(msg, soni, raqam)


#57
@dp.message_handler(Text(startswith = '57', ignore_case=True), state = holat.suralar)
async def b57(msg: types.Message, state: FSMContext):
    raqam = 57
    soni = 29
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a57.set()

@dp.message_handler(state = holat.a57)
async def a57(msg: types.Message, state:FSMContext):
    raqam = 57
    soni = 29
    await foroyat(msg, soni, raqam)


#58
@dp.message_handler(Text(startswith = '58', ignore_case=True), state = holat.suralar)
async def b58(msg: types.Message, state: FSMContext):
    raqam = 58
    soni = 22
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a58.set()

@dp.message_handler(state = holat.a58)
async def a58(msg: types.Message, state:FSMContext):
    raqam = 58
    soni = 22
    await foroyat(msg, soni, raqam)


#59
@dp.message_handler(Text(startswith = '59', ignore_case=True), state = holat.suralar)
async def b59(msg: types.Message, state: FSMContext):
    raqam = 59
    soni = 24
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a59.set()

@dp.message_handler(state = holat.a59)
async def a59(msg: types.Message, state:FSMContext):
    raqam = 59
    soni = 24
    await foroyat(msg, soni, raqam)


#60
@dp.message_handler(Text(startswith = '60', ignore_case=True), state = holat.suralar)
async def b60(msg: types.Message, state: FSMContext):
    raqam = 60
    soni = 13
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a60.set()

@dp.message_handler(state = holat.a60)
async def a60(msg: types.Message, state:FSMContext):
    raqam = 60
    soni = 13
    await foroyat(msg, soni, raqam)


#61
@dp.message_handler(Text(startswith = '61', ignore_case=True), state = holat.suralar)
async def b61(msg: types.Message, state: FSMContext):
    raqam = 61
    soni = 14
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a61.set()

@dp.message_handler(state = holat.a61)
async def a61(msg: types.Message, state:FSMContext):
    raqam = 61
    soni = 14
    await foroyat(msg, soni, raqam)


#62
@dp.message_handler(Text(startswith = '62', ignore_case=True), state = holat.suralar)
async def b62(msg: types.Message, state: FSMContext):
    raqam = 62
    soni = 11
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a62.set()

@dp.message_handler(state = holat.a62)
async def a62(msg: types.Message, state:FSMContext):
    raqam = 62
    soni = 11
    await foroyat(msg, soni, raqam)


#63
@dp.message_handler(Text(startswith = '63', ignore_case=True), state = holat.suralar)
async def b63(msg: types.Message, state: FSMContext):
    raqam = 63
    soni = 11
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a63.set()

@dp.message_handler(state = holat.a63)
async def a63(msg: types.Message, state:FSMContext):
    raqam = 63
    soni = 11
    await foroyat(msg, soni, raqam)


#64
@dp.message_handler(Text(startswith = '64', ignore_case=True), state = holat.suralar)
async def b64(msg: types.Message, state: FSMContext):
    raqam = 64
    soni = 18
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a64.set()

@dp.message_handler(state = holat.a64)
async def a64(msg: types.Message, state:FSMContext):
    raqam = 64
    soni = 18
    await foroyat(msg, soni, raqam)


#65
@dp.message_handler(Text(startswith = '65', ignore_case=True), state = holat.suralar)
async def b65(msg: types.Message, state: FSMContext):
    raqam = 65
    soni = 12
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a65.set()

@dp.message_handler(state = holat.a65)
async def a65(msg: types.Message, state:FSMContext):
    raqam = 65
    soni = 12
    await foroyat(msg, soni, raqam)


#66
@dp.message_handler(Text(startswith = '66', ignore_case=True), state = holat.suralar)
async def b66(msg: types.Message, state: FSMContext):
    raqam = 66
    soni = 12
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a66.set()

@dp.message_handler(state = holat.a66)
async def a66(msg: types.Message, state:FSMContext):
    raqam = 66
    soni = 12
    await foroyat(msg, soni, raqam)


#67
@dp.message_handler(Text(startswith = '67', ignore_case=True), state = holat.suralar)
async def b67(msg: types.Message, state: FSMContext):
    raqam = 67
    soni = 30
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a67.set()

@dp.message_handler(state = holat.a67)
async def a67(msg: types.Message, state:FSMContext):
    raqam = 67
    soni = 30
    await foroyat(msg, soni, raqam)


#68
@dp.message_handler(Text(startswith = '68', ignore_case=True), state = holat.suralar)
async def b68(msg: types.Message, state: FSMContext):
    raqam = 68
    soni = 52
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a68.set()

@dp.message_handler(state = holat.a68)
async def a68(msg: types.Message, state:FSMContext):
    raqam = 68
    soni = 52
    await foroyat(msg, soni, raqam)


#69
@dp.message_handler(Text(startswith = '69', ignore_case=True), state = holat.suralar)
async def b69(msg: types.Message, state: FSMContext):
    raqam = 69
    soni = 52
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a69.set()

@dp.message_handler(state = holat.a69)
async def a69(msg: types.Message, state:FSMContext):
    raqam = 69
    soni = 52
    await foroyat(msg, soni, raqam)


#70
@dp.message_handler(Text(startswith = '70', ignore_case=True), state = holat.suralar)
async def b70(msg: types.Message, state: FSMContext):
    raqam = 70
    soni = 44
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a70.set()

@dp.message_handler(state = holat.a70)
async def a70(msg: types.Message, state:FSMContext):
    raqam = 70
    soni = 44
    await foroyat(msg, soni, raqam)


#71
@dp.message_handler(Text(startswith = '71', ignore_case=True), state = holat.suralar)
async def b71(msg: types.Message, state: FSMContext):
    raqam = 71
    soni = 28
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a71.set()

@dp.message_handler(state = holat.a71)
async def a71(msg: types.Message, state:FSMContext):
    raqam = 71
    soni = 28
    await foroyat(msg, soni, raqam)


#72
@dp.message_handler(Text(startswith = '72', ignore_case=True), state = holat.suralar)
async def b72(msg: types.Message, state: FSMContext):
    raqam = 72
    soni = 28
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a72.set()

@dp.message_handler(state = holat.a72)
async def a72(msg: types.Message, state:FSMContext):
    raqam = 72
    soni = 28
    await foroyat(msg, soni, raqam)


#73
@dp.message_handler(Text(startswith = '73', ignore_case=True), state = holat.suralar)
async def b73(msg: types.Message, state: FSMContext):
    raqam = 73
    soni = 20
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a73.set()

@dp.message_handler(state = holat.a73)
async def a73(msg: types.Message, state:FSMContext):
    raqam = 73
    soni = 20
    await foroyat(msg, soni, raqam)


#74
@dp.message_handler(Text(startswith = '74', ignore_case=True), state = holat.suralar)
async def b74(msg: types.Message, state: FSMContext):
    raqam = 74
    soni = 56
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a74.set()

@dp.message_handler(state = holat.a74)
async def a74(msg: types.Message, state:FSMContext):
    raqam = 74
    soni = 56
    await foroyat(msg, soni, raqam)


#75
@dp.message_handler(Text(startswith = '75', ignore_case=True), state = holat.suralar)
async def b75(msg: types.Message, state: FSMContext):
    raqam = 75
    soni = 40
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a75.set()

@dp.message_handler(state = holat.a75)
async def a75(msg: types.Message, state:FSMContext):
    raqam = 75
    soni = 40
    await foroyat(msg, soni, raqam)


#76
@dp.message_handler(Text(startswith = '76', ignore_case=True), state = holat.suralar)
async def b76(msg: types.Message, state: FSMContext):
    raqam = 76
    soni = 31
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a76.set()

@dp.message_handler(state = holat.a76)
async def a76(msg: types.Message, state:FSMContext):
    raqam = 76
    soni = 31
    await foroyat(msg, soni, raqam)


#77
@dp.message_handler(Text(startswith = '77', ignore_case=True), state = holat.suralar)
async def b77(msg: types.Message, state: FSMContext):
    raqam = 77
    soni = 50
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a77.set()

@dp.message_handler(state = holat.a77)
async def a77(msg: types.Message, state:FSMContext):
    raqam = 77
    soni = 50
    await foroyat(msg, soni, raqam)


#78
@dp.message_handler(Text(startswith = '78', ignore_case=True), state = holat.suralar)
async def b78(msg: types.Message, state: FSMContext):
    raqam = 78
    soni = 40
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a78.set()

@dp.message_handler(state = holat.a78)
async def a78(msg: types.Message, state:FSMContext):
    raqam = 78
    soni = 40
    await foroyat(msg, soni, raqam)


#79
@dp.message_handler(Text(startswith = '79', ignore_case=True), state = holat.suralar)
async def b79(msg: types.Message, state: FSMContext):
    raqam = 79
    soni = 46
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a79.set()

@dp.message_handler(state = holat.a79)
async def a79(msg: types.Message, state:FSMContext):
    raqam = 79
    soni = 46
    await foroyat(msg, soni, raqam)


#80
@dp.message_handler(Text(startswith = '80', ignore_case=True), state = holat.suralar)
async def b80(msg: types.Message, state: FSMContext):
    raqam = 80
    soni = 42
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a80.set()

@dp.message_handler(state = holat.a80)
async def a80(msg: types.Message, state:FSMContext):
    raqam = 80
    soni = 42
    await foroyat(msg, soni, raqam)


#81
@dp.message_handler(Text(startswith = '81', ignore_case=True), state = holat.suralar)
async def b81(msg: types.Message, state: FSMContext):
    raqam = 81
    soni = 29
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a81.set()

@dp.message_handler(state = holat.a81)
async def a81(msg: types.Message, state:FSMContext):
    raqam = 81
    soni = 29
    await foroyat(msg, soni, raqam)


#82
@dp.message_handler(Text(startswith = '82', ignore_case=True), state = holat.suralar)
async def b82(msg: types.Message, state: FSMContext):
    raqam = 82
    soni = 19
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a82.set()

@dp.message_handler(state = holat.a82)
async def a82(msg: types.Message, state:FSMContext):
    raqam = 82
    soni = 19
    await foroyat(msg, soni, raqam)


#83
@dp.message_handler(Text(startswith = '83', ignore_case=True), state = holat.suralar)
async def b83(msg: types.Message, state: FSMContext):
    raqam = 83
    soni = 36
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a83.set()

@dp.message_handler(state = holat.a83)
async def a83(msg: types.Message, state:FSMContext):
    raqam = 83
    soni = 36
    await foroyat(msg, soni, raqam)


#84
@dp.message_handler(Text(startswith = '84', ignore_case=True), state = holat.suralar)
async def b84(msg: types.Message, state: FSMContext):
    raqam = 84
    soni = 25
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a84.set()

@dp.message_handler(state = holat.a84)
async def a84(msg: types.Message, state:FSMContext):
    raqam = 84
    soni = 25
    await foroyat(msg, soni, raqam)


#85
@dp.message_handler(Text(startswith = '85', ignore_case=True), state = holat.suralar)
async def b85(msg: types.Message, state: FSMContext):
    raqam = 85
    soni = 22
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a85.set()

@dp.message_handler(state = holat.a85)
async def a85(msg: types.Message, state:FSMContext):
    raqam = 85
    soni = 22
    await foroyat(msg, soni, raqam)


#86
@dp.message_handler(Text(startswith = '86', ignore_case=True), state = holat.suralar)
async def b86(msg: types.Message, state: FSMContext):
    raqam = 86
    soni = 17
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a86.set()

@dp.message_handler(state = holat.a86)
async def a86(msg: types.Message, state:FSMContext):
    raqam = 86
    soni = 17
    await foroyat(msg, soni, raqam)


#87
@dp.message_handler(Text(startswith = '87', ignore_case=True), state = holat.suralar)
async def b87(msg: types.Message, state: FSMContext):
    raqam = 87
    soni = 19
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a87.set()

@dp.message_handler(state = holat.a87)
async def a87(msg: types.Message, state:FSMContext):
    raqam = 87
    soni = 19
    await foroyat(msg, soni, raqam)


#88
@dp.message_handler(Text(startswith = '88', ignore_case=True), state = holat.suralar)
async def b88(msg: types.Message, state: FSMContext):
    raqam = 88
    soni = 26
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a88.set()

@dp.message_handler(state = holat.a88)
async def a88(msg: types.Message, state:FSMContext):
    raqam = 88
    soni = 26
    await foroyat(msg, soni, raqam)


#89
@dp.message_handler(Text(startswith = '89', ignore_case=True), state = holat.suralar)
async def b89(msg: types.Message, state: FSMContext):
    raqam = 89
    soni = 30
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a89.set()

@dp.message_handler(state = holat.a89)
async def a89(msg: types.Message, state:FSMContext):
    raqam = 89
    soni = 30
    await foroyat(msg, soni, raqam)


#90
@dp.message_handler(Text(startswith = '90', ignore_case=True), state = holat.suralar)
async def b90(msg: types.Message, state: FSMContext):
    raqam = 90
    soni = 20
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a90.set()

@dp.message_handler(state = holat.a90)
async def a90(msg: types.Message, state:FSMContext):
    raqam = 90
    soni = 20
    await foroyat(msg, soni, raqam)


#91
@dp.message_handler(Text(startswith = '91', ignore_case=True), state = holat.suralar)
async def b91(msg: types.Message, state: FSMContext):
    raqam = 91
    soni = 15
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a91.set()

@dp.message_handler(state = holat.a91)
async def a91(msg: types.Message, state:FSMContext):
    raqam = 91
    soni = 15
    await foroyat(msg, soni, raqam)


#92
@dp.message_handler(Text(startswith = '92', ignore_case=True), state = holat.suralar)
async def b92(msg: types.Message, state: FSMContext):
    raqam = 92
    soni = 21
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a92.set()

@dp.message_handler(state = holat.a92)
async def a92(msg: types.Message, state:FSMContext):
    raqam = 92
    soni = 21
    await foroyat(msg, soni, raqam)


#93
@dp.message_handler(Text(startswith = '93', ignore_case=True), state = holat.suralar)
async def b93(msg: types.Message, state: FSMContext):
    raqam = 93
    soni = 11
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a93.set()

@dp.message_handler(state = holat.a93)
async def a93(msg: types.Message, state:FSMContext):
    raqam = 93
    soni = 11
    await foroyat(msg, soni, raqam)


#94
@dp.message_handler(Text(startswith = '94', ignore_case=True), state = holat.suralar)
async def b94(msg: types.Message, state: FSMContext):
    raqam = 94
    soni = 8
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a94.set()

@dp.message_handler(state = holat.a94)
async def a94(msg: types.Message, state:FSMContext):
    raqam = 94
    soni = 8
    await foroyat(msg, soni, raqam)


#95
@dp.message_handler(Text(startswith = '95', ignore_case=True), state = holat.suralar)
async def b95(msg: types.Message, state: FSMContext):
    raqam = 95
    soni = 8
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a95.set()

@dp.message_handler(state = holat.a95)
async def a95(msg: types.Message, state:FSMContext):
    raqam = 95
    soni = 8
    await foroyat(msg, soni, raqam)


#96
@dp.message_handler(Text(startswith = '96', ignore_case=True), state = holat.suralar)
async def b96(msg: types.Message, state: FSMContext):
    raqam = 96
    soni = 19
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a96.set()

@dp.message_handler(state = holat.a96)
async def a96(msg: types.Message, state:FSMContext):
    raqam = 96
    soni = 19
    await foroyat(msg, soni, raqam)


#97
@dp.message_handler(Text(startswith = '97', ignore_case=True), state = holat.suralar)
async def b97(msg: types.Message, state: FSMContext):
    raqam = 97
    soni = 5
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a97.set()

@dp.message_handler(state = holat.a97)
async def a97(msg: types.Message, state:FSMContext):
    raqam = 97
    soni = 5
    await foroyat(msg, soni, raqam)


#98
@dp.message_handler(Text(startswith = '98', ignore_case=True), state = holat.suralar)
async def b98(msg: types.Message, state: FSMContext):
    raqam = 98
    soni = 8
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a98.set()

@dp.message_handler(state = holat.a98)
async def a98(msg: types.Message, state:FSMContext):
    raqam = 98
    soni = 8
    await foroyat(msg, soni, raqam)


#99
@dp.message_handler(Text(startswith = '99', ignore_case=True), state = holat.suralar)
async def b99(msg: types.Message, state: FSMContext):
    raqam = 99
    soni = 8
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a99.set()

@dp.message_handler(state = holat.a99)
async def a99(msg: types.Message, state:FSMContext):
    raqam = 99
    soni = 8
    await foroyat(msg, soni, raqam)


#100
@dp.message_handler(Text(startswith = '100', ignore_case=True), state = holat.suralar)
async def b100(msg: types.Message, state: FSMContext):
    raqam = 100
    soni = 11
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a100.set()

@dp.message_handler(state = holat.a100)
async def a100(msg: types.Message, state:FSMContext):
    raqam = 100
    soni = 11
    await foroyat(msg, soni, raqam)


#101
@dp.message_handler(Text(startswith = '101', ignore_case=True), state = holat.suralar)
async def b101(msg: types.Message, state: FSMContext):
    raqam = 101
    soni = 11
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a101.set()

@dp.message_handler(state = holat.a101)
async def a101(msg: types.Message, state:FSMContext):
    raqam = 101
    soni = 11
    await foroyat(msg, soni, raqam)


#102
@dp.message_handler(Text(startswith = '102', ignore_case=True), state = holat.suralar)
async def b102(msg: types.Message, state: FSMContext):
    raqam = 102
    soni = 8
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a102.set()

@dp.message_handler(state = holat.a102)
async def a102(msg: types.Message, state:FSMContext):
    raqam = 102
    soni = 8
    await foroyat(msg, soni, raqam)


#103
@dp.message_handler(Text(startswith = '103', ignore_case=True), state = holat.suralar)
async def b103(msg: types.Message, state: FSMContext):
    raqam = 103
    soni = 3
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a103.set()

@dp.message_handler(state = holat.a103)
async def a103(msg: types.Message, state:FSMContext):
    raqam = 103
    soni = 3
    await foroyat(msg, soni, raqam)


#104
@dp.message_handler(Text(startswith = '104', ignore_case=True), state = holat.suralar)
async def b104(msg: types.Message, state: FSMContext):
    raqam = 104
    soni = 9
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a104.set()

@dp.message_handler(state = holat.a104)
async def a104(msg: types.Message, state:FSMContext):
    raqam = 104
    soni = 9
    await foroyat(msg, soni, raqam)


#105
@dp.message_handler(Text(startswith = '105', ignore_case=True), state = holat.suralar)
async def b105(msg: types.Message, state: FSMContext):
    raqam = 105
    soni = 5
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a105.set()

@dp.message_handler(state = holat.a105)
async def a105(msg: types.Message, state:FSMContext):
    raqam = 105
    soni = 5
    await foroyat(msg, soni, raqam)


#106
@dp.message_handler(Text(startswith = '106', ignore_case=True), state = holat.suralar)
async def b106(msg: types.Message, state: FSMContext):
    raqam = 106
    soni = 4
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a106.set()

@dp.message_handler(state = holat.a106)
async def a106(msg: types.Message, state:FSMContext):
    raqam = 106
    soni = 4
    await foroyat(msg, soni, raqam)


#107
@dp.message_handler(Text(startswith = '107', ignore_case=True), state = holat.suralar)
async def b107(msg: types.Message, state: FSMContext):
    raqam = 107
    soni = 7
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a107.set()

@dp.message_handler(state = holat.a107)
async def a107(msg: types.Message, state:FSMContext):
    raqam = 107
    soni = 7
    await foroyat(msg, soni, raqam)


#108
@dp.message_handler(Text(startswith = '108', ignore_case=True), state = holat.suralar)
async def b108(msg: types.Message, state: FSMContext):
    raqam = 108
    soni = 3
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a108.set()

@dp.message_handler(state = holat.a108)
async def a108(msg: types.Message, state:FSMContext):
    raqam = 108
    soni = 3
    await foroyat(msg, soni, raqam)


#109
@dp.message_handler(Text(startswith = '109', ignore_case=True), state = holat.suralar)
async def b109(msg: types.Message, state: FSMContext):
    raqam = 109
    soni = 6
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a109.set()

@dp.message_handler(state = holat.a109)
async def a109(msg: types.Message, state:FSMContext):
    raqam = 109
    soni = 6
    await foroyat(msg, soni, raqam)


#110
@dp.message_handler(Text(startswith = '110', ignore_case=True), state = holat.suralar)
async def b110(msg: types.Message, state: FSMContext):
    raqam = 110
    soni = 3
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a110.set()

@dp.message_handler(state = holat.a110)
async def a110(msg: types.Message, state:FSMContext):
    raqam = 110
    soni = 3
    await foroyat(msg, soni, raqam)


#111
@dp.message_handler(Text(startswith = '111', ignore_case=True), state = holat.suralar)
async def b111(msg: types.Message, state: FSMContext):
    raqam = 111
    soni = 5
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a111.set()

@dp.message_handler(state = holat.a111)
async def a111(msg: types.Message, state:FSMContext):
    raqam = 111
    soni = 5
    await foroyat(msg, soni, raqam)


#112
@dp.message_handler(Text(startswith = '112', ignore_case=True), state = holat.suralar)
async def b112(msg: types.Message, state: FSMContext):
    raqam = 112
    soni = 4
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a112.set()

@dp.message_handler(state = holat.a112)
async def a112(msg: types.Message, state:FSMContext):
    raqam = 112
    soni = 4
    await foroyat(msg, soni, raqam)


#113
@dp.message_handler(Text(startswith = '113', ignore_case=True), state = holat.suralar)
async def b113(msg: types.Message, state: FSMContext):
    raqam = 113
    soni = 5
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a113.set()

@dp.message_handler(state = holat.a113)
async def a113(msg: types.Message, state:FSMContext):
    raqam = 113
    soni = 5
    await foroyat(msg, soni, raqam)


#114
@dp.message_handler(Text(startswith = '114', ignore_case=True), state = holat.suralar)
async def b114(msg: types.Message, state: FSMContext):
    raqam = 114
    soni = 6
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a114.set()

@dp.message_handler(state = holat.a114)
async def a114(msg: types.Message, state:FSMContext):
    raqam = 114
    soni = 6
    await foroyat(msg, soni, raqam)




#2
@dp.message_handler(Text(startswith = '2', ignore_case=True), state = holat.suralar)
async def b2(msg: types.Message, state: FSMContext):
    raqam = 2
    soni = 286
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a2.set()

@dp.message_handler(state = holat.a2)
async def a2(msg: types.Message, state:FSMContext):
    raqam = 2
    soni = 286
    await foroyat(msg, soni, raqam)


#3
@dp.message_handler(Text(startswith = '3', ignore_case=True), state = holat.suralar)
async def b3(msg: types.Message, state: FSMContext):
    raqam = 3
    soni = 200
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a3.set()

@dp.message_handler(state = holat.a3)
async def a3(msg: types.Message, state:FSMContext):
    raqam = 3
    soni = 200
    await foroyat(msg, soni, raqam)


#4
@dp.message_handler(Text(startswith = '4', ignore_case=True), state = holat.suralar)
async def b4(msg: types.Message, state: FSMContext):
    raqam = 4
    soni = 176
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a4.set()

@dp.message_handler(state = holat.a4)
async def a4(msg: types.Message, state:FSMContext):
    raqam = 4
    soni = 176
    await foroyat(msg, soni, raqam)


#5
@dp.message_handler(Text(startswith = '5', ignore_case=True), state = holat.suralar)
async def b5(msg: types.Message, state: FSMContext):
    raqam = 5
    soni = 120
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a5.set()

@dp.message_handler(state = holat.a5)
async def a5(msg: types.Message, state:FSMContext):
    raqam = 5
    soni = 120
    await foroyat(msg, soni, raqam)


#6
@dp.message_handler(Text(startswith = '6', ignore_case=True), state = holat.suralar)
async def b6(msg: types.Message, state: FSMContext):
    raqam = 6
    soni = 165
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a6.set()

@dp.message_handler(state = holat.a6)
async def a6(msg: types.Message, state:FSMContext):
    raqam = 6
    soni = 165
    await foroyat(msg, soni, raqam)


#7
@dp.message_handler(Text(startswith = '7', ignore_case=True), state = holat.suralar)
async def b7(msg: types.Message, state: FSMContext):
    raqam = 7
    soni = 206
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a7.set()

@dp.message_handler(state = holat.a7)
async def a7(msg: types.Message, state:FSMContext):
    raqam = 7
    soni = 206
    await foroyat(msg, soni, raqam)


#8
@dp.message_handler(Text(startswith = '8', ignore_case=True), state = holat.suralar)
async def b8(msg: types.Message, state: FSMContext):
    raqam = 8
    soni = 75
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a8.set()

@dp.message_handler(state = holat.a8)
async def a8(msg: types.Message, state:FSMContext):
    raqam = 8
    soni = 75
    await foroyat(msg, soni, raqam)


#9
@dp.message_handler(Text(startswith = '9', ignore_case=True), state = holat.suralar)
async def b9(msg: types.Message, state: FSMContext):
    raqam = 9
    soni = 129
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a9.set()

@dp.message_handler(state = holat.a9)
async def a9(msg: types.Message, state:FSMContext):
    raqam = 9
    soni = 129
    await foroyat(msg, soni, raqam)


#10
@dp.message_handler(Text(startswith = '10', ignore_case=True), state = holat.suralar)
async def b10(msg: types.Message, state: FSMContext):
    raqam = 10
    soni = 109
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a10.set()

@dp.message_handler(state = holat.a10)
async def a10(msg: types.Message, state:FSMContext):
    raqam = 10
    soni = 109
    await foroyat(msg, soni, raqam)


#11
@dp.message_handler(Text(startswith = '11', ignore_case=True), state = holat.suralar)
async def b11(msg: types.Message, state: FSMContext):
    raqam = 11
    soni = 123
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a11.set()

@dp.message_handler(state = holat.a11)
async def a11(msg: types.Message, state:FSMContext):
    raqam = 11
    soni = 123
    await foroyat(msg, soni, raqam)

#1
@dp.message_handler(Text(startswith = '1', ignore_case=True), state = holat.suralar)
async def b1(msg: types.Message, state: FSMContext):
    raqam = 1
    soni = 7
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a1.set()

@dp.message_handler(state = holat.a1)
async def a1(msg: types.Message, state:FSMContext):
    raqam = 1
    soni = 7
    await foroyat(msg, soni, raqam)

