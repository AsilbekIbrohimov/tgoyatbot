from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.reciters import RECITERS

# Qiroatlar ro'yxatidan klaviatura (qatorda 2 tadan) + Asosiy Menyu
_rows = []
_labels = [label for _ident, label in RECITERS]
for i in range(0, len(_labels), 2):
    _rows.append([KeyboardButton(text=t) for t in _labels[i:i + 2]])
_rows.append([KeyboardButton(text='🔝 Asosiy Menyu')])

reciterKeyboard = ReplyKeyboardMarkup(keyboard=_rows, resize_keyboard=True)
