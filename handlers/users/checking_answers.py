from aiogram import types


async def func_answer1(message: types.message, str_ans1):
    if str_ans1 == "Георгия Победоносца":
        await message.answer(text='Вопрос 1:Правильный ответ!')
    else:
        await message.answer(text='Вопрос 1:К сожалению!')


async def func_answer2(message: types.message, str_ans2):
    if str_ans2 == "космический спускаемый аппарат - Союз ТМА-10":
        await message.answer(text='Вопрос 2:Правильный ответ!')
    else:
        await message.answer(text='Вопрос 2:К сожалению, неправильный ответ!')


async def func_answer3(message: types.message, str_ans3):
    if str_ans3 == "Великой Отечественной войне":
        await message.answer(text='Вопрос 2:Правильный ответ!')
    else:
        await message.answer(text='Вопрос 2:К сожалению, неправильный ответ!')
