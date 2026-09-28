from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest

from loader import bot, db2
from data.config import TELEGRAM_SUPPORT_CHAT_ID
from states.adminState import Feedback
from keyboards.default.forstartKeyboard import startKeyboard
from filters.group_chat import IsGroup

feedback_router = Router()


@feedback_router.message(Feedback.waiting)
async def receive_feedback(message: Message, state: FSMContext):
    # (Asosiy Menyu tugmasi global handlerda ushlanadi)
    await bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=f"{message.from_user.mention_html()} xabar yubordi",
    )
    forwarded = await message.forward(TELEGRAM_SUPPORT_CHAT_ID)
    db2.add_message(message_id=forwarded.message_id, user_id=message.from_user.id)
    await message.answer('Xabar yuborildi', reply_markup=startKeyboard)
    await state.clear()


@feedback_router.message(
    IsGroup(),
    F.chat.id == TELEGRAM_SUPPORT_CHAT_ID,
    F.reply_to_message,
)
async def admin_reply(message: Message):
    mapping = db2.select_message(message_id=message.reply_to_message.message_id)
    if not mapping:
        return  # bu javob bot yuborgan savolga emas
    user_id = mapping[1]
    try:
        await bot.send_message(
            chat_id=user_id,
            text=f"Admin xabaringizga javob qaytardi\n\n{message.reply_to_message.text or ''}",
        )
        await bot.copy_message(
            chat_id=user_id,
            from_chat_id=message.chat.id,
            message_id=message.message_id,
        )
        await message.reply('Javob yuborildi ✅')
    except (TelegramForbiddenError, TelegramBadRequest):
        await message.reply("Foydalanuvchi botni bloklagan yoki o'chirgan.")
