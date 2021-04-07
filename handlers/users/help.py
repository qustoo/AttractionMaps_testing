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
        '/get_my_rating - Узнать свой рейтинг в викторине',
        '/save_my_location - Сохранить мою геолокацию',
        '/get_photo - Получить фотку достопримечательности',
        '/reset_encyclopedia - Начать энциклопедию сначала '
    ]
    # добавить энциклопедию и внутрь викторины поместить разные уровни сложности
    await message.answer('\n'.join(text))
