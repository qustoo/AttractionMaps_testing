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
        '/encyclopedia - Энциклопедия',
        '/show_on_map_attractions - Показать ближайшую достопримечательность, и построить паутину маршрута',
        '/buy_map - Купить ориагинальную карту двух районов на выбор',
        '/get_my_rating - Узнать свой рейтинг в викторине',
        '/get_photo - Получить фотку достопримечательности',
    ]

    # добавить энциклопедию и внутрь викторины поместить разные уровни сложности
    await message.answer('\n'.join(text))
