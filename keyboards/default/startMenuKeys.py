from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛍️ Mahsulotlar'),
            KeyboardButton(text="ℹ️ Qo'llanma")
        ],
    ],
    resize_keyboard=True
)