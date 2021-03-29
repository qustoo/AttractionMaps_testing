from aiogram.types import ContentType, Message, MediaGroup
from aiogram.dispatcher.filters import Command

from loader import dp, bot


@dp.message_handler(content_types=ContentType.PHOTO)
async def find_id_photo(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def find_id_video(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("get_photo"))
async def send_atr(message: Message):
    url1 = "https://gos.ifrigate.ru/wp-content/uploads/main2.jpg"
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=url1, caption=f"Администрация!/n" + f"Если хочешь больше фото, то нажми /more_attractions")


@dp.message_handler(Command("more_attractions"))
async def more_attractions(message: Message):
    albums = MediaGroup()
    url1 = "https://gos.ifrigate.ru/wp-content/uploads/main2.jpg"
    url2 = "http://hotel7nebo.ru/images/page/43.jpg"
    url3 = "https://img.geliophoto.com/rostov/12_rostov.jpg"
    url4 = "https://www.yuga.ru/media/0e/29/pr_budennovskogo_rostov-na-donu_ponomar__iic6nxi.jpg"
    albums.attach_photo(url1)
    albums.attach_photo(url2)
    albums.attach_photo(url3)
    albums.attach_photo(url4)

    await message.answer_media_group(media=albums)
