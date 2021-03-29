from aiogram.dispatcher.filters.state import StatesGroup, State


class Quiz(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
