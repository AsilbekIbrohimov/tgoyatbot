from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


Adminkeyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Allusers'),
            KeyboardButton(text='Check users'),
        ],
        [
            KeyboardButton(text='Reklama'),
            KeyboardButton(text='🔝 Asosiy Menyu'),
        ],
    ],
    resize_keyboard=True
)