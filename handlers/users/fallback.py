from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message

from filters.private_chat import IsPrivate

fallback_router = Router()


@fallback_router.message(IsPrivate(), StateFilter("*"))
async def unknown(message: Message):
    await message.reply(
        'Iltimos botdan foydalanish uchun tugma va buyruqlardan foydalaning'
    )
