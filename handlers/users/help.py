from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


# список соответствующие команд
@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/quiz - Начать викторину(в тестовом режиме)',
        '/quiz_easy - Начать викторину в легком режиме',
        '/show_on_map_attractions - Показать ближайшую достопримечательность',
        '/items - Покупка различных карт',
        '/get_photo - Получить фотку достопримечательности'
    ]
    # добавить энциклопедию и внутрь викторины поместить разные уровни сложности
    await message.answer('\n'.join(text))
