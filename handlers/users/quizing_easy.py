import random

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.question_quizing_easy import Easy_Array_Questions
from keyboards.default import menu
from loader import dp
from aiogram import types

from states.quiz_easy import QuizEasy


@dp.message_handler(Command("quiz_easy"), state=None)
async def enter_easy_test(message: types.Message, state: FSMContext):
    rand = random.randint(0, (len(Easy_Array_Questions) - 1))
    if rand == 0:
        # вместо Node - передаем клаву для ответа, и так для каждого вопроса
        await message.answer(text=f"Ответ на вопрос {rand}", reply_markup=menu.menu1.keyboard)
    elif rand == 1:
        await message.answer(text=f"Ответ на вопрос {rand}", reply_markup=menu.menu2.keyboard)
        '''
    elif rand == 2:
        await message.answer(text=f"Ответ на вопрос {rand}")
    elif rand == 3:
        await message.answer(text=f"Ответ на вопрос {rand}")

        
        await message.answer(text=
                             Easy_Array_Questions[
                                 random.randint(0, (len(Easy_Array_Questions) - 1))])
        # установка состояния
        # QuizEasy.Q1.set()
        '''
        await state.finish()

