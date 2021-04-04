import re

from aiogram import types

answer_test_1 = "Георгия Победоносца"
answer_test_2 = "космический спускаемый аппарат - Союз ТМА-10"
answer_test_3 = "Великой Отечественной войне"
answer_test_4 = "Бульвар Дружбы"


async def func_answer1(message: types.message, str_ans1):
    if str_ans1 == answer_test_1:
        await message.answer(text='Вопрос 1:Правильный ответ!')
    else:
        await message.answer(text='Вопрос 1:Неправильный ответ!')


async def func_answer2(message: types.message, str_ans2):
    if str_ans2 == answer_test_2:
        await message.answer(text='Вопрос 2:Правильный ответ!')
    else:
        await message.answer(text='Вопрос 2:Неправильный ответ!')


async def func_answer3(message: types.message, str_ans3):
    if str_ans3 == answer_test_3:
        await message.answer(text='Вопрос 3:Правильный ответ!')
    else:
        await message.answer(text='Вопрос 3:Неправильный ответ!')


async def func_answer4(message: types.message, str_ans3):
    if str_ans3 == answer_test_4:
        await message.answer(text='Вопрос 4:Правильный ответ!')
    else:
        await message.answer(text='Вопрос 4:Неправильный ответ!')

