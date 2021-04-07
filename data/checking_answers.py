from aiogram import types
from loader import db

Answer_List_Question_Easy = [
    "Георгия Победоносца",
    "космический спускаемый аппарат - Союз ТМА-10",
    "Великой Отечественной войне",
    "Бульвар Дружбы",
    "Тихий Дон",
    "Бронзовый век",
    "был владельцем спиртоводочного завода",
    "Старообрядчество",
    "2018г",
    "Библиотека ЮФУ(РГУ)"

]


async def func_answer1(message: types.message, str_ans1):
    if str_ans1 == Answer_List_Question_Easy[0]:
        await message.answer(text='Вопрос 1:Правильный ответ!')
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 1.0)
    else:
        await message.answer(text='Вопрос 1:Неправильный ответ!')


async def func_answer2(message: types.message, str_ans2):
    if str_ans2 == Answer_List_Question_Easy[1]:
        await message.answer(text='Вопрос 2:Правильный ответ!')
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 1.0)
    else:
        await message.answer(text='Вопрос 2:Неправильный ответ!')


async def func_answer3(message: types.message, str_ans3):
    if str_ans3 == Answer_List_Question_Easy[2]:
        await message.answer(text='Вопрос 3:Правильный ответ!')
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 1.0)
    else:
        await message.answer(text='Вопрос 3:Неправильный ответ!')


async def func_answer4(message: types.message, str_ans3):
    if str_ans3 == Answer_List_Question_Easy[3]:
        await message.answer(text='Вопрос 4:Правильный ответ!')
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 1.0)
    else:
        await message.answer(text='Вопрос 4:Неправильный ответ!')


async def func_answer5(message: types.message, str_ans4):
    if str_ans4 == Answer_List_Question_Easy[4]:
        await message.answer(text='Вопрос 5:Правильный ответ!')
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 1.0)
    else:
        await message.answer(text='Вопрос 5:Неправильный ответ!')


async def func_answer6(message: types.message, str_ans5):
    if str_ans5 == Answer_List_Question_Easy[5]:
        await message.answer(text='Вопрос 6:Правильный ответ!')
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 1.0)
    else:
        await message.answer(text='Вопрос 6:Неправильный ответ!')


async def func_answer7(message: types.message, str_ans6):
    if str_ans6 == Answer_List_Question_Easy[6]:
        await message.answer(text='Вопрос 7:Правильный ответ!')
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 1.0)
    else:
        await message.answer(text='Вопрос 7:Неправильный ответ!')


async def func_answer8(message: types.message, str_ans7):
    if str_ans7 == Answer_List_Question_Easy[7]:
        await message.answer(text='Вопрос 8:Правильный ответ!')
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 1.0)
    else:
        await message.answer(text='Вопрос 8:Неправильный ответ!')


async def func_answer9(message: types.message, str_ans8):
    if str_ans8 == Answer_List_Question_Easy[8]:
        await message.answer(text='Вопрос 9:Правильный ответ!')
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 1.0)
    else:
        await message.answer(text='Вопрос 9:Неправильный ответ!')


async def func_answer10(message: types.message, str_ans9):
    if str_ans9 == Answer_List_Question_Easy[9]:
        await message.answer(text='Вопрос 10:Правильный ответ!')
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 1.0)
    else:
        await message.answer(text='Вопрос 10:Неправильный ответ!')
