from data.config import BOT_ID, TELEGRAM_SUPPORT_CHAT_ID
from aiogram.types import ContentType
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot, db2
from data.config import ADMINS
from keyboards.default.forstartKeyboard import startKeyboard
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard
from aiogram.utils.exceptions import BotKicked, BotBlocked, UserDeactivated
from .startHandler import bot_start
from filters.group_chat import IsGroup


@dp.message_handler(state='feedback', content_types=ContentType.ANY)
async def question_text(message: types.Message, state: FSMContext):
    if message.text == mainMenuKeyboard.keyboard[0][0].text:
        await bot_start(message, state)
    else:
        await bot.send_message(chat_id=TELEGRAM_SUPPORT_CHAT_ID, text = f" {message.from_user.get_mention(as_html=True)} xabar yubordi")
        get_id  = await message.forward(TELEGRAM_SUPPORT_CHAT_ID)
        await message.answer('Xabar yuborildi', reply_markup=startKeyboard)
        db2.add_message(message_id=get_id.message_id, user_id = message.from_user.id)
    await state.finish()
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsQuestion(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        try:
            return bool(str(message.reply_to_message.from_user.id) in BOT_ID and (message.reply_to_message.forward_from or message.reply_to_message.forward_sender_name))
        except:
            return False
"""lambda msg: msg.reply_to_message.from_user.id in BOT_ID and (msg.reply_to_message.forward_from or msg.reply_to_message.forward_sender_name)"""

@dp.message_handler(IsGroup(),IsQuestion(),chat_id = TELEGRAM_SUPPORT_CHAT_ID, content_types=ContentType.ANY)
async def echo(message: types.Message):
    try:
        await bot.send_message(chat_id=db2.select_message(message_id = message.reply_to_message.message_id)[1], text = f"Admin xabaringizga javob qaytardi\n\n{message.reply_to_message.text}")
        await bot.copy_message(chat_id=db2.select_message(message_id = message.reply_to_message.message_id)[1], from_chat_id=message.chat.id, message_id=message.message_id)
        
        await message.reply('SUCCESS_ANSWER_TEXT')
    except (BotKicked, BotBlocked, UserDeactivated):
        await message.answer('USER_DEACTIVATED')