from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Quiz


# пустое состояние
@dp.message_handler(Command("quiz"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вы начали Викторину.\n"
                         "Вопрос №1\n"
                         "Откуда вы приеахли?\n"
                         )
    # Устанавливаем состояние чтобы бот понял ответ на 1 вопрос
    await Quiz.Q1.set()

    # или такой способ:
    # или await.Quiz.first()


# Ловим переход в след вопрос
@dp.message_handler(state=Quiz.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer1 = message.text
    # сохраняем результат
    await state.update_data(
        {
            "answer_first": answer1
        }
    )
    # или так
    # await state.update_data(answer1=answer)

    await message.answer("Вопрос№2"
                         "В какой части города вы сейчас находитесь?\n"
                         )

    # Устанавливаем состояние во второй вопрос
    await Quiz.Q2.set()


# Ловим третье состояние
@dp.message_handler(state=Quiz.Q2)
async def answer_q2(message: types.message, state: FSMContext):
    # получает ответ на q2
    answer2 = message.text
    await state.update_data(
        {
            "answer_second": answer2
        }
    )
    await message.answer("Вопрос№3"
                         "Сколько вам лет?\n"
                         )
    # Устанавливаем состояние во третий вопрос
    await Quiz.Q3.set()


# Ловим последний переход
@dp.message_handler(state=Quiz.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    # получаем все данные
    data = await state.get_data()
    # получаем данные по первому вопросу
    answer1 = data.get("answer_first")
    # получаем данные по второму вопрсоу
    answer2 = data.get("answer_second")
    # текущий текст ответа(он же и ответ на второй вопрос), т.е. получаем ответ на q3
    answer3 = message.text

    await message.answer("Спасибо за ответы")
    await message.answer(f"Ответ 1: {answer1}")
    await message.answer(F"Ответ 2: {answer2}")
    await message.answer(F"Ответ 3: {answer3}")

    # сбрасываем состояние
    await state.finish()

    # сбрасываем состояние с сохранением данных
    # await state.reset_state(with_data=False)
