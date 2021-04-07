from aiogram.types import CallbackQuery

from encyclopedia_all_files.Encyclopedia_District.MayDay_region.photos import MayDay_photo1, MayDay_photo5, \
    MayDay_photo4, MayDay_photo3, MayDay_photo2
from encyclopedia_all_files.Encyclopedia_District.MayDay_region.text import MayDay_text1, MayDay_text2, \
    MayDay_text3, MayDay_text4, MayDay_text5
from handlers.users.encyclopedia import h
from keyboards.inline.callback_datas import place_callback
from keyboards.inline.encyclopedia import per_keyboard
from loader import dp, photo_db


@dp.callback_query_handler(place_callback.filter(item_name="perv_r"))
async def perv_region(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Первомайский район\n", reply_markup=per_keyboard)


@dp.callback_query_handler(place_callback.filter(item_name="1per"))
async def perv_1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(h) < len(MayDay_photo1):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=MayDay_photo1[len(h)]), 'rb'))
        await call.message.answer(text=MayDay_text1[len(h)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="2per"))
async def perv_2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(h) < len(MayDay_photo2):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=MayDay_photo2[len(h)]), 'rb'))
        await call.message.answer(text=MayDay_text2[len(h)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="3per"))
async def perv_3(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(h) < len(MayDay_photo3):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=MayDay_photo3[len(h)]), 'rb'))
        await call.message.answer(text=MayDay_text3[len(h)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="4per"))
async def perv_4(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(h) < len(MayDay_photo4):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=MayDay_photo4[len(h)]), 'rb'))
        await call.message.answer(text=MayDay_text4[len(h)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="5per"))
async def perv_5(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(h) < len(MayDay_photo5):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=MayDay_photo5[len(h)]), 'rb'))
        await call.message.answer(text=MayDay_text5[len(h)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="show_more_per"))
async def show_more_len(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    if len(h) < len(MayDay_photo1) - 1:
        h.append(0)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Продолжение...", reply_markup=per_keyboard)
    else:
        await call.message.answer("больше нет😔")
