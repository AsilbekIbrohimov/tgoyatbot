from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Umumiy izlash🔎'),
            KeyboardButton(text='Oyatlar'),
        ],
        [
            KeyboardButton(text="Suradan izlash"),
            KeyboardButton(text='Sozlamalar'),
        ],
        [
            KeyboardButton(text='Fikr bildirish✍️'),
        ],
    ],
    resize_keyboard=True
)
