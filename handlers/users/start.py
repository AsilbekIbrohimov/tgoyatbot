import re

from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from loader import db, bot
from data.config import ADMINS
from data.suralist import suralist
from data.ayah_counts import AYAH_COUNTS
from utils.i18n import t, main_menu_kb, lang_inline_kb
from utils.ayah_text import get_ayah_text
from utils.get_link import get_link

start_router = Router()
_AYAH_REF = re.compile(r'^a_(\d{1,3})_(\d{1,3})$')


def _mention(user) -> str:
    return f'<a href="tg://user?id={user.id}">{user.full_name}</a>'


async def go_main_menu(message: Message, state: FSMContext):
    """Asosiy menyuga qaytish (boshqa handlerlar ham chaqiradi)."""
    await state.clear()
    lang = db.get_ui_lang(message.from_user.id)
    await message.answer(t('m_welcome', lang, name=message.from_user.full_name),
                         reply_markup=main_menu_kb(lang))


async def _register(message: Message, ads: str = None) -> bool:
    """Foydalanuvchini qo'shadi. Yangi bo'lsa True qaytaradi va adminni xabardor qiladi."""
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
    return not existed


async def _start(message: Message, state: FSMContext, ads: str = None):
    await state.clear()
    is_new = await _register(message, ads=ads)
    if is_new:
        # Yangi foydalanuvchi — avval interfeys tilini tanlaydi
        await message.answer("Tilni tanlang / Choose your language:", reply_markup=lang_inline_kb())
    else:
        await go_main_menu(message, state)


@start_router.message(CommandStart(deep_link=True))
async def start_with_ref(message: Message, command: CommandObject, state: FSMContext):
    args = command.args or ''
    m = _AYAH_REF.match(args)
    if m:
        # Ulashilgan oyat havolasi: a_<sura>_<ayah>
        sura, ayah = int(m.group(1)), int(m.group(2))
        await _register(message)
        if 1 <= sura <= 114 and 1 <= ayah <= AYAH_COUNTS.get(sura, 0):
            uid = message.from_user.id
            text = await get_ayah_text(sura, ayah, db.get_text_ed(uid))
            link = await get_link(sura, ayah, db.get_reciter(uid))
            await message.answer(f"{suralist[sura - 1]} — {sura}:{ayah}\n\n{text}{link}")
        await go_main_menu(message, state)
        return
    await _start(message, state, ads=args)


@start_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await _start(message, state)
