from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_0 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Виктора Дамасский")
        ],
        [
            KeyboardButton(text="Георгия Победоносца")

        ],
        [
            KeyboardButton(text="Иоанна Сочавского")
        ],

    ],
    # чтобы размер был нормальным, клава не занимала пол-экрана
    resize_keyboard=True)

menu_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="продукты питания пилотов")
        ],
        [
            KeyboardButton(text="космический спускаемый аппарат - Союз ТМА-10")

        ],
        [
            KeyboardButton(text="баллистическая капсула")
        ],

    ],
    # чтобы размер был нормальным, клава не занимала пол-экрана
    resize_keyboard=True)

menu_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Великой Отечественной войне")
        ],
        [
            KeyboardButton(text="в Первой мировой войне")

        ],
        [
            KeyboardButton(text="в Отечественной войне 1812 г")
        ],

    ],
    # чтобы размер был нормальным, клава не занимала пол-экрана
    resize_keyboard=True)

menu_3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ответ №1111")
        ],
        [
            KeyboardButton(text="Ответ №2222")

        ],
        [
            KeyboardButton(text="Ответ №3333")
        ],

    ],
    # чтобы размер был нормальным, клава не занимала пол-экрана
    resize_keyboard=True)
