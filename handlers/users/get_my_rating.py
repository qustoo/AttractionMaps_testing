from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command("get_my_rating"))
async def view_rating_user(message: types.Message):
    # внутри бд такой порядок переменных
    # (id,name,email,lat,lon,rating)
    await message.answer(f'Ваш рейтинг в системе викторины = {db.select_user(id=message.from_user.id)[-1]}')
    # db.update_rating(id=message.from_user.id, rating=1)
    # await message.answer(f'Ваш рейтинг после увеличения на 1 в системе викторины = {db.select_user(id=message.from_user.id)[-1]}')
