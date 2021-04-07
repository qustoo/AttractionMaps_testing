from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from data.locations import find_locale
from keyboards.default import locations_for_button
from loader import dp, db
from utils.misc.calc_for_distance import New_Attract
from utils.misc.calc_for_distance import choose_nearest


# заставляем пользователя отправить локацию
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
        # передам клаву под локацию
        reply_markup=locations_for_button.keyboard,
    )
    await message.answer(f"Давайте условимся, что вы будто уже пришли к локации, "
                         f"которую мы вам отправили, и следующая"
                         f"локация будет ближайшей к предыдущий"
                         f"\n<b>Это сделано с целью провести клиента через весь город<\b>")


# Отказная от отправления локации
@dp.message_handler(text="Отмена")
async def quit_get_attract(message: types.Message):
    await message.answer(f"Вы отказались от ближайшей достопримечательности!\n"
                         "чтобы вернуться к списку команда нажмите /help", reply_markup=ReplyKeyboardRemove())


# получили уже локацию
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(message: types.Message, state: FSMContext):
    # получение координат из бд юзера
    # latt,lonn = db.get_coordinates(id=message.from_user.id)
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closes_places = choose_nearest(message, latitude, longitude, New_Attract.copy())
    if not closes_places:
        await message.answer("Список мест для посещения пуст!", reply_markup=ReplyKeyboardRemove())
        return

    # await message.answer(f"\n\n start_position,last_position = {new_start} {new_last}\n\n")

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
        # Обновляем данные в БД
        db.update_lat(id=message.from_user.id, lat=place_location["lat"])
        db.update_lon(id=message.from_user.id, lon=place_location["lon"])
    await message.answer("Чтобы перейти к следующией ближайшей достопримечательности нажмите /next")
    await message.answer("Для завершения нажмите /finish")


# получаем
@dp.message_handler(Command("next"))
async def go_to_nex_location(message: types.Message):
    new_lat, new_lon = db.get_coordinates(id=message.from_user.id)
    closes_places = choose_nearest(message, new_lat, new_lon, New_Attract)
    if not closes_places:
        await message.answer(text=
                             "Список мест для посещения закончилось!"
                             "Для завершения нажмите /finish")
        return

    text_format = "{place_name}.\n" \
                  "Маршрут: <a href='{url}'>Google</a>\n" \
                  "Расстояние до объекта: {distance:.2f} км"
    text = "\n\n".join(
        [
            text_format.format(place_name=place_name, url=url, distance=distance)
            for place_name, distance, url, place_location in closes_places
        ]
    )
    # получаем имя локации, к которой нас отправили
    # name_of_location = re.match('^[^.]*', text).group(0)
    # получаем тьюпл локации
    # tuple_location, iteration = find_locale(name_of_location)
    '''
    await message.answer(f"Имя локации = {name_of_location}\n"
                         f"\nlon = {tuple_location.get('lon')}"
                         f"\nlat = {tuple_location.get('lat')}") 
    '''

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
        # Обновляем данные в БД
        db.update_lat(id=message.from_user.id, lat=place_location["lat"])
        db.update_lon(id=message.from_user.id, lon=place_location["lon"])
    await message.answer("Чтобы перейти к следующией ближайшей достопримечательности нажмите /next")
    await message.answer("Для завершения нажмите /finish")


# финишируем
@dp.message_handler(Command("finish"))
async def finish_go_to_the_attractions(message: types.Message):
    await message.answer("Спасибо за пользование нашими командами", reply_markup=ReplyKeyboardRemove())
