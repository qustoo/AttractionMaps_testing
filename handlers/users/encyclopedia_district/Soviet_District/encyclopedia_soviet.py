from aiogram.types import CallbackQuery

from encyclopedia_all_files.Encyclopedia_District.Soviet_region.photos import Sovet_photo1, Sovet_photo2, Sovet_photo3, \
    Sovet_photo4, Sovet_photo5
from encyclopedia_all_files.Encyclopedia_District.Soviet_region.text import Sovet_text_1, Sovet_text_2, Sovet_text_3, \
    Sovet_text_4, Sovet_text_5
from handlers.users.encyclopedia import a
from keyboards.inline.callback_datas import place_callback
from keyboards.inline.encyclopedia import soviet_keyboard
from loader import dp, photo_db


@dp.callback_query_handler(place_callback.filter(item_name="sov_r"))
async def sov_region(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Советский район\n", reply_markup=soviet_keyboard)


@dp.callback_query_handler(place_callback.filter(item_name="1"))
async def sov_1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(a) < len(Sovet_photo1):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Sovet_photo1[len(a)]), 'rb'))
        await call.message.answer(text=Sovet_text_1[len(a)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="2"))
async def sov_2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(a) < len(Sovet_photo2):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Sovet_photo2[len(a)]), 'rb'))
        await call.message.answer(text=Sovet_text_2[len(a)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="3"))
async def sov_3(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(a) < len(Sovet_photo3):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Sovet_photo3[len(a)]), 'rb'))
        await call.message.answer(text=Sovet_text_3[len(a)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="4"))
async def sov_4(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(a) < len(Sovet_photo4):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Sovet_photo4[len(a)]), 'rb'))
        await call.message.answer(text=Sovet_text_4[len(a)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="5"))
async def sov_5(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(a) < len(Sovet_photo5):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Sovet_photo5[len(a)]), 'rb'))
        await call.message.answer(text=Sovet_text_5[len(a)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="show_more"))
async def show_more(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    if len(a) < len(Sovet_photo1) - 1:
        a.append(0)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Продолжение...", reply_markup=soviet_keyboard)
    else:
        await call.message.answer("больше нет😔")

