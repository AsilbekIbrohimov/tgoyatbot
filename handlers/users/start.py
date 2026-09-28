from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from loader import dp, db, bot
from data.config import ADMINS
from keyboards.default.forstartKeyboard import startKeyboard

start_router = Router()


def _mention(user) -> str:
    return f'<a href="tg://user?id={user.id}">{user.full_name}</a>'


async def go_main_menu(message: Message, state: FSMContext):
    """Asosiy menyuga qaytish (boshqa handlerlar ham chaqiradi)."""
    await state.clear()
    await message.answer(
        f"Assalomu alaykum {message.from_user.full_name}! Botga xush kelibsiz",
        reply_markup=startKeyboard,
    )


async def _register(message: Message, ads: str = None):
    """Foydalanuvchini bazaga qo'shadi; faqat YANGI bo'lsa adminga xabar beradi."""
    existed = db.select_user(id=message.from_user.id)
    db.add_user(id=message.from_user.id, name=message.from_user.full_name)
    if not existed:
        try:
            count = db.count_users()[0]
            username = message.from_user.username or ''
            msg = f"{_mention(message.from_user)} {username} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
            if ads:
                msg += f"\nAds code {ads}"
            await bot.send_message(chat_id=ADMINS[0], text=msg)
        except Exception:
            pass


@start_router.message(CommandStart(deep_link=True))
async def start_with_ref(message: Message, command: CommandObject, state: FSMContext):
    await state.clear()
    await _register(message, ads=command.args)
    await message.answer(
        f"Assalomu alaykum {message.from_user.full_name}! Botga xush kelibsiz",
        reply_markup=startKeyboard,
    )


@start_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.clear()
    await _register(message)
    await message.answer(
        f"Assalomu alaykum {message.from_user.full_name}! Botga xush kelibsiz",
        reply_markup=startKeyboard,
    )
