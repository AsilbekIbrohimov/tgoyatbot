from data.suralist import suralist
from data.qurandict import qurandict
from data.qurandict2 import qurandict2
from aiogram.types import Message
from utils import get_link
from loader import dp, db

async def array(txt) -> list:
    arr = []
    if ' ' in txt:
        arr = list(txt.split())
    elif '-' in txt:
        arr = list(txt.split('-'))
    elif ':' in txt:
        arr = list(txt.split(':'))
    return arr
async def reg(txt, trans):
    quran = {}
    if not trans:
        quran = qurandict
    else:
        quran = qurandict2
    arr = await array(txt)
    return f"{suralist[int(arr[0])-1]} surasi {arr[1]}-oyat\n\n{quran[arr[0]][int(arr[1])-1]['text']}"


@dp.message_handler(regexp="^[\d]{1,3}[: ][\d]{1,3}$", state = '*')
async def regex(msg: Message):

    try:
        await msg.reply(f"{await reg(msg.text, db.select_user(id = msg.from_user.id)[4])}{await get_link((await array(msg.text))[0], (await array(msg.text))[1])}")
    except IndexError:
        if int((await array(msg.text))[0]) > 114:
            await msg.reply('Sura raqami noto\'g\'ri kiritildi')
        else:
            await msg.reply("Oyat raqami noto\'g\'ri kiritildi")