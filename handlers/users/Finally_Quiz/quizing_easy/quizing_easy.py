from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from quiz_all_files.Quiz_Questions.questions_quiz import Easy_Array_Questions
from data.checking_answers import func_answer1, func_answer2, func_answer3, func_answer4, func_answer5, func_answer6, \
    func_answer7, func_answer8, func_answer9, func_answer10
from keyboards.default import menu_for_easy_quizing
from loader import dp, photo_db
from aiogram import types
from keyboards.inline.quiz_keyboard import choice_r_q

from states.MachineStates_For_Quiz import QuizEasy


@dp.message_handler(Command("quiz_easy"), state=None)
async def enter_easy_test(message: types.Message):
    # присылаем фотку и клаву
    await message.answer(text="Вопрос 1:\n")
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_1'), 'rb'))
    await message.answer(Easy_Array_Questions[0], reply_markup=menu_for_easy_quizing.menu_0)
    await QuizEasy.Q1.set()


@dp.message_handler(state=QuizEasy.Q1)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_first_easy = message.text
    await state.update_data(answer1=answer_first_easy)

    # Закрываем клаву
    await message.answer(text="Вопрос 2:\n", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_2'), 'rb'))
    await message.answer(Easy_Array_Questions[1], reply_markup=menu_for_easy_quizing.menu_1)

    await QuizEasy.Q2.set()


@dp.message_handler(state=QuizEasy.Q2)
async def answer_test_2(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_second_easy = message.text
    await state.update_data(answer2=answer_second_easy)

    # Закрываем клаву
    await message.answer(text="Вопрос 3:\n", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_3'), 'rb'))
    await message.answer(Easy_Array_Questions[2], reply_markup=menu_for_easy_quizing.menu_2)

    await QuizEasy.Q3.set()


@dp.message_handler(state=QuizEasy.Q3)
async def answer_test_3(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_third_easy = message.text
    await state.update_data(answer3=answer_third_easy)

    # Закрываем и отправляем клаву
    await message.answer(text="Вопрос 4:\n", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_4'), 'rb'))
    await message.answer(Easy_Array_Questions[3], reply_markup=menu_for_easy_quizing.menu_3)

    await QuizEasy.Q4.set()


@dp.message_handler(state=QuizEasy.Q4)
async def answer_test_4(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_fourth_easy = message.text
    await state.update_data(answer4=answer_fourth_easy)

    # Закрываем и отправляем клаву
    await message.answer(text="Вопрос 5:\n", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_5'), 'rb'))
    await message.answer(Easy_Array_Questions[4], reply_markup=menu_for_easy_quizing.menu_4)

    await QuizEasy.Q5.set()


@dp.message_handler(state=QuizEasy.Q5)
async def answer_test_5(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_5th_easy = message.text
    await state.update_data(answer5=answer_5th_easy)

    await message.answer(text="Вопрос 6:\n", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_6'), 'rb'))
    await message.answer(Easy_Array_Questions[5], reply_markup=menu_for_easy_quizing.menu_5)
    await QuizEasy.Q6.set()


@dp.message_handler(state=QuizEasy.Q6)
async def answer_test_6(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_6th = message.text
    await state.update_data(answer6=answer_6th)

    # Закрываем и отправляем клаву

    await message.answer(text="Вопрос 7:\n", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_7'), 'rb'))
    await message.answer(Easy_Array_Questions[6], reply_markup=menu_for_easy_quizing.menu_6)

    await QuizEasy.Q7.set()


@dp.message_handler(state=QuizEasy.Q7)
async def answer_test_6(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_7th = message.text
    await state.update_data(answer7=answer_7th)

    # Закрываем и отправляем клаву

    await message.answer(text="Вопрос 8:\n", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_8'), 'rb'))
    await message.answer(Easy_Array_Questions[7], reply_markup=menu_for_easy_quizing.menu_7)

    await QuizEasy.Q8.set()


@dp.message_handler(state=QuizEasy.Q8)
async def answer_test_6(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_8th = message.text
    await state.update_data(answer8=answer_8th)

    # Закрываем и отправляем клаву

    await message.answer(text="Вопрос 9:\n", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_9'), 'rb'))
    await message.answer(Easy_Array_Questions[8], reply_markup=menu_for_easy_quizing.menu_8)

    await QuizEasy.Q9.set()


@dp.message_handler(state=QuizEasy.Q9)
async def answer_test_6(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_9th = message.text
    await state.update_data(answer9=answer_9th)

    # Закрываем и отправляем клаву

    await message.answer(text="Вопрос 10:\n", reply_markup=ReplyKeyboardRemove())

    # отправляем новую фотку + вопрос + новую клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_10'), 'rb'))
    await message.answer(Easy_Array_Questions[9], reply_markup=menu_for_easy_quizing.menu_9)

    await QuizEasy.Q10.set()


@dp.message_handler(state=QuizEasy.Q10)
async def answer_test_7(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_10th = message.text
    await state.update_data(answer10=answer_10th)
    # Закрываем и отправляем клаву
    await message.answer(text="Спасибо за ваши ответы\n Чтобы закончить викторину нажмите /finish"
                         , reply_markup=ReplyKeyboardRemove())
    await QuizEasy.Q11.set()


@dp.message_handler(Command("finish"), state=QuizEasy.Q11)
async def finish_test(message: types.Message, state: FSMContext):
    # получаем все данные
    data = await state.get_data()

    # пишем их в переменные
    answer_first = data.get("answer1")
    answer_second = data.get("answer2")
    answer_third = data.get("answer3")
    answer_fourth = data.get("answer4")
    answer_5th = data.get("answer5")
    answer_6th = data.get("answer6")
    answer_7th = data.get("answer7")
    answer_8th = data.get("answer8")
    answer_9th = data.get("answer9")
    answer_10th = data.get("answer10")

    await message.answer("Ваши ответы:")

    # пишем ответы

    list_answer = [func_answer1(message, answer_first),
                   func_answer2(message, answer_second),
                   func_answer3(message, answer_second),
                   func_answer4(message, answer_fourth),
                   func_answer5(message, answer_5th),
                   func_answer6(message, answer_6th),
                   func_answer7(message, answer_7th),
                   func_answer8(message, answer_8th),
                   func_answer9(message, answer_9th),
                   func_answer10(message, answer_10th)]

    await func_answer1(message, answer_first)
    await func_answer2(message, answer_second)
    await func_answer3(message, answer_third)
    await func_answer4(message, answer_fourth)
    await func_answer5(message, answer_5th)
    await func_answer6(message, answer_6th)
    await func_answer7(message, answer_7th)
    await func_answer8(message, answer_8th)
    await func_answer9(message, answer_9th)
    await func_answer10(message, answer_10th)
    #await message.answer('\n'.join(list_answer))
    await message.answer("Чтобы увидеть свой рейтинг, после прохождения викторины нажмите /get_my_rating")

    await state.finish()
