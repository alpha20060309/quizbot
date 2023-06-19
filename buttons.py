from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


fanlar_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Matematika", callback_data="Matematika"),
            InlineKeyboardButton(text="Ona tili", callback_data="Ona tili"),
        ],
        [
            InlineKeyboardButton(text="Sport", callback_data="Sport"),
            InlineKeyboardButton(text="Informatika", callback_data="Informatika"),
        ],
        [
            InlineKeyboardButton(text="Tarix", callback_data="Tarix"),
        ],
       
    ]
)