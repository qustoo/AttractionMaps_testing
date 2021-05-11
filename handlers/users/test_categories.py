from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from keyboards.default import locations_for_button
from loader import dp, db
from utils.misc.calc_for_distance import choose_nearest

ListCallbackPlaces = [
    ("Церковь Екатерины Великомученицы", {
        "lat": 47.200084,
        "lon": 39.629942,
        "bypass": True
    }),
    ("Церковь Георгия Победоносца",
     {
         "lat": 47.208686,
         "lon": 39.622199,
         "bypass": True
     }),
    # ("Музей Иоанна Кронштадтского", {
    #     "lat": 47.250313,
    #     "lon": 39.695835,
    #     "bypass": True
    # }),
    ("Музей русско-армянской дружбы", {
        "lat": 47.229132,
        "lon": 39.765032,
        "bypass": True
    })]

type_of_attraction = CallbackData("ComingSoon", "type_place", "name_place")
next_or_finish_locations = CallbackData("ComingSoon", "next")

choiсe_attractions = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Церковь",
            # callback_data="place:Church:2155"
            callback_data=type_of_attraction.new(type_place="Church", name_place="Церковь")
        )
    ],
    [
        InlineKeyboardButton
            (
            text="Музей",
            callback_data=type_of_attraction.new(type_place="Museum", name_place="Музей")
        )
    ],
    [
        InlineKeyboardButton
            (
            text="Отмена",
            callback_data="cancel_choice_attractions")
    ]

])

NextOrFinishLocationKeyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="next",
            # callback_data="place:Church:2155"
            callback_data=next_or_finish_locations.new(next="True")
        ),
        InlineKeyboardButton(
            text="finish",
            callback_data=next_or_finish_locations.new(next="False"))
    ]

])


@dp.message_handler(Command("inline_locations"), state=None)
async def show_on_map(message: types.Message, state: FSMContext):
    await message.answer(
        f"Здравствуйте,{message.from_user.full_name}.\n",
        reply_markup=locations_for_button.keyboard)


@dp.message_handler(text="Отмена")
async def exit_locations(message: types.Message, state: FSMContext):
    await message.answer("Вы отказались\n", reply_markup=ReplyKeyboardRemove())
    await state.finish()


# state=CallBackLocation.Q1,
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def go_to_objet(message: types.Message, state: FSMContext):
    await message.answer(text="Вы отправили локацию", reply_markup=ReplyKeyboardRemove())
    await message.answer("Выберите объект, который вам интересен", reply_markup=choiсe_attractions)
    # заносим в машину координаты пользователя, которые он отправил
    await state.update_data(locations_from_user=(message.location.latitude, message.location.longitude))


@dp.callback_query_handler(type_of_attraction.filter(type_place="Church"))
async def exit_locations(call: CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    await call.answer(cache_time=1)
    # заносим в Машину состояний имя того объекта, на который он нажал
    await state.update_data(lastLocations=callback_data.get('name_place'))
    # получаем нужную информацию об объекте(имя,ссылка,координаты)
    closes_places = choose_nearest(data.get("locations_from_user")[0], data.get("locations_from_user")[-1],
                                   ListCallbackPlaces, callback_data.get('name_place'))
    if not closes_places:
        New_Keyboard = InlineKeyboardMarkup(row_width=2,inline_keyboard=[])
        New_Keyboard.inline_keyboard.append({choiсe_attractions["inline_keyboard"][1][0]})
        New_Keyboard.inline_keyboard.append({choiсe_attractions["inline_keyboard"][-1][-1]})
        await call.message.edit_text(
            text="Список мест типа " + "'callback_data.get('name_place')'" + " для посещения пуст!\n",
            reply_markup=New_Keyboard)
    text_format = "{place_name}.\n" \
                  "Маршрут: <a href='{url}'>Google</a>\n" \
                  "Расстояние до объекта: {distance:.2f} км\n"
    text = "\n\n".join(
        [
            text_format.format(place_name=place_name, url=url, distance=distance)
            for place_name, distance, url, place_location in closes_places
        ]
    )

    await call.message.answer(f'Спасибо за отправку!\n'
                              f'Ближайшая к вам:\n'
                              f'{text}',
                              disable_web_page_preview=True)
    for place_name, distance, url, place_location in closes_places:
        # отправляем пользователю объект по его точному местоположению
        await call.message.answer_location(
            latitude=place_location["lat"],
            longitude=place_location["lon"]
        )
        # Обновляем данные юзера в БД
        db.update_lat(id=call.from_user.id, lat=place_location["lat"])
        db.update_lon(id=call.from_user.id, lon=place_location["lon"])

    await call.message.answer(text="Если вы хотите продолжить, нажмите кнопку ниже\n",
                              reply_markup=NextOrFinishLocationKeyboard)


@dp.callback_query_handler(type_of_attraction.filter(type_place="Museum"))
async def exit_locations(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=1)
    data = await state.get_data()
    await state.update_data(lastLocations=callback_data.get('name_place'))
    # await call.message.answer(text=f"{callback_data.get('type_place')} {callback_data.get('name_place')}")
    # await call.message.answer(
    #     text=str(data.get("locations_from_user")[0]) + " " + str(data.get("locations_from_user")[-1]))
    closes_places = choose_nearest(data.get("locations_from_user")[0], data.get("locations_from_user")[-1],
                                   ListCallbackPlaces, callback_data.get('name_place'))
    if not closes_places:
        New_Keyboard = InlineKeyboardMarkup(row_width=2,inline_keyboard=[])
        New_Keyboard.inline_keyboard.append({choiсe_attractions["inline_keyboard"][0][0]})
        New_Keyboard.inline_keyboard.append({choiсe_attractions["inline_keyboard"][-1][-1]})
        await call.message.edit_text(
            text="Список мест типа " + "'callback_data.get('name_place')'" + " для посещения пуст!\n",
            reply_markup=New_Keyboard)

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

    await call.message.answer(f'Спасибо за отправку!\n'
                              f'Ближайшая к вам:\n'
                              f'{text}',
                              disable_web_page_preview=True)
    for place_name, distance, url, place_location in closes_places:
        # отправляем пользователю объект по его точному местоположению
        await call.message.answer_location(
            latitude=place_location["lat"],
            longitude=place_location["lon"]
        )
        # Обновляем данные юзера в БД
        db.update_lat(id=call.from_user.id, lat=place_location["lat"])
        db.update_lon(id=call.from_user.id, lon=place_location["lon"])

    await call.message.answer(text="Если вы хотите продолжить, нажмите кнопку ниже\n",
                              reply_markup=NextOrFinishLocationKeyboard)

    # await state.finish()


@dp.callback_query_handler(text="cancel_choice_attractions")
async def cancel_choice_attractions(call: CallbackQuery):
    await call.message.edit_text("Вы отказались.")
    await call.message.edit_reply_markup()


@dp.callback_query_handler(next_or_finish_locations.filter(next="True"))
async def next_place(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=1)
    data = await state.get_data()
    user = db.select_user(id=call.from_user.id)
    new_lat, new_lon = db.get_coordinates(id=call.from_user.id)
    closes_places = choose_nearest(new_lat, new_lon, ListCallbackPlaces, name_object=data.get('lastLocations'))
    if not closes_places:
        await call.message.edit_text(text='Список мест для посещения закончилось!\n')
        await call.message.edit_reply_markup()
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

    await call.message.answer(f'Спасибо за отправку!\n'
                              f'Ближайшая к вам:\n\n'
                              f'{text_next}',
                              disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for place_name, distance, url, place_location in closes_places:
        await call.message.answer_location(
            # отправляем пользователю объект по его точному местоположению
            latitude=place_location["lat"],
            longitude=place_location["lon"]
        )
        # Обновляем данные юзера в БД
        db.update_lat(id=call.from_user.id, lat=place_location["lat"])
        db.update_lon(id=call.from_user.id, lon=place_location["lon"])
    await call.message.answer(text="Если вы хотите продолжить, нажмите кнопку ниже\n",
                              reply_markup=NextOrFinishLocationKeyboard)
    # await call.message.edit_reply_markup(reply_markup=NextOrFinishLocationKeyboard)
    # await call.message.edit_text(text="Если вы хотите продолжить, нажмите кнопку ниже\n")


@dp.callback_query_handler(next_or_finish_locations.filter(next="False"))
async def Finish_InlineLocations(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_text(text="Спасибо")
