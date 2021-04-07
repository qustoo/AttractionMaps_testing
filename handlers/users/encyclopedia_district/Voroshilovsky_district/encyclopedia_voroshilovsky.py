from aiogram.types import CallbackQuery

from encyclopedia_all_files.Encyclopedia_District.Voroshilovsky_region.photos import Voroshil_photo1, Voroshil_photo5, \
    Voroshil_photo4, Voroshil_photo3, Voroshil_photo2
from encyclopedia_all_files.Encyclopedia_District.Voroshilovsky_region.text import Voroshil_text1, Voroshil_text2, \
    Voroshil_text3, Voroshil_text4, Voroshil_text5
from handlers.users.encyclopedia import g
from keyboards.inline.callback_datas import place_callback
from keyboards.inline.encyclopedia import vor_keyboard
from loader import dp, photo_db


@dp.callback_query_handler(place_callback.filter(item_name="vor_r"))
async def vor_region(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Ворошиловский район\n", reply_markup=vor_keyboard)


@dp.callback_query_handler(place_callback.filter(item_name="1vor"))
async def vor_1(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(g) < len(Voroshil_photo1):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Voroshil_photo1[len(g)]), 'rb'))
        await call.message.answer(text=Voroshil_text1[len(g)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="2vor"))
async def vor_2(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(g) < len(Voroshil_photo2):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Voroshil_photo2[len(g)]), 'rb'))
        await call.message.answer(text=Voroshil_text2[len(g)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="3vor"))
async def vor_3(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(g) < len(Voroshil_photo3):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Voroshil_photo3[len(g)]), 'rb'))
        await call.message.answer(text=Voroshil_text3[len(g)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="4vor"))
async def vor_4(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(g) < len(Voroshil_photo4):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Voroshil_photo4[len(g)]), 'rb'))
        await call.message.answer(text=Voroshil_text4[len(g)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="5vor"))
async def vor_5(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    if len(g) < len(Voroshil_photo5):
        await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=Voroshil_photo5[len(g)]), 'rb'))
        await call.message.answer(text=Voroshil_text5[len(g)])
    else:
        await call.message.answer("больше нет😔")


@dp.callback_query_handler(place_callback.filter(item_name="show_more_vor"))
async def show_more_len(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    if len(g) < len(Voroshil_photo1) - 1:
        g.append(0)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Продолжение...", reply_markup=vor_keyboard)
    else:
        await call.message.answer("больше нет😔")
