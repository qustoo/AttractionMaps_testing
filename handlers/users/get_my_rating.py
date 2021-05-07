from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command("get_rating"))
async def view_rating_user(message: types.Message):
    # внутри бд такой порядок переменных
    # (id,name,email,lat,lon,rating)
    await message.answer(f'Ваш рейтинг в системе викторины = {db.select_user(id=message.from_user.id)[-1]}')
    list_of_users = [(434354, 'Jaroslaw', 3.0),
                     (245636, 'Daria', 8.0),
                     (234236, 'Vika', 5.0),
                     (326267, 'Nastya', 9.0)]
    # выборка всех пользователей из бд db.select_all_users()
    # словарь для хранения переменных в виде: Имя - Рейтинг
    temp_dict_users = {}

    # заполняем словарь именами и рейтингом
    for i in list_of_users:
        temp_dict_users[i[1]] = i[-1]

    # формируем на лету новый словарь, сортируем по убыванию, от наибольшего к наименьшему рейтингу
    dict_rating_users = {k: temp_dict_users[k] for k in sorted(temp_dict_users, key=temp_dict_users.get, reverse=True)}

    answer_str = ""
    index = 1
    # формируем готовую строчку c местом, именем и рейтингом
    for user in dict_rating_users.items():
        answer_str = answer_str + str(index) + ':' + ' ' + user[0] + ' - ' + str(user[1]) + '\n'
        index += 1
    # Отправлую лишь одну строчку пользователю чтобы не присылать 100 сообщений со звуком уведомления
    await message.answer(text='Топ Рейтинга пользователей:\n'
                              f'{answer_str}')
