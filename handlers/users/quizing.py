from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Quiz


@dp.message_handler(Command("quiz"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали Викторину.\n"
                         "Вопрос №1\n"
                         "Откуда вы приеахли?\n"
                         )
    await Quiz.Q1.set()


# или await.Quiz.first()


@dp.message_handler(state=Quiz.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer1": answer}
    )

    await message.answer("Вопрос№2"
                         "В какой части города вы сейчас находитесь?\n"
                         )

    await Quiz.Q2.set()


@dp.message_handler(state=Quiz.Q2)
async def answer_q1(message: types.Message,state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спасибо за ответы")
    await message.answer(f"Ответ1 :{answer1}")
    await message.answer(F"Ответ2: {answer2}")

    await state.reset_state(with_data=False)