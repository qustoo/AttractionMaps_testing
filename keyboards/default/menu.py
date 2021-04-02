from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ответ №1")
        ],
        [
            KeyboardButton(text="Ответ №2")

        ],
        [
            KeyboardButton(text="Ответ №3")
        ],

    ],
    # чтобы размер был нормальным, клава не занимала пол-экрана
    resize_keyboard=True

)

menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ответ №11")
        ],
        [
            KeyboardButton(text="Ответ №22")

        ],
        [
            KeyboardButton(text="Ответ №33")
        ],

    ],
    # чтобы размер был нормальным, клава не занимала пол-экрана
    resize_keyboard=True

)
