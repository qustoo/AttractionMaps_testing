from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from data.locations import Attractions
from keyboards.default import locations_for_button
from loader import dp, db
from utils.misc.calc_for_distance import SetTrueForAllAttractions
from utils.misc.calc_for_distance import choose_nearest


# Просим пользователя отправить свою геопозицию
@dp.message_handler(Command("show_on_map_attractions"))
async def show_on_map(message: types.Message):
    await message.answer(
        f"Здравствуйте,{message.from_user.full_name}.\n"
        f"Чтобы показать ближайшую достопримечательность,отправьте нам свое местоположение"
        "нажав на кнопку ниже\n\n"
        "Давайте условимся, что вы будто уже пришли к локации,"
        "которую мы вам отправили, и следующая "
        "локация будет ближайшей к предыдущий локации."
        "\n" + hbold("Это сделано с целью провести клиента через весь город"),
        reply_markup=locations_for_button.keyboard,
    )

    if db.select_user(id=message.from_user.id)[-2] != 0.0 and db.select_user(id=message.from_user.id)[-3] != 0.0:
        db.update_lat(id=message.from_user.id, lat=float(0.0))
        db.update_lon(id=message.from_user.id, lon=float(0.0))


# db.update_lat(id=message.from_user.id, lat=0.0)
# db.update_lon(id=message.from_user.id, lon=0.0)
# Удаляем старые координаты пользователя


# Устанавливаем в каждом месте обход - True
@dp.message_handler(Command("reset_map"))
async def reset_map(message: types.Message):
    SetTrueForAllAttractions(Attractions)
    await message.answer(text=
                         f'Карта была успешно сброшена.\n'
                         'Чтобы начать поиск локации заново, нажми ' + hbold('/show_on_map_attractions'))


# Отказ отправления геопозиции пользователя
@dp.message_handler(text="Отмена")
async def quit_get_attract(message: types.Message):
    await message.answer(f"Вы отказались от ближайшей достопримечательности!\n"
                         'чтобы вернуться к списку команда нажмите' + hbold('/help'),
                         reply_markup=ReplyKeyboardRemove())


# Получили от юзера его местоположение
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(message: types.Message, state: FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude
    closes_places = choose_nearest(latitude, longitude, Attractions)
    # если список пуст
    if not closes_places:
        await message.answer("Список мест для посещения пуст!", reply_markup=ReplyKeyboardRemove())
        return

    text_format = "{place_name}.\n" \
                  "Маршрут: <a href='{url}'>Google</a>\n" \
                  "Расстояние до объекта: {distance:.2f} км\n"
    text = "\n\n".join(
        [
            text_format.format(place_name=place_name, url=url, distance=distance)
            for place_name, distance, url, place_location in closes_places
        ]
    )

    await message.answer(f'Спасибо за отправку!\n'
                         f'Ближайшая к вам:\n'
                         f'{text}',
                         disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())
    for place_name, distance, url, place_location in closes_places:
        # отправляем пользователю объект по его точному местоположению
        await message.answer_location(
            latitude=place_location["lat"],
            longitude=place_location["lon"]
        )
        # Обновляем данные юзера в БД
        db.update_lat(id=message.from_user.id, lat=place_location["lat"])
        db.update_lon(id=message.from_user.id, lon=place_location["lon"])
    await message.answer(text='Чтобы перейти к следующией ближайшей достопримечательности нажмите ' + hbold('/next'))
    await message.answer(text='Для завершения нажмите ' + hbold('/finish'))
    # print(closes_places)


# Переходим к следующему объекту.
@dp.message_handler(Command("next"))
async def go_to_nex_location(message: types.Message):
    new_lat, new_lon = db.get_coordinates(id=message.from_user.id)
    closes_places = choose_nearest(new_lat, new_lon, Attractions)
    # если список пуст
    if not closes_places:
        await message.answer(text=
                             'Список мест для посещения закончилось!\n'
                             'Для завершения нажмите /finish')
        return

    text_format = "{place_name}.\n" \
                  "Маршрут: <a href='{url}'>Google</a>\n" \
                  "Расстояние до объекта: {distance:.2f} км"
    text_next = "\n\n".join(
        [
            text_format.format(place_name=place_name, url=url, distance=distance)
            for place_name, distance, url, place_location in closes_places
        ]
    )

    await message.answer(f'Спасибо за отправку!\n'
                         f'Ближайшая к вам:\n\n'
                         f'{text_next}',
                         disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for place_name, distance, url, place_location in closes_places:
        await message.answer_location(
            # отправляем пользователю объект по его точному местоположению
            latitude=place_location["lat"],
            longitude=place_location["lon"]
        )
        # Обновляем данные юзера в БД
        db.update_lat(id=message.from_user.id, lat=place_location["lat"])
        db.update_lon(id=message.from_user.id, lon=place_location["lon"])
    await message.answer(text='Чтобы перейти к следующией ближайшей достопримечательности нажмите ' + hbold('/next'))
    await message.answer(text='Для завершения нажмите ' + hbold('/finish'))
    # print(closes_places)


# Финишируем проход по локациям
@dp.message_handler(Command("finish"))
async def finish_go_to_the_attractions(message: types.Message):
    await message.answer(text="\n".join(
        [
            'Для сброса карты нажми ' + hbold('/reset_map')
        ]
    ), reply_markup=ReplyKeyboardRemove())
