# -*- coding: utf-8 -*-
"""i18n yordamchilari: t() tarjima, til-agnostik tugma filtri, klaviatura quruvchilar."""
from aiogram.filters import BaseFilter
from aiogram.types import (
    Message, ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
)

from data.locales import LOCALES, FALLBACK, UI_LANGS
from data.suralist import suralist

BUTTON_KEYS = ['b_general', 'b_oyatlar', 'b_suradan', 'b_settings', 'b_feedback',
               'b_donate', 'b_main', 'b_back', 'b_next', 'b_prev', 'b_trans',
               'b_reciter', 'b_lang', 'b_sura_audio']


def t(key: str, lang: str = FALLBACK, **kw) -> str:
    d = LOCALES.get(lang) or LOCALES[FALLBACK]
    text = d.get(key) or LOCALES[FALLBACK].get(key) or key
    return text.format(**kw) if kw else text


# Har bir tugma kaliti uchun barcha tillardagi yorliqlar to'plami
_LABELS = {}
for _key in BUTTON_KEYS:
    _LABELS[_key] = {LOCALES[lng][_key] for lng in LOCALES if _key in LOCALES[lng]}


class Btn(BaseFilter):
    """Til-agnostik tugma filtri: matn shu tugmaning istalgan tildagi yorlig'imi?"""
    def __init__(self, key: str):
        self.key = key

    async def __call__(self, message: Message) -> bool:
        return bool(message.text) and message.text in _LABELS.get(self.key, set())


# ---------- Klaviaturalar ----------
def main_menu_kb(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=t('b_general', lang)), KeyboardButton(text=t('b_oyatlar', lang))],
        [KeyboardButton(text=t('b_suradan', lang)), KeyboardButton(text=t('b_settings', lang))],
        [KeyboardButton(text=t('b_feedback', lang)), KeyboardButton(text=t('b_donate', lang))],
    ], resize_keyboard=True)


def back_main_kb(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=t('b_main', lang))]], resize_keyboard=True)


def read_kb(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=t('b_sura_audio', lang))],
        [KeyboardButton(text=t('b_back', lang)), KeyboardButton(text=t('b_main', lang))],
    ], resize_keyboard=True)


def settings_kb(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=t('b_trans', lang)), KeyboardButton(text=t('b_reciter', lang))],
        [KeyboardButton(text=t('b_lang', lang)), KeyboardButton(text=t('b_main', lang))],
    ], resize_keyboard=True)


def sura_kb(page: int, lang: str) -> ReplyKeyboardMarkup:
    """Sura tanlash klaviaturasi. page=1 -> 1-56, page=2 -> 57-114."""
    start, end = (1, 56) if page == 1 else (57, 114)
    rows, row = [], []
    for i in range(start, end + 1):
        row.append(KeyboardButton(text=f"{i}.{suralist[i - 1]}"))
        if len(row) == 4:
            rows.append(row); row = []
    if row:
        rows.append(row)
    if page == 1:
        rows.append([KeyboardButton(text=t('b_main', lang)), KeyboardButton(text=t('b_next', lang))])
    else:
        rows.append([KeyboardButton(text=t('b_main', lang)), KeyboardButton(text=t('b_prev', lang))])
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)


def sura_kb_for(raqam: int, lang: str) -> ReplyKeyboardMarkup:
    return sura_kb(1 if raqam <= 56 else 2, lang)


def lang_inline_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=label, callback_data=f"setlang:{code}")]
        for code, label in UI_LANGS
    ])
