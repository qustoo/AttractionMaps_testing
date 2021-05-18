from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command("get_my_rating"))
async def get_my_rating(message: types.Message):
    rate = db.get_rating_total(message.from_user.id)
    await message.answer("Ваш рейтинг: " + str(rate))


@dp.message_handler(Command("get_rating"))
async def view_rating_user(message: types.Message):
    users = db.select_all_users()
    tmp_user_rating = {}
    for i in users:
        tmp_user_rating[i[1]] = db.get_rating_total(i[0])
    sorted_user_rating = {}
    sorted_users = sorted(tmp_user_rating, key=tmp_user_rating.get, reverse=True)
    for w in sorted_users:
        sorted_user_rating[w] = tmp_user_rating[w]

    output_string = ""
    index = 1
    for user in sorted_user_rating:
        output_string += str(index) + ': ' + user + " - " + str(sorted_user_rating[user])[0] + str("\n")
        index += 1
    await message.answer(text="Топ пользователей:\n" + output_string)
