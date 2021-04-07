from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.checking_answers_medium_level import check_answer_medium_1, check_answer_medium_2, check_answer_medium_3, \
    check_answer_medium_4, check_answer_medium_5, check_answer_medium_6, check_answer_medium_7, check_answer_medium_8, \
    check_answer_medium_9, check_answer_medium_10, check_answer_medium_11, check_answer_medium_12, \
    check_answer_medium_13
from quiz_all_files.Quiz_Questions.questions_quiz import Medium_Array_Questions
from loader import dp, photo_db
from aiogram import types

from states.MachineStates_For_Quiz import QuizMedium


@dp.message_handler(Command("quiz_medium"), state=None)
async def enter_easy_test(message: types.Message):
    # присылаем фотку и клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_1'), 'rb'))
    await message.answer("Вопрос 1:\n" + Medium_Array_Questions[0])
    await QuizMedium.Q1.set()


@dp.message_handler(state=QuizMedium.Q1)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_first_medium = message.text
    await state.update_data(answer1=answer_first_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_2'), 'rb'))
    await message.answer("Вопрос 2:\n" + Medium_Array_Questions[1])

    await QuizMedium.Q2.set()


@dp.message_handler(state=QuizMedium.Q2)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_second_medium = message.text
    await state.update_data(answer2=answer_second_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_3'), 'rb'))
    await message.answer("Вопрос 3:\n" + Medium_Array_Questions[2])

    await QuizMedium.Q3.set()


@dp.message_handler(state=QuizMedium.Q3)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_third_medium = message.text
    await state.update_data(answer3=answer_third_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_4'), 'rb'))
    await message.answer("Вопрос 4:\n" + Medium_Array_Questions[3])

    await QuizMedium.Q4.set()


@dp.message_handler(state=QuizMedium.Q4)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_4th_medium = message.text
    await state.update_data(answer4=answer_4th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_5'), 'rb'))
    await message.answer("Вопрос 5:\n" + Medium_Array_Questions[4])

    await QuizMedium.Q5.set()


@dp.message_handler(state=QuizMedium.Q5)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_5th_medium = message.text
    await state.update_data(answer5=answer_5th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_6'), 'rb'))
    await message.answer("Вопрос 6:\n" + Medium_Array_Questions[5])

    await QuizMedium.Q6.set()


@dp.message_handler(state=QuizMedium.Q6)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_6th_medium = message.text
    await state.update_data(answer6=answer_6th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_7'), 'rb'))
    await message.answer("Вопрос 7:\n" + Medium_Array_Questions[6])

    await QuizMedium.Q7.set()


@dp.message_handler(state=QuizMedium.Q7)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_7th_medium = message.text
    await state.update_data(answer7=answer_7th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_8'), 'rb'))
    await message.answer("Вопрос 8:\n" + Medium_Array_Questions[7])

    await QuizMedium.Q8.set()


@dp.message_handler(state=QuizMedium.Q8)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_8th_medium = message.text
    await state.update_data(answer8=answer_8th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_9'), 'rb'))
    await message.answer("Вопрос 9:\n" + Medium_Array_Questions[8])

    await QuizMedium.Q9.set()


@dp.message_handler(state=QuizMedium.Q9)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_9th_medium = message.text
    await state.update_data(answer9=answer_9th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_10'), 'rb'))
    await message.answer("Вопрос 10:\n" + Medium_Array_Questions[9])

    await QuizMedium.Q10.set()


@dp.message_handler(state=QuizMedium.Q10)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_10th_medium = message.text
    await state.update_data(answer10=answer_10th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_11'), 'rb'))
    await message.answer("Вопрос 11:\n" + Medium_Array_Questions[10])

    await QuizMedium.Q11.set()


@dp.message_handler(state=QuizMedium.Q11)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_11th_medium = message.text
    await state.update_data(answer9=answer_11th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_12'), 'rb'))
    await message.answer("Вопрос 12:\n" + Medium_Array_Questions[11])

    await QuizMedium.Q12.set()


@dp.message_handler(state=QuizMedium.Q12)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_12th_medium = message.text
    await state.update_data(answer12=answer_12th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_13'), 'rb'))
    await message.answer("Вопрос 13:\n" + Medium_Array_Questions[12])

    await QuizMedium.Q13.set()


@dp.message_handler(state=QuizMedium.Q13)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    data = await state.get_data()

    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = data.get("answer3")
    answer4 = data.get("answer4")
    answer5 = data.get("answer5")
    answer6 = data.get("answer6")
    answer7 = data.get("answer7")
    answer8 = data.get("answer8")
    answer9 = data.get("answer9")
    answer10 = data.get("answer10")
    answer11 = data.get("answer11")
    answer12 = data.get("answer12")
    answer13 = message.text
    await check_answer_medium_1(message, answer1)
    await check_answer_medium_2(message, answer2)
    await check_answer_medium_3(message, answer3)
    await check_answer_medium_4(message, answer4)
    await check_answer_medium_5(message, answer5)
    await check_answer_medium_6(message, answer6)
    await check_answer_medium_7(message, answer7)
    await check_answer_medium_8(message, answer8)
    await check_answer_medium_9(message, answer9)
    await check_answer_medium_10(message, answer10)
    await check_answer_medium_11(message, answer11)
    await check_answer_medium_12(message, answer12)
    await check_answer_medium_13(message, answer13)
    await state.finish()
