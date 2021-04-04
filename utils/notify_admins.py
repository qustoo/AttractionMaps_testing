import logging

from aiogram import Dispatcher

from data.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            # отправляем сообщение админам о готовности бота
            await dp.bot.send_message(admin, "Бот Запущен и готов к работе!")

        except Exception as err:
            logging.exception(err)
