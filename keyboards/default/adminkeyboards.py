from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Adminkeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📊 Statistika'),
            KeyboardButton(text='📢 Reklama'),
        ],
        [
            KeyboardButton(text='📥 Foydalanuvchilar'),
            KeyboardButton(text='✅ Tekshirish'),
        ],
        [
            KeyboardButton(text='🗑 Bazani tozalash'),
        ],
        [
            KeyboardButton(text='🔝 Asosiy Menyu'),
        ],
    ],
    resize_keyboard=True
)
