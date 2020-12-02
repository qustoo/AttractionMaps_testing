from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    # Отвечает на первый и кидаем его на второй
    Q1 = State()
    Q2 = State()