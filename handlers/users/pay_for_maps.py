from random import randint

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.markdown import hlink, hcode

from data.Maps import Maps
from data.config import WALLET_QIWI
from keyboards.default.BuyMapSelectKeyboard import SelectDistrictSovietKirosvky
from keyboards.inline.purchase_maps import buy_keyboard, paid_keyboard
from loader import dp
from utils.misc.qiwi import PaymentForQiwi, NoPaymentFound, NotEnoughMoney


class ChoiceAMapDistrict(StatesGroup):
    Q1 = State()


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
    await call.answer("Отменено", show_alert=True)
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
        await call.message.answer("Все успешно оплачено!\nВыберите район:", reply_markup=SelectDistrictSovietKirosvky)
        await ChoiceAMapDistrict.Q1.set()

        # rand_item = randint(1, 2)
        # if rand_item == 1:
        #     await call.message.answer_document(types.InputFile("data/Rostov-na-donu.png"),
        #                                        caption="Вот ваша секретная покупка!")
        # else:
        #     await call.message.answer_document(types.InputFile("data/Rostov-na-donu_1.png"),
        #                                        caption="Вот ваша секретная покупка!")
        # await state.set_state("choose a product")
        await call.message.delete_reply_markup()


@dp.message_handler(text="Советский", state=ChoiceAMapDistrict.Q1)
async def exit_locations(message: types.Message, state: FSMContext):
    await message.answer("Cпасибо за покупку", reply_markup=ReplyKeyboardRemove())
    await message.answer_document(types.InputFile("data/Rostov-na-donu_1.png"),
                                  caption="Вот ваша секретная покупка!")
    await state.finish()


@dp.message_handler(text="Кировский", state=ChoiceAMapDistrict.Q1)
async def exit_locations(message: types.Message, state: FSMContext):
    await message.answer("Cпасибо за покупку", reply_markup=ReplyKeyboardRemove())
    await message.answer_document(types.InputFile("data/Rostov-na-donu.png"),
                                  caption="Вот ваша секретная покупка!")
    await state.finish()

# await call.message.delete_reply_markup()
# await state.finish()
