from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Церковь Святого Ивана")
        ],
        [
            KeyboardButton(text="Памятник Раку")

        ],
        [
            KeyboardButton(text="Аллея Роз")
        ],

    ],
    # чтобы размер был нормальным, клава не занимала пол-экрана
    resize_keyboard=True

)
