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
    await message.answer(f'Здравствуйте, {message.from_user.full_name}! 😎😉'
                         f'\nДля получения списка доступных команд нажми /help')
    bot.send_photo(chat_id=message.chat.id,photo=
                   'https://sun9-54.userapi.com/impg/1O_sfsIKAevSAu491ceTr5NeGqe3aTa79Z560w/HLI396NWNdo.jpg?size=2560x1440&quality=96&sign=50d5e79815f9784d3835a7f776f84c8a&type=album'
                   )
