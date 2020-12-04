from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Церковь Святого Ивана")
        ],
        [
            KeyboardButton(text="Памятник рачку")

        ],
        [
            KeyboardButton(text="Аллея Роз")
        ],

    ],
    resize_keyboard=True

)
