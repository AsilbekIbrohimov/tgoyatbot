from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message

from loader import db
from filters.private_chat import IsPrivate
from utils.i18n import t

fallback_router = Router()


@fallback_router.message(IsPrivate(), StateFilter("*"))
async def unknown(message: Message):
    await message.reply(t('m_fallback', db.get_ui_lang(message.from_user.id)))
