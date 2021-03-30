from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# получаем локацию
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            # запрашиваем локацию у пользователя
            KeyboardButton(text="🌐", request_location=True)
        ]

    ],
    resize_keyboard=True,

    # one_time_keyboard=True

)
