# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# callbacks для кнопок локацию
from aiogram.utils.callback_data import CallbackData
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# callbacks для кнопок локацию
TypeObject = CallbackData("ComingSoon", "type_place", "name_place", "number_to_remove")
# callbacks для next/finish прохождения по карте
NextOrFinishProgressMap = CallbackData("ComingSoon", "next")

# Клавиатура выбора типа объекта
SelectTypeAttractions = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Церковь|Храм|Собор",
            # callback_data="place:Church:2155"
            callback_data=TypeObject.new(type_place="Church", name_place="Церковь|Храм|Собор", number_to_remove=0)
        )
    ],
    [
        InlineKeyboardButton(
            text="Доходный Дом|Особняк",
            # callback_data="place:Church:2155"
            callback_data=TypeObject.new(type_place="ApartmentBuilding", name_place="Дом|Особняк",
                                                 number_to_remove=1)
        )
    ],
    [
        InlineKeyboardButton
            (
            text="Музей|Сквер",
            callback_data=TypeObject.new(type_place="Museum", name_place="Музей|Сквер", number_to_remove=2)
        )
    ],
    [
        InlineKeyboardButton
            (
            text="Дворец|Театр",
            callback_data=TypeObject.new(type_place="Palace", name_place="Дворец|Театр", number_to_remove=3)
        )
    ],
    [
        InlineKeyboardButton
            (
            text="Памятник|Мемориал",
            callback_data=TypeObject.new(type_place="Monument", name_place="Памятник|Мемориал", number_to_remove=4)
        )
    ],
    [
        InlineKeyboardButton
            (
            text="Парк|Фонтан",
            callback_data=TypeObject.new(type_place="Park", name_place="Парк|Фонтан", number_to_remove=5)
        )
    ],
    [
        InlineKeyboardButton
            (
            text="Любую достопримечательность",
            callback_data=TypeObject.new(type_place="AnyOne", name_place="AnyOne", number_to_remove=6)
        )
    ],
    [
        InlineKeyboardButton
            (
            text="Отмена",
            callback_data="cancel_choice_attractions")
    ]

])
# Клавиатура next/finish
NextOrFinishLocationKeyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="next",
            # callback_data="place:Church:2155"
            callback_data=NextOrFinishProgressMap.new(next="True")
        ),
        InlineKeyboardButton(
            text="finish",
            callback_data=NextOrFinishProgressMap.new(next="False"))
    ]

])
# Клавиатура для получения локации
SendToBotUserLocation = ReplyKeyboardMarkup(
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
# Локация для сохранения изначальной позиции пользователя
SaveFirstLocationsInDataBase = ReplyKeyboardMarkup(
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
