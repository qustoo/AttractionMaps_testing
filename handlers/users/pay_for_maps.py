from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink, hcode

from data.Maps import Maps
from data.config import WALLET_QIWI
from keyboards.inline.purchase_maps import buy_keyboard, paid_keyboard
from loader import dp
from utils.misc.qiwi import PaymentForQiwi, NoPaymentFound, NotEnoughMoney


@dp.message_handler(Command("buy_map"))
async def show_maps(message: types.Message):
    caption = """
    Название: {title}
    <i>Описание</i>
    {description}
    
    <b>Цена </b> {price:.1f} <b>RUB</b>
    """
    for map in Maps:
        await message.answer_photo(
            photo=map.photo_link,
            caption=caption.format(
                title=map.title,
                description=map.description,
                price=map.price
            ),
            reply_markup=buy_keyboard(item_id=map.id)
        )


@dp.callback_query_handler(text_contains="buy")
async def create_invoice(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    item_id = int(call.data.split(":")[-1]) - 1
    item = Maps[0]
    amount = item.price

    payment = PaymentForQiwi(amount=amount)
    payment.create()

    await call.message.answer(
        "\n".join(
            [
                f"Оплатите не менее {amount:.1f} по номеру телефона или по адресу",
                hlink(WALLET_QIWI, url=payment.invoice),
                "Обязательно укажите ID платежа",
                hcode(payment.id)
            ]
        ),
        reply_markup=paid_keyboard
    )
    await state.set_state("qiwi")
    await state.update_data(payment=payment)


@dp.callback_query_handler(text="cancel", state="qiwi")
async def cancel_payment(call: CallbackQuery, state: FSMContext):
    await call.answer("Отменено",show_alert=True)
    await state.finish()


@dp.callback_query_handler(text="paid", state="qiwi")
async def cancel_payment(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: PaymentForQiwi = data.get("payment")
    try:
        payment.check_payment()
    except NoPaymentFound:
        await call.message.answer("Не найден платеж!")
        return
    except NotEnoughMoney:
        await call.message.answer("Не хватает средств!")
        return
    else:
        await call.message.answer("Все успешно оплачено!")
    await call.message.delete_reply_markup()
    await state.finish()
