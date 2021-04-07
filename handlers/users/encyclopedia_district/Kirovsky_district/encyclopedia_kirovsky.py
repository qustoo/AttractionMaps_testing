from aiogram.types import CallbackQuery

from encyclopedia_all_files.Encyclopedia_District.Kirovsky_region.photos import Kirovsky_photo1, Kirovsky_photo5, \
    Kirovsky_photo4, Kirovsky_photo3, Kirovsky_photo2
from encyclopedia_all_files.Encyclopedia_District.Kirovsky_region.text import Kirovsky_text1, Kirovsky_text2, \
    Kirovsky_text3, Kirovsky_text4, Kirovsky_text5
from handlers.users.encyclopedia import d
from keyboards.inline.callback_datas import place_callback
from keyboards.inline.encyclopedia import kirov_keyboard
from loader import dp, photo_db


@dp.callback_query_handler(place_callback.filter(item_name="kir_r"))
async def oct_region(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Кировский район\n", reply_markup=kirov_keyboard)


@dp.callback_query_handler(place_callback.filter(item_name="1kir"))
async def oct_1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(d) < len(Kirovsky_photo1):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Kirovsky_photo1[len(d)]), 'rb'))
        await call.message.answer(text=Kirovsky_text1[len(d)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="2kir"))
async def oct_2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(d) < len(Kirovsky_photo2):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Kirovsky_photo2[len(d)]), 'rb'))
        await call.message.answer(text=Kirovsky_text2[len(d)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="3kir"))
async def oct_3(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(d) < len(Kirovsky_photo3):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Kirovsky_photo3[len(d)]), 'rb'))
        await call.message.answer(text=Kirovsky_text3[len(d)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="4kir"))
async def oct_4(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(d) < len(Kirovsky_photo4):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Kirovsky_photo4[len(d)]), 'rb'))
        await call.message.answer(text=Kirovsky_text4[len(d)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="5kir"))
async def oct_5(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(d) < len(Kirovsky_photo5):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Kirovsky_photo5[len(d)]), 'rb'))
        await call.message.answer(text=Kirovsky_text5[len(d)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="show_more_kir"))
async def show_more(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    if len(d) < len(Kirovsky_photo1) - 1:
        d.append(0)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Продолжение...", reply_markup=kirov_keyboard)
    else:
        await call.message.answer("больше нет😔")
