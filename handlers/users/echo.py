from aiogram import types
from loader import dp


# Декоратор
# Сюда летят только текстовые сообщения
@dp.message_handler(content_types=types.ContentType.TEXT)
async def bot_echo(message: types.Message):
    # Получил чат айди и текст сообщения
    chat_id = message.chat.id
    text = message.text

    # Импортируем бота
    from loader import bot

    await bot.send_message(chat_id=chat_id, text=text)

    # Второй вариант без chat_id
    # await message.answer(text=text)
