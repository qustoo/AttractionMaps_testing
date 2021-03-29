from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Local", request_location=True)
        ]

    ],
    resize_keyboard=True,

    # one_time_keyboard=True

)
