from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery


from encyclopedia_all_files.Encyclopedia_District.Soviet_region.photos import Sovet_photo1
from encyclopedia_all_files.Encyclopedia_District.Soviet_region.text import Sovet_text
from handlers.users.encyclopedia import a
from keyboards.inline.callback_datas import place_callback
from keyboards.inline.encyclopedia import place_keyboard
from loader import dp


@dp.callback_query_handler(place_callback.filter(item_name="sov_r"))
async def sov_region(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Советский район\n", reply_markup=place_keyboard)


@dp.callback_query_handler(place_callback.filter(item_name="1"))
async def sov_1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer_photo(photo=Sovet_photo1[len(a)])
    await call.message.answer(text=Sovet_text[len(a)])


@dp.callback_query_handler(place_callback.filter(item_name="2"))
async def sov_2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    await call.message.answer("район\n")


@dp.callback_query_handler(place_callback.filter(item_name="show_more"))
async def show_more(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    if len(a) < len(Sovet_photo1):
        a.append(0)
        await call.message.answer("More...", reply_markup=place_keyboard)
    else:
        await call.message.answer("no more")
