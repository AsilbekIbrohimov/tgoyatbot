from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


pages = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton (text = "⬅️", callback_data= "-1"),
        InlineKeyboardButton (text= "❌", callback_data= "delete"),
        InlineKeyboardButton (text = "➡️", callback_data = "1")
        ],
    ],)