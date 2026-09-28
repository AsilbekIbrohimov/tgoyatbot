from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Oyat o'qish paytidagi klaviatura
readKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🎧 Butun sura audiosi')],
        [
            KeyboardButton(text='⬅️ Orqaga'),
            KeyboardButton(text='🔝 Asosiy Menyu'),
        ],
    ],
    resize_keyboard=True,
)
