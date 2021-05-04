from db import do_db_photo
from loader import db
from loader import photo_db
import filters
import middlewares
from utils.notify_admins import on_startup_notify


async def on_startup(dp):
    # Установка фильтров и мидлварей
    filters.setup(dp)
    middlewares.setup(dp)

    # создаем бд юзера
    try:
        db.create_table_users()
    except Exception as error:
        print(f'Error = {error}')
    # Чистим БД юзеров
    # db.delete_all_users()

    # создаем бд фотки
    try:
        photo_db.create_table_photos()
    except Exception as error:
        print(f'Error = {error}')
    # Чистим БД фоток
    photo_db.delete_all_photos()
    # вносим изначально в бд фотки
    do_db_photo(photo_db)
    print('\nПользователи = ', db.select_all_users())
    print('--------------')
    print('\nФоточки = ', photo_db.select_all_photos())
    # отправка сообщения админам
    await on_startup_notify(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
