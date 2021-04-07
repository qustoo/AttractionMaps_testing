from aiogram.types import CallbackQuery

from encyclopedia_all_files.Encyclopedia_District.Proletarian_region.photos import Proletarian_photo1, Proletarian_photo5, \
    Proletarian_photo4, Proletarian_photo3, Proletarian_photo2
from encyclopedia_all_files.Encyclopedia_District.Proletarian_region.text import Proletarian_text1, Proletarian_text2, \
    Proletarian_text3, Proletarian_text4, Proletarian_text5
from handlers.users.encyclopedia import c
from keyboards.inline.callback_datas import place_callback
from keyboards.inline.encyclopedia import prolet_keyboard
from loader import dp, photo_db


@dp.callback_query_handler(place_callback.filter(item_name="prol_r"))
async def oct_region(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Пролетарский район\n", reply_markup=prolet_keyboard)


@dp.callback_query_handler(place_callback.filter(item_name="1pr"))
async def oct_1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(c) < len(Proletarian_photo1):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Proletarian_photo1[len(c)]), 'rb'))
        await call.message.answer(text=Proletarian_text1[len(c)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="2pr"))
async def oct_2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(c) < len(Proletarian_photo2):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Proletarian_photo2[len(c)]), 'rb'))
        await call.message.answer(text=Proletarian_text2[len(c)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="3pr"))
async def oct_3(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(c) < len(Proletarian_photo3):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Proletarian_photo3[len(c)]), 'rb'))
        await call.message.answer(text=Proletarian_text3[len(c)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="4pr"))
async def oct_4(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(c) < len(Proletarian_photo4):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Proletarian_photo4[len(c)]), 'rb'))
        await call.message.answer(text=Proletarian_text4[len(c)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="5pr"))
async def oct_5(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(c) < len(Proletarian_photo5):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Proletarian_photo5[len(c)]), 'rb'))
        await call.message.answer(text=Proletarian_text5[len(c)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="show_more_pr"))
async def show_more(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    if len(c) < len(Proletarian_photo1) - 1:
        c.append(0)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Продолжение...", reply_markup=prolet_keyboard)
    else:
        await call.message.answer("больше нет😔")