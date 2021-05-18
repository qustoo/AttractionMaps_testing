from aiogram.utils.callback_data import CallbackData
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# Локация для сохранения изначальной позиции пользователя
SelectDistrictSovietKirosvky = ReplyKeyboardMarkup(
    keyboard=[
        [
            # запрашиваем локацию у пользователя
            KeyboardButton(text="Кировский")
        ],
        [
            KeyboardButton(text="Советский")
        ]
    ],
    resize_keyboard=True,
    # одна кнопка в строке
    row_width=2

)