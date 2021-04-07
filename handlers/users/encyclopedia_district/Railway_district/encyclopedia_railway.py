from aiogram.types import CallbackQuery

from encyclopedia_all_files.Encyclopedia_District.Railway_region.photos import Railway_photo1, Railway_photo5, \
    Railway_photo4, Railway_photo3, Railway_photo2
from encyclopedia_all_files.Encyclopedia_District.Railway_region.text import Railway_text1, Railway_text2, \
    Railway_text3, Railway_text4, Railway_text5
from handlers.users.encyclopedia import f
from keyboards.inline.callback_datas import place_callback
from keyboards.inline.encyclopedia import rai_keyboard
from loader import dp, photo_db


@dp.callback_query_handler(place_callback.filter(item_name="rai_r"))
async def rai_region(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Железнодорожный район\n", reply_markup=rai_keyboard)


@dp.callback_query_handler(place_callback.filter(item_name="1rai"))
async def rai_1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(f) < len(Railway_photo1):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Railway_photo1[len(f)]), 'rb'))
        await call.message.answer(text=Railway_text1[len(f)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="2rai"))
async def rai_2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(f) < len(Railway_photo2):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Railway_photo2[len(f)]), 'rb'))
        await call.message.answer(text=Railway_text2[len(f)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="3rai"))
async def rai_3(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(f) < len(Railway_photo3):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Railway_photo3[len(f)]), 'rb'))
        await call.message.answer(text=Railway_text3[len(f)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="4rai"))
async def rai_4(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(f) < len(Railway_photo4):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Railway_photo4[len(f)]), 'rb'))
        await call.message.answer(text=Railway_text4[len(f)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="5rai"))
async def rai_5(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(f) < len(Railway_photo5):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Railway_photo5[len(f)]), 'rb'))
        await call.message.answer(text=Railway_text5[len(f)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="show_more_rai"))
async def show_more_len(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    if len(f) < len(Railway_photo1) - 1:
        f.append(0)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Продолжение...", reply_markup=rai_keyboard)
    else:
        await call.message.answer("больше нет😔")
