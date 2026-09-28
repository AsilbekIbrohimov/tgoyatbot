"""Qidiruv natijalarini sahifalash uchun umumiy yordamchilar.

Natijalar FSM state ma'lumotlarida saqlanadi (pages, idx, total), shu sababli
bot qayta ishga tushsa ham eski tugma bosilganda KeyError bo'lmaydi.
"""
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.inline.changePageKeyboard import pages as pages_kb


def _header(idx: int, total_pages: int, total_ayahs: int) -> str:
    return f"Natijalar {idx + 1}-sahifa {total_pages} dan {total_ayahs} ta oyat\n\n"


async def show_first(placeholder: Message, state: FSMContext, pages: list, total_ayahs: int):
    await state.update_data(pages=pages, idx=0, total=total_ayahs)
    await placeholder.edit_text(
        _header(0, len(pages), total_ayahs) + pages[0], reply_markup=pages_kb
    )


async def paginate(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    pages = data.get("pages")
    if not pages:
        await call.answer("Natijalar eskirgan. Iltimos qaytadan qidiring.", show_alert=True)
        return
    idx = data.get("idx", 0) + int(call.data)
    if idx < 0:
        idx = 0
    if idx >= len(pages):
        idx = len(pages) - 1
    await state.update_data(idx=idx)
    await call.message.edit_text(
        _header(idx, len(pages), data.get("total", 0)) + str(pages[idx]),
        reply_markup=pages_kb,
    )
    await call.answer()
