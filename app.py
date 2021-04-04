from loader import db


async def on_startup(dp):
    import filters
    import middlewares
    # Установка фильтров и мидлваров
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    # создаем бд юзера
    try:
        db.create_table_users()
    except Exception as error:
        print(f'Error = {error}')
    # Чистим таблицу
    db.delete_all_users()
    # печатаем пользователей бд
    print('Пользователи = ', db.select_all_users())
    # отправка сообщения админам
    await on_startup_notify(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
