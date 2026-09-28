from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.text_editions import TEXT_EDITIONS

_labels = [label for _ident, label in TEXT_EDITIONS]
_rows = [[KeyboardButton(text=t)] for t in _labels]  # har qatorda 1 ta (nomlar uzun)
_rows.append([KeyboardButton(text='🔝 Asosiy Menyu')])

textEditionKeyboard = ReplyKeyboardMarkup(keyboard=_rows, resize_keyboard=True)
