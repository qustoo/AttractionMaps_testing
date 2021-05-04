from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.callback_datas import place_callback
from quiz_all_files.Quiz_Questions.questions_quiz import Easy_Array_Questions
from data.checking_answers import func_answer1, func_answer2, func_answer3, func_answer4, func_answer5, func_answer6, \
    func_answer7, func_answer8, func_answer9, func_answer10
from keyboards.default import menu_for_easy_quizing
from loader import dp, photo_db
from aiogram import types
from keyboards.inline.quiz_keyboard import choice_r_q
from aiogram.types import CallbackQuery

from states.MachineStates_For_Quiz import QuizEasy


@dp.message_handler(place_callback.filter(item_name="sov_r_q"), state=None)
async def enter_easy_test(message: types.Message):
    # присылаем фотку и клаву
    await message.answer(text="Вопрос 1:\n")
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_1'), 'rb'))
    await message.answer(Easy_Array_Questions[0], reply_markup=menu_for_easy_quizing.menu_0)
    await QuizEasy.Q1.set()
