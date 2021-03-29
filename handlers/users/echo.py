from aiogram import types
from loader import dp


# Декоратор
# Сюда летят только текстовые сообщения
@dp.message_handler(content_types=types.ContentType.TEXT)
async def bot_echo(message: types.Message):
    # Импортируем бота
    from loader import bot

    # Получил чат айди и текст сообщения
    await bot.send_message(chat_id=message.chat.id, text=('Эхо' + message.text))

    # Второй вариант без chat_id
    # await message.answer(text=text)
