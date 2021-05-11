from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# получаем локацию
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            # запрашиваем локацию у пользователя
            KeyboardButton(text="Отправить свою локацию 🗺️", request_location=True)
        ],
        [
            KeyboardButton(text="Отмена")
        ]
    ],
    resize_keyboard=True,
    # одна кнопка в строке
    row_width=1

)
save_location = ReplyKeyboardMarkup(
    keyboard=[
        [
            # запрашиваем локацию у пользователя
            KeyboardButton(text="Отправить свою локацию 🗺️", request_location=True)
        ],
        [
            KeyboardButton(text="Отмена")
        ]
    ],
    resize_keyboard=True,
    # одна кнопка в строке
    row_width=2

)
