"""Qidiruv natijalarini sahifalash (natijalar FSM state'da saqlanadi)."""
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.inline.changePageKeyboard import pages as pages_kb
from utils.i18n import t


def _header(idx, total_pages, total_ayahs, lang):
    return t('m_results', lang, page=idx + 1, pages=total_pages, ayahs=total_ayahs)


async def show_first(placeholder: Message, state: FSMContext, pages: list, total_ayahs: int, lang: str):
    await state.update_data(pages=pages, idx=0, total=total_ayahs)
    await placeholder.edit_text(_header(0, len(pages), total_ayahs, lang) + pages[0], reply_markup=pages_kb)


async def paginate(call: CallbackQuery, state: FSMContext, lang: str):
    data = await state.get_data()
    pages = data.get("pages")
    if not pages:
        await call.answer("—", show_alert=True)
        return
    idx = data.get("idx", 0) + int(call.data)
    idx = max(0, min(idx, len(pages) - 1))
    await state.update_data(idx=idx)
    await call.message.edit_text(
        _header(idx, len(pages), data.get("total", 0), lang) + str(pages[idx]), reply_markup=pages_kb)
    await call.answer()
