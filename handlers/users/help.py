from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


# список соответствующие команд
@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    # '/items - Покупка различных карт',
    text = [
        'Список команд: ',
        '/quiz_easy - Начать викторину на легком уровне сложности',
        '/quiz_medium - Начать викторину на среднем уровне сложности',
        '/quiz_hard - Начать викторину на тяжелом уровне сложности',
        '/encyclopedia - Энциклопедия',
        '/show_on_map_attractions - Показать ближайшую достопримечательность, и построить паутину маршрута',
        '/reset_map - Сбросить маршрут прохождения'
        '/buy_map - Купить одну из карту двух районов',
        '/get_my_rating - Узнать свой рейтинг в викторине',
        '/get_rating - Топ по рейтингу',
        '/get_photo - Получить фотку достопримечательности',

    ]

    # добавить энциклопедию и внутрь викторины поместить разные уровни сложности
    await message.answer('\n'.join(text))