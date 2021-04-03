from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from data.question_quizing_easy import Easy_Array_Questions
from handlers.users.checking_answers import func_answer1, func_answer2, func_answer3
from keyboards.default import menu_for_easy_quizing
from loader import dp
from aiogram import types

from states.quiz_easy import QuizEasy


@dp.message_handler(Command("quiz_easy"), state=None)
async def enter_easy_test(message: types.Message):
    await message.answer_photo(
        photo="https://sun9-59.userapi.com/impg/y7nJnzgMVs0XwM7cflhVlH01DE8loZUNIu54Ug/GkSlRyEVGH4.jpg?size=1200x800&quality=96&sign=54c7cd6bfb511adf18a85f7277880acc&type=album"
    )
    #  reply_markup=menu_for_easy_quizing.menu_0
    await message.answer(Easy_Array_Questions[0])
    await QuizEasy.Q1.set()


@dp.message_handler(state=QuizEasy.Q1)
async def answer_test_1(message: types.Message, state: FSMContext):
    answer_first_easy = message.text
    # пишем данные
    await state.update_data(answer1=answer_first_easy)
    await message.answer(text="Спасибо за ваш ответ!, нажмите на /quiz_easy Для продолжения"
                        )
    # reply_markup=ReplyKeyboardRemove()
    await QuizEasy.Q2.set()


@dp.message_handler(state=QuizEasy.Q2)
async def answer_test_2(message: types.Message, state: FSMContext):
    await message.answer_photo(
        photo="https://sun9-74.userapi.com/impg/4GSndLxSSM5KdJZjfAXgDVH-grfcECyZH7t7dQ/prQbILXkJYc.jpg?size=1920x1440&quality=96&sign=4af6e3f73508b2c24c2e6e34749af34a&type=album"
    )
    await message.answer(Easy_Array_Questions[1], reply_markup=menu_for_easy_quizing.menu_1)
    await QuizEasy.Q3.set()


@dp.message_handler(state=QuizEasy.Q3)
async def answer_test_3(message: types.Message, state: FSMContext):
    answer_second_easy = message.text
    # пишем данные
    await state.update_data(answer2=answer_second_easy)
    await message.answer(text="Спасибо за ваш ответ!, нажмите на /quiz_easy Для продолжения",
                         reply_markup=ReplyKeyboardRemove())
    await QuizEasy.Q4.set()


@dp.message_handler(state=QuizEasy.Q4)
async def answer_test_4(message: types.Message, state: FSMContext):
    await message.answer_photo(
        photo="https://sun9-46.userapi.com/impg/BPO3N5zfeo4bWElVfh89yxnduAts15zDxs177A/RjsyBuBc0s8.jpg?size=1133x850&quality=96&sign=210d67b1c645e4f3004432e6993103f2&type=album"
    )
    await message.answer(Easy_Array_Questions[2], reply_markup=menu_for_easy_quizing.menu_2)
    await QuizEasy.Q5.set()


@dp.message_handler(state=QuizEasy.Q5)
async def answer_test_5(message: types.Message, state: FSMContext):
    answer_second_easy = message.text
    # пишем данные
    await state.update_data(answer2=answer_second_easy)
    await message.answer(text="Спасибо за ваш ответ!, нажмите на /quiz_easy Для продолжения",
                         reply_markup=ReplyKeyboardRemove())
    await QuizEasy.Q6.set()


@dp.message_handler(state=QuizEasy.Q6)
async def finish_test(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer_first = data.get("answer1")
    answer_second = data.get("answer2")
    await message.answer("Ваши ответы:")
    await func_answer1(message, answer_first)
    await func_answer2(message, answer_second)
    await func_answer3(message, answer_second)
    await state.finish()
