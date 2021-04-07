from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.encyclopedia import choice_p
from loader import dp

# чтобы можно было смотреть другие районы, не обновляя энциклопедию
a, b, c, d, e, f, g, h = [], [], [], [], [], [], [], []


@dp.message_handler(Command("reset_encyclopedia"))
async def show_encyclopedia(message: types.Message):
    a.clear()
    b.clear()
    c.clear()
    d.clear()
    e.clear()
    f.clear()
    g.clear()
    h.clear()
    await message.answer("Энциклопедия обновлена\n")


@dp.message_handler(Command("encyclopedia"))
async def show_encyclopedia(message: types.Message):
    await message.answer(text=
                         f"Выберите район\n"
                         "Если передумали - нажмите отмена",
                         # choice - клавиатура
                         reply_markup=choice_p
                         )


@dp.callback_query_handler(text="cancel_place")
async def cancel_encyclopedia(call: CallbackQuery):
    await call.answer(text="Отмена", show_alert=True)

    # Отправляем пустую клавиатуру, т.е. выходит из клавиатуры
    await call.message.edit_reply_markup(reply_markup=None)
