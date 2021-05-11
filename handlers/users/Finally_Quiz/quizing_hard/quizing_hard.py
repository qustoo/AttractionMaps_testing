from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.checking_answers_hard_level import check_answer_hard_1, check_answer_hard_2, check_answer_hard_3, \
    check_answer_hard_4, check_answer_hard_5, check_answer_hard_6, check_answer_hard_7, check_answer_hard_8, \
    check_answer_hard_9, check_answer_hard_10, check_answer_hard_11, check_answer_hard_12, check_answer_hard_13, \
    check_answer_hard_14, check_answer_hard_15, check_answer_hard

from quiz_all_files.Quiz_Questions.questions_quiz import Hard_Array_Questions
from loader import dp, photo_db
from aiogram import types

from states.MachineStates_For_Quiz import QuizHard

List_of_answers_hard = []


@dp.message_handler(Command("quiz_hard"), state=None)
async def enter_hard_test(message: types.Message):
    # присылаем фотку и клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_1'), 'rb'))
    await message.answer("Вопрос 1:\n" + Hard_Array_Questions[0])
    await QuizHard.Q1.set()


@dp.message_handler(state=QuizHard.Q1)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_first_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer1=answer_first_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_2'), 'rb'))
    await message.answer("Вопрос 2:\n" + Hard_Array_Questions[1])
    await QuizHard.Q2.set()


@dp.message_handler(state=QuizHard.Q2)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_2nd_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer2=answer_2nd_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_3'), 'rb'))
    await message.answer("Вопрос 3:\n" + Hard_Array_Questions[2])
    await QuizHard.Q3.set()


@dp.message_handler(state=QuizHard.Q3)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_3rd_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer3=answer_3rd_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_4'), 'rb'))
    await message.answer("Вопрос 4:\n" + Hard_Array_Questions[3])
    await QuizHard.Q4.set()


@dp.message_handler(state=QuizHard.Q4)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_4th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer4=answer_4th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_5'), 'rb'))
    await message.answer("Вопрос 5:\n" + Hard_Array_Questions[4])
    await QuizHard.Q5.set()


@dp.message_handler(state=QuizHard.Q5)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_5th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer5=answer_5th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_6'), 'rb'))
    await message.answer("Вопрос 6:\n" + Hard_Array_Questions[5])
    await QuizHard.Q6.set()


@dp.message_handler(state=QuizHard.Q6)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_6th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer6=answer_6th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_7'), 'rb'))
    await message.answer("Вопрос 7:\n" + Hard_Array_Questions[6])
    await QuizHard.Q7.set()


@dp.message_handler(state=QuizHard.Q7)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_7th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer7=answer_7th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_8'), 'rb'))
    await message.answer("Вопрос 8:\n" + Hard_Array_Questions[7])
    await QuizHard.Q8.set()


@dp.message_handler(state=QuizHard.Q8)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_8th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer8=answer_8th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_9'), 'rb'))
    await message.answer("Вопрос 9:\n" + Hard_Array_Questions[8])
    await QuizHard.Q9.set()


@dp.message_handler(state=QuizHard.Q9)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_9th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer9=answer_9th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_10'), 'rb'))
    await message.answer("Вопрос 10:\n" + Hard_Array_Questions[9])
    await QuizHard.Q10.set()


@dp.message_handler(state=QuizHard.Q10)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_10th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer10=answer_10th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_11'), 'rb'))
    await message.answer("Вопрос 11:\n" + Hard_Array_Questions[10])
    await QuizHard.Q11.set()


@dp.message_handler(state=QuizHard.Q11)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_11th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer11=answer_11th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_12'), 'rb'))
    await message.answer("Вопрос 12:\n" + Hard_Array_Questions[11])
    await QuizHard.Q12.set()


@dp.message_handler(state=QuizHard.Q12)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_12th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer12=answer_12th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_13'), 'rb'))
    await message.answer("Вопрос 13:\n" + Hard_Array_Questions[12])
    await QuizHard.Q13.set()


@dp.message_handler(state=QuizHard.Q13)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_13th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer13=answer_13th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_14'), 'rb'))
    await message.answer("Вопрос 14:\n" + Hard_Array_Questions[13])
    await QuizHard.Q14.set()


@dp.message_handler(state=QuizHard.Q14)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_14th_hard = message.text
    List_of_answers_hard.append(message.text)
    await state.update_data(answer14=answer_14th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_15'), 'rb'))
    await message.answer("Вопрос 15:\n" + Hard_Array_Questions[14])
    await QuizHard.Q15.set()


@dp.message_handler(state=QuizHard.Q15)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем последний ответ
    List_of_answers_hard.append(message.text)
    await state.update_data(answer15=message.text)
    # сохраняем и пишем данные
    data = await state.get_data()

    # сохраняем и пишем данные
    # data = await state.get_data()
    # answer1 = data.get("answer1")
    # answer2 = data.get("answer2")
    # answer3 = data.get("answer3")
    # answer4 = data.get("answer4")
    # answer5 = data.get("answer5")
    # answer6 = data.get("answer6")
    # answer7 = data.get("answer7")
    # answer8 = data.get("answer8")
    # answer9 = data.get("answer9")
    # answer10 = data.get("answer10")
    # answer11 = data.get("answer11")
    # answer12 = data.get("answer12")
    # answer13 = data.get("answer13")
    # answer14 = data.get("answer14")
    # answer15 = message.text
    #
    # await check_answer_hard_1(message, answer1)
    # await check_answer_hard_2(message, answer2)
    # await check_answer_hard_3(message, answer3)
    # await check_answer_hard_4(message, answer4)
    # await check_answer_hard_5(message, answer5)
    # await check_answer_hard_6(message, answer6)
    # await check_answer_hard_7(message, answer7)
    # await check_answer_hard_8(message, answer8)
    # await check_answer_hard_9(message, answer9)
    # await check_answer_hard_10(message, answer10)
    # await check_answer_hard_11(message, answer11)
    # await check_answer_hard_12(message, answer12)
    # await check_answer_hard_13(message, answer13)
    # await check_answer_hard_14(message, answer14)
    # await check_answer_hard_15(message, answer15)

    # checked = []
    #
    # for i in range(len(data)):
    #     checked.append(await check_answer_hard(message, data.get("answer" + str(i+1)), i+1))
    #
    # await message.answer('\n'.join(checked))
    # await state.finish()
    total_answers = await check_answer_hard(message, List_of_answers_hard)
    await message.answer(total_answers)

    await state.finish()
