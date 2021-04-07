from aiogram.types import CallbackQuery

from encyclopedia_all_files.Encyclopedia_District.October_region.photos import October_photo1, October_photo5, \
    October_photo4, October_photo3, October_photo2
from encyclopedia_all_files.Encyclopedia_District.October_region.text import October_text1, October_text2, \
    October_text3, October_text4, October_text5
from handlers.users.encyclopedia import b
from keyboards.inline.callback_datas import place_callback
from keyboards.inline.encyclopedia import oct_keyboard
from loader import dp, photo_db


@dp.callback_query_handler(place_callback.filter(item_name="oct_r"))
async def oct_region(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Октябрьский район\n", reply_markup=oct_keyboard)


@dp.callback_query_handler(place_callback.filter(item_name="1ok"))
async def oct_1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(b) < len(October_photo1):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=October_photo1[len(b)]), 'rb'))
        await call.message.answer(text=October_text1[len(b)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="2ok"))
async def oct_2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(b) < len(October_photo2):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=October_photo2[len(b)]), 'rb'))
        await call.message.answer(text=October_text2[len(b)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="3ok"))
async def oct_3(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(b) < len(October_photo3):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=October_photo3[len(b)]), 'rb'))
        await call.message.answer(text=October_text3[len(b)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="4ok"))
async def oct_4(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(b) < len(October_photo4):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=October_photo4[len(b)]), 'rb'))
        await call.message.answer(text=October_text4[len(b)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="5ok"))
async def oct_5(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(b) < len(October_photo5):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=October_photo5[len(b)]), 'rb'))
        await call.message.answer(text=October_text5[len(b)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="show_more_ok"))
async def show_more(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    if len(b) < len(October_photo1) - 1:
        b.append(0)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Продолжение...", reply_markup=oct_keyboard)
    else:
        await call.message.answer("больше нет😔")
