from aiogram import types

from aiogram.contrib.middlewares import logging
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice,pear_keyboard_terrain
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(text="Мы можем предложить карту местности,и карту маршрутов.\n"
                              "Если же вам ничего не нужно жмите - Отмена"
                         , reply_markup=choice
                         )


@dp.callback_query_handler(buy_callback.filter(item_name="terrain_map"))
async def buying_terrain_map(call: CallbackQuery):
    await call.answer(cache_time=60)
    #logging.info(f"callback_data := {call.data}")
    await call.message.answer(f"Вы выбрали купить карту местности!\n",reply_markup=pear_keyboard_terrain)


@dp.callback_query_handler(buy_callback.filter(item_name="route_map"))
async def buying_terrain_map(call: CallbackQuery):
    await call.answer(cache_time=60)
    #logging.info(f"callback_data := {call.data}")
    await call.message.answer(f"Вы выбрали купить карту маршрутов!\n",reply_markup=pear_keyboard_terrain)
