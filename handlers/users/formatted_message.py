from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink

text = "\n".join(
    [
        "Привет" + hbold(" пользователь!"),
        "Здесь мы тестируем форматирование" + " " + hitalic("текста c HTML"),
        "Уверен ты работал с html" + " " + "(" + hstrikethrough("или нет") + ")",
        "Почитать подробнее можно " + hlink("тут", "http://htmlbook.ru/content/formatirovanie-teksta"),
        hcode("While(true)"),
    ]
)


# просто пример обработки текста с html тегами
@dp.message_handler(Command("html_parse_text"))
async def get_answer_html(message: types.Message):
    await message.answer(text, parse_mode="HTML")
