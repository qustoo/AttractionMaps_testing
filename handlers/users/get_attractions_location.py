from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default import locations_for_button
from loader import dp
from utils.misc.calc_for_distance import choose_nearest


@dp.message_handler(Command("show_attractions"))
async def show_on_map(message: types.Message):
    await message.answer(
        f"Здравствуйте, {message.from_user.full_name}.\n"
        f"Чтобы показать ближайшую достопримечательность,отправьте нам свое местоположение"
        "нажав на кнопку ниже",
        reply_markup=locations_for_button.keyboard,


    )


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def go_to_local(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    atract_nearest = choose_nearest(location)

    text_format = "Название: {attract_name}. <a href ='{url}'>Google</a>\n Расстояние равно: {distance:.1f} км"
    new_text = "\n\n".join(
        [
            ##text_format.format(atract_name=attract_name, url=url, distance=distance)
            # for atract_name, url, distance, atract_local in atract_nearest

        ]
    )

    await message.answer(f"Cпасибо за ответ\n"
                         "Коордитаны:\n"
                         f"Широта: {latitude}\n"
                         f"Долгота:{longitude}\n\n"
                         "Ближайшее к вам будет:"
                         f"{new_text}",
                         disable_web_page_preview=True
                         )
    for atract_name, url, distance, atract_local in atract_nearest:
        await message.answer_location(
            latitude=atract_local["lat"],
            longitude=atract_local["lon"]
        )
