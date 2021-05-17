from aiogram.types import CallbackQuery, InputMediaPhoto

from keyboards.inline.callback_datas import quiz_photo_callback
from keyboards.inline.medium_keyboard import med_photo_keyboard2, med_photo_keyboard3, med_photo_keyboard4, \
    med_photo_keyboard5, med_photo_keyboard6, med_photo_keyboard7, med_photo_keyboard8, med_photo_keyboard9, \
    med_photo_keyboard10, med_photo_keyboard11, med_photo_keyboard12
from loader import dp, photo_db
from states.MachineStates_For_Quiz import QuizMedium

med_photo_quiz=['medium_question_1','medium_question_2','medium_question_3','medium_question_4','medium_question_5','medium_question_6','medium_question_7','medium_question_8','medium_question_9','medium_question_10','medium_question_11','medium_question_12','medium_question_13']

@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q1)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q2)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q3)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q4)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q5)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q6)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q7)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q8)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q9)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q10)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m1"),state= QuizMedium.Q13)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[1]), 'rb')),reply_markup=med_photo_keyboard2)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q2)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q3)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q4)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q5)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q6)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q7)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q8)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q9)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q10)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m2"),state= QuizMedium.Q13)
async def question_2(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[2]), 'rb')),reply_markup=med_photo_keyboard3)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q3)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q4)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q5)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q6)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q7)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q8)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q9)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q10)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m3"),state= QuizMedium.Q13)
async def question_3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[3]), 'rb')),reply_markup=med_photo_keyboard4)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m4"),state= QuizMedium.Q4)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m4"),state= QuizMedium.Q5)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m4"),state= QuizMedium.Q6)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m4"),state= QuizMedium.Q7)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m4"),state= QuizMedium.Q8)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m4"),state= QuizMedium.Q9)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m4"),state= QuizMedium.Q10)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m4"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m4"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m4"),state= QuizMedium.Q13)
async def question_3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[4]), 'rb')),reply_markup=med_photo_keyboard5)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m5"),state= QuizMedium.Q5)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m5"),state= QuizMedium.Q6)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m5"),state= QuizMedium.Q7)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m5"),state= QuizMedium.Q8)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m5"),state= QuizMedium.Q9)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m5"),state= QuizMedium.Q10)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m5"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m5"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m5"),state= QuizMedium.Q13)
async def question_3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[5]), 'rb')),reply_markup=med_photo_keyboard6)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m6"),state= QuizMedium.Q6)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m6"),state= QuizMedium.Q7)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m6"),state= QuizMedium.Q8)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m6"),state= QuizMedium.Q9)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m6"),state= QuizMedium.Q10)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m6"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m6"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m6"),state= QuizMedium.Q13)
async def question_3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[6]), 'rb')),reply_markup=med_photo_keyboard7)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m7"),state= QuizMedium.Q7)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m7"),state= QuizMedium.Q8)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m7"),state= QuizMedium.Q9)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m7"),state= QuizMedium.Q10)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m7"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m7"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m7"),state= QuizMedium.Q13)
async def question_3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[7]), 'rb')),reply_markup=med_photo_keyboard8)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m8"),state= QuizMedium.Q8)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m8"),state= QuizMedium.Q9)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m8"),state= QuizMedium.Q10)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m8"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m8"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m8"),state= QuizMedium.Q13)
async def question_3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[8]), 'rb')),reply_markup=med_photo_keyboard9)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m9"),state= QuizMedium.Q9)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m9"),state= QuizMedium.Q10)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m9"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m9"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m9"),state= QuizMedium.Q13)
async def question_3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[9]), 'rb')),reply_markup=med_photo_keyboard10)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m10"),state= QuizMedium.Q10)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m10"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m10"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m10"),state= QuizMedium.Q13)
async def question_3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[10]), 'rb')),reply_markup=med_photo_keyboard11)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m11"),state= QuizMedium.Q11)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m11"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m11"),state= QuizMedium.Q13)
async def question_3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[11]), 'rb')),reply_markup=med_photo_keyboard12)

@dp.callback_query_handler(quiz_photo_callback.filter(next="m12"),state= QuizMedium.Q12)
@dp.callback_query_handler(quiz_photo_callback.filter(next="m12"),state= QuizMedium.Q13)
async def question_3(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=med_photo_quiz[12]), 'rb')),reply_markup=None)


