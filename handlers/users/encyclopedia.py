from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import pagination_call
from keyboards.inline.encyclopedia import choice_p
from loader import dp, photo_db



@dp.callback_query_handler(text="cancel_place")
async def cancel_encyclopedia(call: CallbackQuery):
    await call.answer(text="Отмена", show_alert=True)

    # Отправляем пустую клавиатуру, т.е. выходит из клавиатуры
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(Command("encyclopedia"))
async def kir_reg(message: types.Message):

    await message.answer(text=
                         f"Выберите район\n"
                         "Если передумали - нажмите отмена",
                         # choice - клавиатура
                         reply_markup=choice_p
                         )

@dp.callback_query_handler(pagination_call.filter(page="current_page"))
async def cur_p(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)


def get_page(array,page:int=1):
    page_index=page-1
    return array[page_index]
