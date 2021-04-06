from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.encyclopedia import choice_p
from loader import dp

a = []


@dp.message_handler(Command("reset_encyclopedia"))
async def show_encyclopedia(message: types.Message):
    a.clear()
    await message.answer("Энциклопедия обновлена\n")


@dp.message_handler(Command("encyclopedia"))
async def show_encyclopedia(message: types.Message):
    await message.answer(text=
                         f"Выберите район\n"
                         "Если передумали - нажмите отмена",
                         # choice - клавиатура
                         reply_markup=choice_p
                         )
