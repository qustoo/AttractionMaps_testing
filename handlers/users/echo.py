from aiogram import types
from loader import dp, bot


# Декоратор
# Сюда летят только текстовые сообщения
# Upd : сюда летит всфе!
@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def get_audio(message: types.Message):
    # получаем айди
    file = message.audio.file_id

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def bot_echo(message: types.Message):
    await message.answer(text="\n".join([
        "Бла-бла я ничего не понимаю!",
        "Лучше нажми на /help и выбери интересующую команду!"]))
