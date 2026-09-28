"""Xayriya — Telegram Stars (XTR) orqali. Provider token shart emas."""
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import (
    Message, CallbackQuery, PreCheckoutQuery, LabeledPrice,
    InlineKeyboardMarkup, InlineKeyboardButton,
)

from loader import db
from utils.i18n import Btn

donate_router = Router()

AMOUNTS = [25, 50, 100, 250, 500]

INTRO = {
    'uz': "Botni qo'llab-quvvatlash uchun xayriya qiling (Telegram Stars ⭐):",
    'en': "Support the bot with a donation (Telegram Stars ⭐):",
    'ru': "Поддержите бота пожертвованием (Telegram Stars ⭐):",
    'tr': "Botu bir bağışla destekleyin (Telegram Stars ⭐):",
    'ar': "ادعم البوت بتبرع (Telegram Stars ⭐):",
}
THANKS = {
    'uz': "Xayriyangiz uchun katta rahmat! ❤️ Alloh rozi bo'lsin.",
    'en': "Thank you so much for your donation! ❤️",
    'ru': "Большое спасибо за пожертвование! ❤️",
    'tr': "Bağışınız için çok teşekkürler! ❤️",
    'ar': "شكرًا جزيلاً على تبرعك! ❤️",
}


def _tr(d, lang):
    return d.get(lang) or d['en']


def _kb():
    rows = [[InlineKeyboardButton(text=f"⭐ {a}", callback_data=f"don:{a}")] for a in AMOUNTS]
    return InlineKeyboardMarkup(inline_keyboard=rows)


@donate_router.message(Command("donate"), StateFilter("*"))
@donate_router.message(Btn('b_donate'), StateFilter("*"))
async def donate_menu(message: Message):
    lang = db.get_ui_lang(message.from_user.id)
    await message.answer(_tr(INTRO, lang), reply_markup=_kb())


@donate_router.callback_query(F.data.startswith("don:"))
async def donate_invoice(call: CallbackQuery):
    stars = int(call.data.split(":", 1)[1])
    await call.message.answer_invoice(
        title="Xayriya / Donation",
        description="Qur'on boti rivoji uchun ⭐",
        payload=f"donate_{stars}",
        currency="XTR",
        prices=[LabeledPrice(label=f"{stars} ⭐", amount=stars)],
    )
    await call.answer()


@donate_router.pre_checkout_query()
async def pre_checkout(pcq: PreCheckoutQuery):
    await pcq.answer(ok=True)


@donate_router.message(F.successful_payment)
async def paid(message: Message):
    lang = db.get_ui_lang(message.from_user.id)
    await message.answer(_tr(THANKS, lang))
