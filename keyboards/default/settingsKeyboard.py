from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

settingsKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='tarjima'),
            KeyboardButton(text='Qiroat 🎧'),
        ],
        [
            KeyboardButton(text='🔝 Asosiy Menyu'),
        ],
    ],
    resize_keyboard=True
)
