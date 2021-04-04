from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard_terrain, pear_keyboard_route
from loader import dp


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
