from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.locations_for_button import save_location
from loader import dp, db


@dp.message_handler(Command("save_my_location"))
async def save_first_time_location(message: types.Message, state: FSMContext):
    await message.answer("Нам требуется сохранить вашу локацию, нажмите на кнопку ниже", reply_markup=save_location)
    await state.set_state("save_rate")


@dp.message_handler(content_types=types.ContentType.LOCATION, state="save_rate")
async def get_location(message: types.Message):
    location = message.location
    db.update_lon(id=message.from_user.id, lon=location.longitude)
    db.update_lat(id=message.from_user.id, lat=location.latitude)
    await message.answer("Cпасибо за отправку", reply_markup=ReplyKeyboardRemove())
