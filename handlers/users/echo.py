from aiogram import types
from loader import dp


# Декоратор
# Сюда летят только текстовые сообщения
# Upd : сюда летит всфе!
@dp.message_handler(content_types=types.ContentTypes.ANY)
async def bot_echo(message: types.Message):
    # Импортируем бота
    from loader import bot

    # Получил чат айди и текст сообщения
    await bot.send_message(chat_id=message.chat.id, text = "\n".join([
        "Бла-бла я ничего не понимаю!",
        "Лучше нажми на /help и выбери интересующую команду!"])
    )

    # Второй вариант без chat_id
    # await message.answer(text=text)
