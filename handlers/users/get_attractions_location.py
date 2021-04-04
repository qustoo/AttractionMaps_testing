from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import locations_for_button
from loader import dp
from utils.misc.calc_for_distance import choose_nearest


# заставляем пользователя отправить локацию
@dp.message_handler(Command("show_on_map_attractions"))
async def show_on_map(message: types.Message):
    await message.answer(
        f"Здравствуйте, {message.from_user.full_name}.\n"
        f"Чтобы показать ближайшую достопримечательность,отправьте нам свое местоположение"
        "нажав на кнопку ниже",
        # передам клаву под локацию
        reply_markup=locations_for_button.keyboard,

    )


# Отказная
@dp.message_handler(text="Отмена")
async def quit_get_attract(message: types.Message):
    await message.answer(f"Вы отказались от ближайшей достопримечательности!\n"
                         "чтобы вернуться к списку команда нажмите /help", reply_markup=ReplyKeyboardRemove())


# получили уже локацию
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closes_places = choose_nearest(location)

    text_format = "{place_name}.\n" \
                  "Маршрут: <a href='{url}'>Google</a>\n" \
                  "Расстояние до объекта: {distance:.2f} км"
    text = "\n\n".join(
        [
            text_format.format(place_name=place_name, url=url, distance=distance)
            for place_name, distance, url, place_location in closes_places
        ]
    )
    await message.answer(f'Спасибо за отправку!\n'
                         f'Ближайшая к вам:\n'
                         f'{text}',
                         disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove()
                         # Добавил reply_markup=ReplyKeyboardRemove(),
                         # т.е. убираем клаву после отправки геопозиции
                         )
    for place_name, distance, url, place_location in closes_places:
        await message.answer_location(
            latitude=place_location["lat"],
            longitude=place_location["lon"]
        )
