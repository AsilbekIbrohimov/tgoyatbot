from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenuKeyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🔝 Asosiy Menyu'),
        ],
    ],
    resize_keyboard=True
)


mainAndbackKeyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='🔝 Asosiy Menyu')
        ],
    ],
    resize_keyboard=True
)