from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types
from states import Test
from aiogram.dispatcher.filters import Command


@dp.register_message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали Викторину.\n"
                         "Вопрос №1 \n\n"
                         "(1869,1868)")


await Test.Q1.set()


# await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)
    '''
    await state.update_data()
    {
        "answer1": answer
    }
    '''

    # async with state.proxy() as data:
    #   data["answer1"]=answer

    await  message.answer("Вопрос №2\n\n"
                          "(1903,1904)")
    await Test.next()
    # await Test.Q2.set()


    @dp.message_handler(state = Test.Q2)
    async def answer_q2(message: types.Message, state: FSMContext):
        data = await state.get_data()
        answer1 = data.get("answer1")
        answer2 = message.text

        await message.answer("Спасибо за ответы")
        await message.answer(f"Ответ 1: {answer1}")
        await message.answer(f"Ответ 2: {answer2}")

        # Сбросим машину состояний
        await state.finish()

        # Сброс с сохранением данных в q2
        await state.reset_state(with_data=False)




