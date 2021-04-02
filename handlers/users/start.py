from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from utils.misc import rate_limit


# 2.04 опробовали git
# abra
# принял изменения


# лимит на раз в 5 сек
@rate_limit(limit=5)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Здра!!!!вствуй, {message.from_user.full_name}! 😎😉'
                         f'\nДля получения списка д!!!оступных коман!!д нажми /help')
