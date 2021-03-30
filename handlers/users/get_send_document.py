from loader import dp
from aiogram import types


@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def get_audio(message: types.Message):
    # получаем айди
    file = message.audio.file_id
