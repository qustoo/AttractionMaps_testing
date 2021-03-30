from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states.quiz_easy import QuizEasy


@dp.message_handler(Command("quiz_easy"), state=None)
async def enter_easy_test(message: types.Message, state: FSMContext):
    await message.answer(text="В разработке!1")
    # установка состояния
    # QuizEasy.Q1.set()
    await state.finish()
