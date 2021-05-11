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


async def check_answer_easy(message: types.Message, str_ans, num):

    if str_ans == Answer_List_Question_Easy[num - 1]:
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
        return "Вопрос " + str(num) + ": Правильный ответ!"
    else:
        return "Вопрос " + str(num) + ": Неправильный ответ!"
