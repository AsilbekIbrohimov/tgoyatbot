from fuzzywuzzy import fuzz
from loader import dp
from aiogram import types
from data.suralist import suralist
from states.searcherState import AyahSearch as holat
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard, mainAndbackKeyboard
from.ForOyatHandler import answertext

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[0].lower()) > 80, state = holat.suralar)
async def c1(msg: types.Message):
    raqam = 1
    soni = 7
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a1.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[1].lower()) > 80, state = holat.suralar)
async def c2(msg: types.Message):
    raqam = 2
    soni = 286
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a2.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[2].lower()) > 80, state = holat.suralar)
async def c3(msg: types.Message):
    raqam = 3
    soni = 200
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a3.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[3].lower()) > 80, state = holat.suralar)
async def c4(msg: types.Message):
    raqam = 4
    soni = 176
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a4.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[4].lower()) > 80, state = holat.suralar)
async def c5(msg: types.Message):
    raqam = 5
    soni = 120
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a5.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[5].lower()) > 80, state = holat.suralar)
async def c6(msg: types.Message):
    raqam = 6
    soni = 165
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a6.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[6].lower()) > 80, state = holat.suralar)
async def c7(msg: types.Message):
    raqam = 7
    soni = 206
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a7.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[7].lower()) > 80, state = holat.suralar)
async def c8(msg: types.Message):
    raqam = 8
    soni = 75
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a8.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[8].lower()) > 80, state = holat.suralar)
async def c9(msg: types.Message):
    raqam = 9
    soni = 129
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a9.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[9].lower()) > 80, state = holat.suralar)
async def c10(msg: types.Message):
    raqam = 10
    soni = 109
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a10.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[10].lower()) > 80, state = holat.suralar)
async def c11(msg: types.Message):
    raqam = 11
    soni = 123
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a11.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[11].lower()) > 80, state = holat.suralar)
async def c12(msg: types.Message):
    raqam = 12
    soni = 111
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a12.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[12].lower()) > 80, state = holat.suralar)
async def c13(msg: types.Message):
    raqam = 13
    soni = 43
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a13.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[13].lower()) > 80, state = holat.suralar)
async def c14(msg: types.Message):
    raqam = 14
    soni = 52
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a14.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[14].lower()) > 80, state = holat.suralar)
async def c15(msg: types.Message):
    raqam = 15
    soni = 99
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a15.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[15].lower()) > 80, state = holat.suralar)
async def c16(msg: types.Message):
    raqam = 16
    soni = 128
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a16.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[16].lower()) > 80, state = holat.suralar)
async def c17(msg: types.Message):
    raqam = 17
    soni = 111
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a17.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[17].lower()) > 80, state = holat.suralar)
async def c18(msg: types.Message):
    raqam = 18
    soni = 110
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a18.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[18].lower()) > 80, state = holat.suralar)
async def c19(msg: types.Message):
    raqam = 19
    soni = 98
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a19.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[19].lower()) > 80, state = holat.suralar)
async def c20(msg: types.Message):
    raqam = 20
    soni = 135
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a20.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[20].lower()) > 80, state = holat.suralar)
async def c21(msg: types.Message):
    raqam = 21
    soni = 112
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a21.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[21].lower()) > 80, state = holat.suralar)
async def c22(msg: types.Message):
    raqam = 22
    soni = 78
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a22.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[22].lower()) > 80, state = holat.suralar)
async def c23(msg: types.Message):
    raqam = 23
    soni = 118
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a23.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[23].lower()) > 80, state = holat.suralar)
async def c24(msg: types.Message):
    raqam = 24
    soni = 64
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a24.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[24].lower()) > 80, state = holat.suralar)
async def c25(msg: types.Message):
    raqam = 25
    soni = 77
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a25.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[25].lower()) > 80, state = holat.suralar)
async def c26(msg: types.Message):
    raqam = 26
    soni = 227
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a26.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[26].lower()) > 80, state = holat.suralar)
async def c27(msg: types.Message):
    raqam = 27
    soni = 93
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a27.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[27].lower()) > 80, state = holat.suralar)
async def c28(msg: types.Message):
    raqam = 28
    soni = 88
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a28.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[28].lower()) > 80, state = holat.suralar)
async def c29(msg: types.Message):
    raqam = 29
    soni = 69
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a29.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[29].lower()) > 80, state = holat.suralar)
async def c30(msg: types.Message):
    raqam = 30
    soni = 60
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a30.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[30].lower()) > 80, state = holat.suralar)
async def c31(msg: types.Message):
    raqam = 31
    soni = 34
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a31.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[31].lower()) > 80, state = holat.suralar)
async def c32(msg: types.Message):
    raqam = 32
    soni = 30
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a32.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[32].lower()) > 80, state = holat.suralar)
async def c33(msg: types.Message):
    raqam = 33
    soni = 73
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a33.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[33].lower()) > 80, state = holat.suralar)
async def c34(msg: types.Message):
    raqam = 34
    soni = 54
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a34.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[34].lower()) > 80, state = holat.suralar)
async def c35(msg: types.Message):
    raqam = 35
    soni = 45
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a35.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[35].lower()) > 80, state = holat.suralar)
async def c36(msg: types.Message):
    raqam = 36
    soni = 83
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a36.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[36].lower()) > 80, state = holat.suralar)
async def c37(msg: types.Message):
    raqam = 37
    soni = 182
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a37.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[37].lower()) > 80, state = holat.suralar)
async def c38(msg: types.Message):
    raqam = 38
    soni = 88
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a38.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[38].lower()) > 80, state = holat.suralar)
async def c39(msg: types.Message):
    raqam = 39
    soni = 75
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a39.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[39].lower()) > 80, state = holat.suralar)
async def c40(msg: types.Message):
    raqam = 40
    soni = 85
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a40.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[40].lower()) > 80, state = holat.suralar)
async def c41(msg: types.Message):
    raqam = 41
    soni = 54
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a41.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[41].lower()) > 80, state = holat.suralar)
async def c42(msg: types.Message):
    raqam = 42
    soni = 53
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a42.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[42].lower()) > 80, state = holat.suralar)
async def c43(msg: types.Message):
    raqam = 43
    soni = 89
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a43.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[43].lower()) > 80, state = holat.suralar)
async def c44(msg: types.Message):
    raqam = 44
    soni = 59
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a44.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[44].lower()) > 80, state = holat.suralar)
async def c45(msg: types.Message):
    raqam = 45
    soni = 37
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a45.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[45].lower()) > 80, state = holat.suralar)
async def c46(msg: types.Message):
    raqam = 46
    soni = 35
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a46.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[46].lower()) > 80, state = holat.suralar)
async def c47(msg: types.Message):
    raqam = 47
    soni = 38
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a47.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[47].lower()) > 80, state = holat.suralar)
async def c48(msg: types.Message):
    raqam = 48
    soni = 29
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a48.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[48].lower()) > 80, state = holat.suralar)
async def c49(msg: types.Message):
    raqam = 49
    soni = 18
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a49.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[49].lower()) > 80, state = holat.suralar)
async def c50(msg: types.Message):
    raqam = 50
    soni = 45
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a50.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[50].lower()) > 80, state = holat.suralar)
async def c51(msg: types.Message):
    raqam = 51
    soni = 60
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a51.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[51].lower()) > 80, state = holat.suralar)
async def c52(msg: types.Message):
    raqam = 52
    soni = 49
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a52.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[52].lower()) > 80, state = holat.suralar)
async def c53(msg: types.Message):
    raqam = 53
    soni = 62
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a53.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[53].lower()) > 80, state = holat.suralar)
async def c54(msg: types.Message):
    raqam = 54
    soni = 55
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a54.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[54].lower()) > 80, state = holat.suralar)
async def c55(msg: types.Message):
    raqam = 55
    soni = 78
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a55.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[55].lower()) > 80, state = holat.suralar)
async def c56(msg: types.Message):
    raqam = 56
    soni = 96
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a56.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[56].lower()) > 80, state = holat.suralar)
async def c57(msg: types.Message):
    raqam = 57
    soni = 29
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a57.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[57].lower()) > 80, state = holat.suralar)
async def c58(msg: types.Message):
    raqam = 58
    soni = 22
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a58.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[58].lower()) > 80, state = holat.suralar)
async def c59(msg: types.Message):
    raqam = 59
    soni = 24
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a59.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[59].lower()) > 80, state = holat.suralar)
async def c60(msg: types.Message):
    raqam = 60
    soni = 13
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a60.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[60].lower()) > 80, state = holat.suralar)
async def c61(msg: types.Message):
    raqam = 61
    soni = 14
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a61.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[61].lower()) > 80, state = holat.suralar)
async def c62(msg: types.Message):
    raqam = 62
    soni = 11
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a62.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[62].lower()) > 80, state = holat.suralar)
async def c63(msg: types.Message):
    raqam = 63
    soni = 11
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a63.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[63].lower()) > 80, state = holat.suralar)
async def c64(msg: types.Message):
    raqam = 64
    soni = 18
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a64.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[64].lower()) > 80, state = holat.suralar)
async def c65(msg: types.Message):
    raqam = 65
    soni = 12
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a65.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[65].lower()) > 80, state = holat.suralar)
async def c66(msg: types.Message):
    raqam = 66
    soni = 12
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a66.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[66].lower()) > 80, state = holat.suralar)
async def c67(msg: types.Message):
    raqam = 67
    soni = 30
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a67.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[67].lower()) > 80, state = holat.suralar)
async def c68(msg: types.Message):
    raqam = 68
    soni = 52
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a68.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[68].lower()) > 80, state = holat.suralar)
async def c69(msg: types.Message):
    raqam = 69
    soni = 52
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a69.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[69].lower()) > 80, state = holat.suralar)
async def c70(msg: types.Message):
    raqam = 70
    soni = 44
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a70.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[70].lower()) > 80, state = holat.suralar)
async def c71(msg: types.Message):
    raqam = 71
    soni = 28
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a71.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[71].lower()) > 80, state = holat.suralar)
async def c72(msg: types.Message):
    raqam = 72
    soni = 28
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a72.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[72].lower()) > 80, state = holat.suralar)
async def c73(msg: types.Message):
    raqam = 73
    soni = 20
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a73.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[73].lower()) > 80, state = holat.suralar)
async def c74(msg: types.Message):
    raqam = 74
    soni = 56
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a74.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[74].lower()) > 80, state = holat.suralar)
async def c75(msg: types.Message):
    raqam = 75
    soni = 40
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a75.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[75].lower()) > 80, state = holat.suralar)
async def c76(msg: types.Message):
    raqam = 76
    soni = 31
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a76.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[76].lower()) > 80, state = holat.suralar)
async def c77(msg: types.Message):
    raqam = 77
    soni = 50
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a77.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[77].lower()) > 80, state = holat.suralar)
async def c78(msg: types.Message):
    raqam = 78
    soni = 40
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a78.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[78].lower()) > 80, state = holat.suralar)
async def c79(msg: types.Message):
    raqam = 79
    soni = 46
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a79.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[79].lower()) > 80, state = holat.suralar)
async def c80(msg: types.Message):
    raqam = 80
    soni = 42
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a80.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[80].lower()) > 80, state = holat.suralar)
async def c81(msg: types.Message):
    raqam = 81
    soni = 29
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a81.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[81].lower()) > 80, state = holat.suralar)
async def c82(msg: types.Message):
    raqam = 82
    soni = 19
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a82.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[82].lower()) > 80, state = holat.suralar)
async def c83(msg: types.Message):
    raqam = 83
    soni = 36
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a83.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[83].lower()) > 80, state = holat.suralar)
async def c84(msg: types.Message):
    raqam = 84
    soni = 25
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a84.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[84].lower()) > 80, state = holat.suralar)
async def c85(msg: types.Message):
    raqam = 85
    soni = 22
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a85.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[85].lower()) > 80, state = holat.suralar)
async def c86(msg: types.Message):
    raqam = 86
    soni = 17
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a86.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[86].lower()) > 80, state = holat.suralar)
async def c87(msg: types.Message):
    raqam = 87
    soni = 19
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a87.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[87].lower()) > 80, state = holat.suralar)
async def c88(msg: types.Message):
    raqam = 88
    soni = 26
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a88.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[88].lower()) > 80, state = holat.suralar)
async def c89(msg: types.Message):
    raqam = 89
    soni = 30
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a89.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[89].lower()) > 80, state = holat.suralar)
async def c90(msg: types.Message):
    raqam = 90
    soni = 20
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a90.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[90].lower()) > 80, state = holat.suralar)
async def c91(msg: types.Message):
    raqam = 91
    soni = 15
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a91.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[91].lower()) > 80, state = holat.suralar)
async def c92(msg: types.Message):
    raqam = 92
    soni = 21
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a92.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[92].lower()) > 80, state = holat.suralar)
async def c93(msg: types.Message):
    raqam = 93
    soni = 11
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a93.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[93].lower()) > 80, state = holat.suralar)
async def c94(msg: types.Message):
    raqam = 94
    soni = 8
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a94.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[94].lower()) > 80, state = holat.suralar)
async def c95(msg: types.Message):
    raqam = 95
    soni = 8
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a95.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[95].lower()) > 80, state = holat.suralar)
async def c96(msg: types.Message):
    raqam = 96
    soni = 19
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a96.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[96].lower()) > 80, state = holat.suralar)
async def c97(msg: types.Message):
    raqam = 97
    soni = 5
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a97.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[97].lower()) > 80, state = holat.suralar)
async def c98(msg: types.Message):
    raqam = 98
    soni = 8
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a98.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[98].lower()) > 80, state = holat.suralar)
async def c99(msg: types.Message):
    raqam = 99
    soni = 8
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a99.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[99].lower()) > 80, state = holat.suralar)
async def c100(msg: types.Message):
    raqam = 100
    soni = 11
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a100.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[100].lower()) > 80, state = holat.suralar)
async def c101(msg: types.Message):
    raqam = 101
    soni = 11
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a101.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[101].lower()) > 80, state = holat.suralar)
async def c102(msg: types.Message):
    raqam = 102
    soni = 8
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a102.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[102].lower()) > 80, state = holat.suralar)
async def c103(msg: types.Message):
    raqam = 103
    soni = 3
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a103.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[103].lower()) > 80, state = holat.suralar)
async def c104(msg: types.Message):
    raqam = 104
    soni = 9
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a104.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[104].lower()) > 80, state = holat.suralar)
async def c105(msg: types.Message):
    raqam = 105
    soni = 5
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a105.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[105].lower()) > 80, state = holat.suralar)
async def c106(msg: types.Message):
    raqam = 106
    soni = 4
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a106.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[106].lower()) > 80, state = holat.suralar)
async def c107(msg: types.Message):
    raqam = 107
    soni = 7
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a107.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[107].lower()) > 80, state = holat.suralar)
async def c108(msg: types.Message):
    raqam = 108
    soni = 3
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a108.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[108].lower()) > 80, state = holat.suralar)
async def c109(msg: types.Message):
    raqam = 109
    soni = 6
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a109.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[109].lower()) > 80, state = holat.suralar)
async def c110(msg: types.Message):
    raqam = 110
    soni = 3
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a110.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[110].lower()) > 80, state = holat.suralar)
async def c111(msg: types.Message):
    raqam = 111
    soni = 5
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a111.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[111].lower()) > 80, state = holat.suralar)
async def c112(msg: types.Message):
    raqam = 112
    soni = 4
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a112.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[112].lower()) > 80, state = holat.suralar)
async def c113(msg: types.Message):
    raqam = 113
    soni = 5
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a113.set()

@dp.message_handler(lambda msg: fuzz.ratio(msg.text.lower(), suralist[113].lower()) > 80, state = holat.suralar)
async def c114(msg: types.Message):
    raqam = 114
    soni = 6
    await msg.answer(answertext(soni, raqam), reply_markup=mainAndbackKeyboard)
    await holat.a114.set()

