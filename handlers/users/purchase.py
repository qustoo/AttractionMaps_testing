from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from encyclopedia_all_files.Encyclopedia_District.Soviet_region.photos import Sovet_photo1
from encyclopedia_all_files.Encyclopedia_District.Soviet_region.text import Sovet_text
from keyboards.inline.callback_datas import buy_callback, place_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard_terrain, pear_keyboard_route
from keyboards.inline.encyclopedia import choice_p, place_keyboard
from loader import dp, photo_db
a=[]
@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(text=
                         f"Мы можем предложить\n1)Карту местности,\n 2)Карту маршрутов.\n"
                         "Если ничего не интересует - нажмите отмена",
                         # choice - клавиатура
                         reply_markup=choice
                         )
    # await bot.send_photo(chat_id=message.chat_id,photo=)


@dp.callback_query_handler(buy_callback.filter(item_name="terrain_map"))
async def buying_terrain_map(call: CallbackQuery, callback_data: dict):
    # не ловит в 60 сек
    await call.answer(cache_time=60)
    # Логирование
    # logging.info(f"callback_data := {call.data}")
    # ScaleMap = callback_data.get("skale")
    await call.message.answer(f"Вы выбрали купить карту местности!\n".upper(),  # f"Масштаб 1 к {ScaleMap}",
                              reply_markup=pear_keyboard_terrain)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(buy_callback.filter(item_name="route_map"))
async def buying_route_map(call: CallbackQuery, callback_data: dict):
    # не ловит в 60 сек
    await call.answer(cache_time=60)
    # Логирование
    # logging.info(f"callback_data := {call.data}")
    # отвечает на сообщение вызова пользователю
    # mapskale = callback_data.get("scale")
    await call.message.answer(f"Вы выбрали купить карту маршрутов!\n".upper(),
                              # f"Масштаб 1 к {mapskale}",
                              reply_markup=pear_keyboard_route)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(text="cancel")
async def cancel_buying_maps(call: CallbackQuery):
    await call.answer(text="Отмена покупки карт!", show_alert=True)

    # Отправляем пустую клавиатуру, т.е. выходит из клавиатуры
    await call.message.edit_reply_markup(reply_markup=None)




@dp.message_handler(Command("reset_encyclopedia"))
async def show_encyclopedia(message: types.Message):
    a.clear()
    await message.answer("Энциклопедия обновлена\n")

@dp.message_handler(Command("encyclopedia"))
async def show_encyclopedia(message: types.Message):
    await message.answer(text=
                         f"Выберите район\n"
                         "Если передумали - нажмите отмена",
                         # choice - клавиатура
                         reply_markup=choice_p
                         )

@dp.callback_query_handler(text="cancel_place")
async def cancel_encyclopedia(call: CallbackQuery):
    await call.answer(text="Отмена", show_alert=True)

    # Отправляем пустую клавиатуру, т.е. выходит из клавиатуры
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(place_callback.filter(item_name="sov_r"))
async def sov_region(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Советский район\n", reply_markup=place_keyboard)


@dp.callback_query_handler(place_callback.filter(item_name="1"))
async def sov_1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(Sovet_photo1[len(a)])
    await call.message.answer(text=Sovet_text[len(a)])


@dp.callback_query_handler(place_callback.filter(item_name="2"))
async def sov_2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    await call.message.answer("район\n")

@dp.callback_query_handler(place_callback.filter(item_name="show_more"))
async def show_more(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    global a
    if len(a)<len(Sovet_photo1):
        a.append(0)
        await call.message.answer("More...", reply_markup=place_keyboard)
    else:
        await call.message.answer("no more")

