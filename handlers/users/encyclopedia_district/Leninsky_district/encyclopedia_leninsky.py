from aiogram.types import CallbackQuery

from encyclopedia_all_files.Encyclopedia_District.Leninsky_region.photos import Lininsky_photo1, Lininsky_photo5, \
    Lininsky_photo4, Lininsky_photo3, Lininsky_photo2
from encyclopedia_all_files.Encyclopedia_District.Leninsky_region.text import Leninsky_text1, Leninsky_text2, \
    Leninsky_text3, Leninsky_text4, Leninsky_text5
from handlers.users.encyclopedia import e
from keyboards.inline.callback_datas import place_callback
from keyboards.inline.encyclopedia import len_keyboard
from loader import dp, photo_db


@dp.callback_query_handler(place_callback.filter(item_name="len_r"))
async def len_region(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Ленинский район\n", reply_markup=len_keyboard)


@dp.callback_query_handler(place_callback.filter(item_name="1len"))
async def len_1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(e) < len(Lininsky_photo1):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Lininsky_photo1[len(e)]), 'rb'))
        await call.message.answer(text=Leninsky_text1[len(e)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="2len"))
async def len_2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(e) < len(Lininsky_photo2):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Lininsky_photo2[len(e)]), 'rb'))
        await call.message.answer(text=Leninsky_text2[len(e)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="3len"))
async def len_3(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(e) < len(Lininsky_photo3):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Lininsky_photo3[len(e)]), 'rb'))
        await call.message.answer(text=Leninsky_text3[len(e)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="4len"))
async def len_4(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(e) < len(Lininsky_photo4):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Lininsky_photo4[len(e)]), 'rb'))
        await call.message.answer(text=Leninsky_text4[len(e)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="5len"))
async def len_5(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(e) < len(Lininsky_photo5):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Lininsky_photo5[len(e)]), 'rb'))
        await call.message.answer(text=Leninsky_text5[len(e)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="show_more_len"))
async def show_more_len(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    if len(e) < len(Lininsky_photo1) - 1:
        e.append(0)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Продолжение...", reply_markup=len_keyboard)
    else:
        await call.message.answer("больше нет😔")
