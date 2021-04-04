from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from data.question_quizing_easy import Easy_Array_Questions
from data.url_photo.Easy_url_photo.easy_url_photo import url_1_easy, url_2_easy, url_3_easy, url_4_easy
from data.checking_answers import func_answer1, func_answer2, func_answer3, func_answer4
from keyboards.default import menu_for_easy_quizing
from loader import dp
from aiogram import types

from states.quiz_easy import QuizEasy


@dp.message_handler(Command("quiz_easy"), state=None)
async def enter_easy_test(message: types.Message):
    # присылаем фотку и клаву
    await message.answer_photo(photo=url_1_easy)
    await message.answer(Easy_Array_Questions[0], reply_markup=menu_for_easy_quizing.menu_0)
    await QuizEasy.Q1.set()


@dp.message_handler(state=QuizEasy.Q1)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_first_easy = message.text
    await state.update_data(answer1=answer_first_easy)

    # Закрываем клаву
    await message.answer(text="Спасибо за ваш ответ!", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=url_2_easy)
    await message.answer(Easy_Array_Questions[1], reply_markup=menu_for_easy_quizing.menu_1)

    await QuizEasy.Q2.set()


@dp.message_handler(state=QuizEasy.Q2)
async def answer_test_2(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_second_easy = message.text
    await state.update_data(answer2=answer_second_easy)

    # Закрываем клаву
    await message.answer(text="Спасибо за ваш ответ!", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=url_3_easy)
    await message.answer(Easy_Array_Questions[2], reply_markup=menu_for_easy_quizing.menu_2)

    await QuizEasy.Q3.set()


@dp.message_handler(state=QuizEasy.Q3)
async def answer_test_3(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_third_easy = message.text
    await state.update_data(answer3=answer_third_easy)

    # Закрываем и отправляем клаву
    await message.answer(text="Спасибо за ваш ответ!"
                         , reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=url_4_easy)
    await message.answer(Easy_Array_Questions[3], reply_markup=menu_for_easy_quizing.menu_3)

    await QuizEasy.Q4.set()


@dp.message_handler(state=QuizEasy.Q4)
async def answer_test_4(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_fourth_easy = message.text
    await state.update_data(answer4=answer_fourth_easy)

    # Закрываем и отправляем клаву
    await message.answer(text="Спасибо за ваш ответ!,чтобы закончить нажмите /finish",
                         reply_markup=ReplyKeyboardRemove())
    await QuizEasy.Q5.set()


@dp.message_handler(Command("finish"), state=QuizEasy.Q5)
async def finish_test(message: types.Message, state: FSMContext):
    # получаем все данные
    data = await state.get_data()

    # пишем их в переменные
    answer_first = data.get("answer1")
    answer_second = data.get("answer2")
    answer_third = data.get("answer3")
    answer_fourth = data.get("answer4")
    await message.answer("Ваши ответы:")

    # пишем ответы
    await func_answer1(message, answer_first)
    await func_answer2(message, answer_second)
    await func_answer3(message, answer_third)
    await func_answer4(message, answer_fourth)
    await state.finish()
