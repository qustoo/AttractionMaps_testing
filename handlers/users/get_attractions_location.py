from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from data.locations import Attractions

from keyboards.default import KeyboardsToSendLocations
from keyboards.default.KeyboardsToSendLocations import TypeObject, NextOrFinishProgressMap, SelectTypeAttractions, \
    NextOrFinishLocationKeyboard
from loader import dp, db
from utils.misc.calc_for_distance import choose_nearest, SetTrueForAllAttractions

# Заносим кнопки в локальное пространство имен
global_buttons = [SelectTypeAttractions.inline_keyboard[0],
                  SelectTypeAttractions.inline_keyboard[1],
                  SelectTypeAttractions.inline_keyboard[2],
                  SelectTypeAttractions.inline_keyboard[3],
                  SelectTypeAttractions.inline_keyboard[4],
                  SelectTypeAttractions.inline_keyboard[5],
                  SelectTypeAttractions.inline_keyboard[6]
                  ]


# Устанавливаем в каждом месте обход - True
@dp.message_handler(Command("reset_map"))
async def reset_map(message: types.Message):
    SetTrueForAllAttractions(Attractions)
    await message.answer(text=f'Карта была успешно сброшена.\n')


# метод нахождения индекса кнопки и её удаление
async def RemoveButtonsInInlineKeyboard(closes_places, call: CallbackQuery, callback_data: dict, number_to_remove):
    # удаляем кнопку, если объекта с таким именем не существует
    if global_buttons[int(number_to_remove)] in SelectTypeAttractions.inline_keyboard:
        SelectTypeAttractions.inline_keyboard.pop(
            SelectTypeAttractions.inline_keyboard.index(global_buttons[int(number_to_remove)]))
    await call.message.edit_text(
        text="Список мест типа " + callback_data.get('name_place') + " для посещения пуст!\n",
        reply_markup=SelectTypeAttractions)


# формируем строку, которую отправляем пользователю + отравляем локацию объекта + обновляем данные в БД и присылает клавиатуру с 'next/finish'
async def SendToUserLocationUpdateDataBase(closes_places, call: CallbackQuery):
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


@dp.message_handler(Command("show_on_map_attractions"), state=None)
async def show_on_map(message: types.Message, state: FSMContext):
    await message.answer(
        f"Здравствуйте,{message.from_user.full_name}.\n",
        reply_markup=KeyboardsToSendLocations.SendToBotUserLocation)


@dp.message_handler(text="Отмена")
async def exit_locations(message: types.Message, state: FSMContext):
    await message.answer("Вы отказались\n", reply_markup=ReplyKeyboardRemove())
    await state.finish()


# state=CallBackLocation.Q1,
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def go_to_objet(message: types.Message, state: FSMContext):
    await message.answer(text="Вы отправили локацию", reply_markup=ReplyKeyboardRemove())
    await message.answer("Выберите объект, который вам интересен", reply_markup=SelectTypeAttractions)
    # заносим в машину координаты пользователя, которые он отправил
    await state.update_data(locations_from_user=(message.location.latitude, message.location.longitude))


'''
ФИЛЬТРЫ ДЛЯ КАЖДЫЙ КНОПКИ КОЛЛБЕКА
'''


@dp.callback_query_handler(TypeObject.filter(type_place="Church"))
async def exit_locations(call: CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    await call.answer(cache_time=1)
    # заносим в Машину состояний имя того объекта, на который он нажал
    await state.update_data(lastLocations=callback_data.get('name_place'))
    # получаем нужную информацию об объекте(имя,ссылка,координаты)
    closes_places = choose_nearest(data.get("locations_from_user")[0], data.get("locations_from_user")[-1],
                                   Attractions, callback_data.get('name_place'))
    if not closes_places:
        await RemoveButtonsInInlineKeyboard(closes_places, call, callback_data,
                                            callback_data.get('number_to_remove'))
        return
    await SendToUserLocationUpdateDataBase(closes_places, call)


@dp.callback_query_handler(TypeObject.filter(type_place="ApartmentBuilding"))
async def exit_locations(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=1)
    data = await state.get_data()
    await state.update_data(lastLocations=callback_data.get('name_place'))
    closes_places = choose_nearest(data.get("locations_from_user")[0], data.get("locations_from_user")[-1],
                                   Attractions, callback_data.get('name_place'))
    if not closes_places:
        await RemoveButtonsInInlineKeyboard(closes_places, call, callback_data,
                                            callback_data.get('number_to_remove'))
        return
    await SendToUserLocationUpdateDataBase(closes_places, call)


@dp.callback_query_handler(TypeObject.filter(type_place="Museum"))
async def exit_locations(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=1)
    data = await state.get_data()
    await state.update_data(lastLocations=callback_data.get('name_place'))
    # await call.message.answer(text=f"{callback_data.get('type_place')} {callback_data.get('name_place')}")
    # await call.message.answer(
    #     text=str(data.get("locations_from_user")[0]) + " " + str(data.get("locations_from_user")[-1]))
    closes_places = choose_nearest(data.get("locations_from_user")[0], data.get("locations_from_user")[-1],
                                   Attractions, callback_data.get('name_place'))
    if not closes_places:
        await RemoveButtonsInInlineKeyboard(closes_places, call, callback_data,
                                            callback_data.get('number_to_remove'))
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


@dp.callback_query_handler(TypeObject.filter(type_place="Palace"))
async def exit_locations(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=1)
    data = await state.get_data()
    await state.update_data(lastLocations=callback_data.get('name_place'))
    closes_places = choose_nearest(data.get("locations_from_user")[0], data.get("locations_from_user")[-1],
                                   Attractions, callback_data.get('name_place'))
    if not closes_places:
        await RemoveButtonsInInlineKeyboard(closes_places, call, callback_data,
                                            callback_data.get('number_to_remove'))
        return
    await SendToUserLocationUpdateDataBase(closes_places, call)


@dp.callback_query_handler(TypeObject.filter(type_place="Monument"))
async def exit_locations(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=1)
    data = await state.get_data()
    await state.update_data(lastLocations=callback_data.get('name_place'))
    # await call.message.answer(text=f"{callback_data.get('type_place')} {callback_data.get('name_place')}")
    # await call.message.answer(
    #     text=str(data.get("locations_from_user")[0]) + " " + str(data.get("locations_from_user")[-1]))
    closes_places = choose_nearest(data.get("locations_from_user")[0], data.get("locations_from_user")[-1],
                                   Attractions, callback_data.get('name_place'))
    if not closes_places:
        await RemoveButtonsInInlineKeyboard(closes_places, call, callback_data,
                                            callback_data.get('number_to_remove'))
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


@dp.callback_query_handler(TypeObject.filter(type_place="Park"))
async def exit_locations(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=1)
    data = await state.get_data()
    await state.update_data(lastLocations=callback_data.get('name_place'))
    # await call.message.answer(text=f"{callback_data.get('type_place')} {callback_data.get('name_place')}")
    # await call.message.answer(
    #     text=str(data.get("locations_from_user")[0]) + " " + str(data.get("locations_from_user")[-1]))
    closes_places = choose_nearest(data.get("locations_from_user")[0], data.get("locations_from_user")[-1],
                                   Attractions, callback_data.get('name_place'))
    if not closes_places:
        await RemoveButtonsInInlineKeyboard(closes_places, call, callback_data,
                                            callback_data.get('number_to_remove'))
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


@dp.callback_query_handler(TypeObject.filter(type_place="AnyOne"))
async def exit_locations(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=1)
    data = await state.get_data()
    await state.update_data(lastLocations=callback_data.get('name_place'))
    closes_places = choose_nearest(data.get("locations_from_user")[0], data.get("locations_from_user")[-1],
                                   Attractions, callback_data.get('name_place'))
    if not closes_places:
        await RemoveButtonsInInlineKeyboard(closes_places, call, callback_data,
                                            callback_data.get('number_to_remove'))
        return
    await SendToUserLocationUpdateDataBase(closes_places, call)


'''
ФИЛЬТР ОТМЕНЫ ВЫБОРА ТИПО ДОСТОПРИМЕЧАТЕЛЬНОСТИ В КОЛЛБЕК КЛАВИАТУРЕ
'''


@dp.callback_query_handler(text="cancel_choice_attractions")
async def cancel_choice_attractions(call: CallbackQuery):
    await call.message.edit_text("Вы отказались.")
    await call.message.edit_reply_markup()


'''
ФИЛЬТР ДЛЯ ОТМЕНЫ ПРОХОЖДЕНИЯ СЛЕДУЮЩЕЙ ЛОКАЦИИ
'''


@dp.callback_query_handler(NextOrFinishProgressMap.filter(next="True"))
async def next_place(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=1)
    data = await state.get_data()
    user = db.select_user(id=call.from_user.id)
    # получаем координаты из БД
    new_lat, new_lon = await db.get_coordinates(id=call.from_user.id)
    closes_places = choose_nearest(new_lat, new_lon, Attractions, name_object=data.get('lastLocations'))
    if not closes_places:
        await call.message.edit_text(text='Список мест для посещения закончилось!\n')
        await call.message.edit_reply_markup()
        await call.message.answer(text="Чтобы сбросить карту нажмите /")
        return

    await SendToUserLocationUpdateDataBase(closes_places, call)


@dp.callback_query_handler(NextOrFinishProgressMap.filter(next="False"))
async def Finish_InlineLocations(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_text(text="Спасибо")
