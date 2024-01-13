from data.config import ADMINS
from loader import bot
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp, db
from keyboards.default.forstartKeyboard import startKeyboard
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard
from data.config import ADMINS
from aiogram.dispatcher.filters.builtin import CommandStart
from data.suralist import suralist

# @dp.message_handler(lambda message: message.text.capitalize() in suralist)
# async def start_message(message: types.Message):
#     await message.answer("Выберите нужный вам вариант")

async def reklama(message: types.Message):
    args = message.get_args()
    mention = message.from_user.get_mention(as_html=True)
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        count = db.count_users()[0]
        try:
            username = message.from_user.username
        except:
            username = ''
        msg = f"{mention} {username} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor.\nAds code {args}"
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    except Exception as err:
        pass

    await message.answer(f"Assalomu alaykum {name}! Botga xush kelibsiz", reply_markup=startKeyboard)



@dp.message_handler(CommandStart(deep_link='1001'))
async def relama1(message: types.Message):
    await reklama(message)


@dp.message_handler(CommandStart(deep_link='1002'))
async def relama2(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1003'))
async def relama3(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1004'))
async def relama4(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1005'))
async def relama5(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1006'))
async def relama6(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1007'))
async def relama7(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1008'))
async def relama8(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1009'))
async def relama9(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1010'))
async def relama10(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1011'))
async def relama11(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1012'))
async def relama12(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1013'))
async def relama13(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1014'))
async def relama14(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1015'))
async def relama15(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1016'))
async def relama16(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1017'))
async def relama17(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1018'))
async def relama18(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1019'))
async def relama19(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1020'))
async def relama20(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1021'))
async def relama21(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1022'))
async def relama22(message: types.Message):
    await reklama(message)

@dp.message_handler(CommandStart(deep_link='1023'))
async def relama23(message: types.Message):
    await reklama(message)



@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    mention = message.from_user.get_mention(as_html=True)
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        count = db.count_users()[0]
        try:
            username = message.from_user.username
        except:
            username = ''
        msg = f"{mention} {username} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    except Exception as err:
        pass

    await message.answer(f"Assalomu alaykum {message.from_user.full_name}! Botga xush kelibsiz", reply_markup=startKeyboard)
    await state.finish()
