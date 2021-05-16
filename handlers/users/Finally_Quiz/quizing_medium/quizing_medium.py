from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold, hitalic

from handlers.users.Finally_Quiz.quizing_medium.quiz_medium_photo import med_photo_quiz
from handlers.users.get_my_rating import get_my_rating
from keyboards.inline.callback_datas import quiz_callback
from keyboards.inline.medium_keyboard import med_photo_keyboard1, medium_keyboard1, medium_keyboard2, medium_keyboard3, \
    medium_keyboard4, medium_keyboard5, medium_keyboard6, \
    medium_keyboard7, medium_keyboard8, medium_keyboard9, medium_keyboard10, medium_keyboard11, medium_keyboard12, \
    medium_keyboard13, CorrectAnswersMediumQuiz
from keyboards.inline.quiz_keyboard import YesOrNoFinishKeyboard
from quiz_all_files.Quiz_Questions.questions_quiz import Medium_Array_Questions
from loader import dp, photo_db, db
from aiogram import types

from states.MachineStates_For_Quiz import QuizMedium, YesOrNoFinishShowRating


@dp.message_handler(Command("quiz_medium"), state=None)
async def enter_easy_test(message: types.Message):
    # присылаем фотку и клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name=med_photo_quiz[0]), 'rb'),
                               reply_markup=med_photo_keyboard1)
    await message.answer(text="<b>Вопрос 1:</b>\n" + Medium_Array_Questions[0], reply_markup=medium_keyboard1)
    await QuizMedium.Q1.set()


@dp.callback_query_handler(quiz_callback.filter(next="2m"), state=QuizMedium.Q1)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer1=answer1)
    await call.message.edit_text(text="<b>Вопрос 2:</b>\n" + Medium_Array_Questions[1], reply_markup=medium_keyboard2)
    await QuizMedium.Q2.set()


@dp.callback_query_handler(quiz_callback.filter(next="3m"), state=QuizMedium.Q2)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer2=answer1)
    await call.message.edit_text(text="<b>Вопрос 3:</b>\n" + Medium_Array_Questions[2], reply_markup=medium_keyboard3)
    await QuizMedium.Q3.set()


@dp.callback_query_handler(quiz_callback.filter(next="4m"), state=QuizMedium.Q3)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer3=answer1)
    await call.message.edit_text(text="<b>Вопрос 4:</b>\n" + Medium_Array_Questions[3], reply_markup=medium_keyboard4)
    await QuizMedium.Q4.set()


@dp.callback_query_handler(quiz_callback.filter(next="5m"), state=QuizMedium.Q4)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer4=answer1)
    await call.message.edit_text(text="<b>Вопрос 5:</b>\n" + Medium_Array_Questions[4], reply_markup=medium_keyboard5)
    await QuizMedium.Q5.set()


@dp.callback_query_handler(quiz_callback.filter(next="6m"), state=QuizMedium.Q5)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer5=answer1)
    await call.message.edit_text(text="<b>Вопрос 6:</b>\n" + Medium_Array_Questions[5], reply_markup=medium_keyboard6)
    await QuizMedium.Q6.set()


@dp.callback_query_handler(quiz_callback.filter(next="7m"), state=QuizMedium.Q6)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer6=answer1)
    await call.message.edit_text(text="<b>Вопрос 7:</b>\n" + Medium_Array_Questions[6], reply_markup=medium_keyboard7)
    await QuizMedium.Q7.set()


@dp.callback_query_handler(quiz_callback.filter(next="8m"), state=QuizMedium.Q7)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer7=answer1)
    await call.message.edit_text(text="<b>Вопрос 8:</b>\n" + Medium_Array_Questions[7], reply_markup=medium_keyboard8)
    await QuizMedium.Q8.set()


@dp.callback_query_handler(quiz_callback.filter(next="9m"), state=QuizMedium.Q8)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer8=answer1)
    await call.message.edit_text(text="<b>Вопрос 9:</b>\n" + Medium_Array_Questions[8], reply_markup=medium_keyboard9)
    await QuizMedium.Q9.set()


@dp.callback_query_handler(quiz_callback.filter(next="10m"), state=QuizMedium.Q9)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer9=answer1)
    await call.message.edit_text(text="<b>Вопрос 10:</b>\n" + Medium_Array_Questions[9], reply_markup=medium_keyboard10)
    await QuizMedium.Q10.set()


@dp.callback_query_handler(quiz_callback.filter(next="11m"), state=QuizMedium.Q10)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer10=answer1)
    await call.message.edit_text(text="<b>Вопрос 11:</b>\n" + Medium_Array_Questions[10],
                                 reply_markup=medium_keyboard11)
    await QuizMedium.Q11.set()


@dp.callback_query_handler(quiz_callback.filter(next="12m"), state=QuizMedium.Q11)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer11=answer1)
    await call.message.edit_text(text="<b>Вопрос 12:</b>\n" + Medium_Array_Questions[11],
                                 reply_markup=medium_keyboard12)
    await QuizMedium.Q12.set()


@dp.callback_query_handler(quiz_callback.filter(next="13m"), state=QuizMedium.Q12)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer12=answer1)
    await call.message.edit_text(text="<b>Вопрос 13:</b>\n" + Medium_Array_Questions[12],
                                 reply_markup=medium_keyboard13)
    await QuizMedium.Q13.set()


@dp.callback_query_handler(quiz_callback.filter(next="14m"), state=QuizMedium.Q13)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer1 = callback_data.get('answer')
    await state.update_data(answer13=answer1)
    await call.message.edit_text(text="Спасибо за ваши ответы\n Чтобы закончить викторину нажмите /finish_medium",
                                 reply_markup=None)
    await QuizMedium.Q14.set()


# Выход

@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q1)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q2)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q3)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q4)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q5)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q6)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q7)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q8)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q9)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q10)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q11)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q12)
@dp.callback_query_handler(quiz_callback.filter(next="0m"), state=QuizMedium.Q13)
async def cancel_quiz(call: CallbackQuery):
    await call.message.edit_text(text="Спасибо за ваши ответы\n Чтобы закончить викторину нажмите /finish_medium")
    # Отправляем пустую клавиатуру, т.е. выходит из клавиатуры
    await QuizMedium.Q14.set()
    await call.message.edit_reply_markup(reply_markup=None)


# finish

@dp.message_handler(Command("finish_medium"), state=QuizMedium.Q14)
async def finish_test(message: types.Message, state: FSMContext):
    # # получаем все данные
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

    Answer_List_Question = [answer_first, answer_second, answer_third, answer_fourth, answer_5th, answer_6th,
                            answer_7th, answer_8th, answer_9th, answer_10th]

    # Обнуляем рейтинг
    await db.update_rating_easy(message.from_user.id, 0)

    result_str = ""
    for index in range(0, 10):
        if Answer_List_Question[index] == CorrectAnswersMediumQuiz[index]:
            result_str += hbold(f'Вопрос {index + 1}') + hbold(' - Правильный ответ!') + "\n\n"
            # postgres :  await db.get_rating_medium(id=message.from_user.id)
            rate = db.get_rating_medium(id=message.from_user.id)
            # postgres :   await db.update_rating_medium(id=message.from_user.id, rating=rate + 3.0)
            db.update_rating_medium(id=message.from_user.id, rating=rate + 3.0)
        else:
            result_str += hitalic(f'Вопрос {index + 1}') + hbold(' - Неправильный ответ!\n') + hitalic(
                f'Корректным ответом будет: \n') + hbold(f'{CorrectAnswersMediumQuiz[index]}') + "\n\n"
    await message.answer(text="Ваши ответы:\n\n" + result_str)

    await message.answer(text="Хотите увидеть свой рейтинг?", reply_markup=YesOrNoFinishKeyboard)
    await YesOrNoFinishShowRating.Q1.set()


@dp.message_handler(text="Да", state=YesOrNoFinishShowRating.Q1)
async def YesShowRating(message: types.message, state: FSMContext):
    await get_my_rating(message)
    await message.answer(text="Спасибо за прохождение викторины", reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text="Нет", state=YesOrNoFinishShowRating.Q1)
async def YesShowRating(message: types.message, state: FSMContext):
    await message.answer(text=hitalic("Спасибо за прохождение викторины"), reply_markup=ReplyKeyboardRemove())
    await state.finish()


