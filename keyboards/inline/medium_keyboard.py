from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import quiz_callback, quiz_photo_callback

medium_keyboard1 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="Одну",
                callback_data=quiz_callback.new(next="2m",answer="Одну")),
],[InlineKeyboardButton(
                text="Две",
                callback_data=quiz_callback.new(next="2m",answer="2")),
],
[InlineKeyboardButton(
                text="Три",
                callback_data=quiz_callback.new(next="2m",answer="3")),
],[InlineKeyboardButton(
                text="Четыре",
                callback_data=quiz_callback.new(next="2m",answer="4")),
],[InlineKeyboardButton(
                text="Пять",
                callback_data=quiz_callback.new(next="2m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard2 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="Дмитрий Донской",
                callback_data=quiz_callback.new(next="3m",answer="1")),
],[InlineKeyboardButton(
                text="Елизавета Петровна",
                callback_data=quiz_callback.new(next="3m",answer="2")),
],
[InlineKeyboardButton(
                text="Иван Грозный",
                callback_data=quiz_callback.new(next="3m",answer="3")),
],[InlineKeyboardButton(
                text="Перт Алексеевич",
                callback_data=quiz_callback.new(next="3m",answer="Петр")),
],[InlineKeyboardButton(
                text="Николай Павлович",
                callback_data=quiz_callback.new(next="3m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard3 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="Ростовский областной музей краеведения",
                callback_data=quiz_callback.new(next="4m",answer="1")),
],[InlineKeyboardButton(
                text="Ростовский областной суд",
                callback_data=quiz_callback.new(next="4m",answer="2")),
],
[InlineKeyboardButton(
                text="Художественная Галерея 'Ростов'",
                callback_data=quiz_callback.new(next="4m",answer="3")),
],[InlineKeyboardButton(
                text="Пятнадцатый арбитражный апелляционный суд",
                callback_data=quiz_callback.new(next="4m",answer="Суд")),
],[InlineKeyboardButton(
                text="Музейная экспозиция в Управлении ФССП России по РО",
                callback_data=quiz_callback.new(next="4m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard4 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="Тихий Дон",
                callback_data=quiz_callback.new(next="5m",answer="1")),
],[InlineKeyboardButton(
                text="Горе от ума",
                callback_data=quiz_callback.new(next="5m",answer="2")),
],
[InlineKeyboardButton(
                text="12 стульев",
                callback_data=quiz_callback.new(next="5m",answer="Стулья")),
],[InlineKeyboardButton(
                text="Война и мир",
                callback_data=quiz_callback.new(next="5m",answer="4")),
],[InlineKeyboardButton(
                text="Отцы и дети",
                callback_data=quiz_callback.new(next="5m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard5 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="Комитет министров",
                callback_data=quiz_callback.new(next="6m",answer="1")),
],[InlineKeyboardButton(
                text="Верховный суд",
                callback_data=quiz_callback.new(next="6m",answer="2")),
],
[InlineKeyboardButton(
                text="Совет Федераций",
                callback_data=quiz_callback.new(next="6m",answer="3")),
],[InlineKeyboardButton(
                text="Сенат",
                callback_data=quiz_callback.new(next="6m",answer="4")),
],[InlineKeyboardButton(
                text="Городская дума",
                callback_data=quiz_callback.new(next="6m",answer="Дума")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard6 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="1952",
                callback_data=quiz_callback.new(next="7m",answer="1")),
],[InlineKeyboardButton(
                text="1941",
                callback_data=quiz_callback.new(next="7m",answer="1941")),
],
[InlineKeyboardButton(
                text="1869",
                callback_data=quiz_callback.new(next="7m",answer="3")),
],[InlineKeyboardButton(
                text="1955",
                callback_data=quiz_callback.new(next="7m",answer="4")),
],[InlineKeyboardButton(
                text="1980",
                callback_data=quiz_callback.new(next="7m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard7 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="Деникин",
                callback_data=quiz_callback.new(next="8m",answer="1")),
],[InlineKeyboardButton(
                text="Дроздовский",
                callback_data=quiz_callback.new(next="8m",answer="2")),
],
[InlineKeyboardButton(
                text="Врангель",
                callback_data=quiz_callback.new(next="8m",answer="Врангель")),
],[InlineKeyboardButton(
                text="Краснов",
                callback_data=quiz_callback.new(next="8m",answer="4")),
],[InlineKeyboardButton(
                text="Юденич",
                callback_data=quiz_callback.new(next="8m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard8 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="Абрахам Маслоу",
                callback_data=quiz_callback.new(next="9m",answer="1")),
],[InlineKeyboardButton(
                text="Дейл Карнеги ",
                callback_data=quiz_callback.new(next="9m",answer="2")),
],
[InlineKeyboardButton(
                text="Эрик Берн",
                callback_data=quiz_callback.new(next="9m",answer="3")),
],[InlineKeyboardButton(
                text="Дэвид Карнеги",
                callback_data=quiz_callback.new(next="9m",answer="4")),
],[InlineKeyboardButton(
                text="Карл Густав Юнг",
                callback_data=quiz_callback.new(next="9m",answer="Юнг")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard9 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="Темерницкий мост",
                callback_data=quiz_callback.new(next="10m",answer="1")),
],[InlineKeyboardButton(
                text="Каратаевский мост",
                callback_data=quiz_callback.new(next="10m",answer="2")),
],
[InlineKeyboardButton(
                text="Американский Мост",
                callback_data=quiz_callback.new(next="10m",answer="Мост")),
],[InlineKeyboardButton(
                text="Новый мост",
                callback_data=quiz_callback.new(next="10m",answer="4")),
],[InlineKeyboardButton(
                text="Депутатский мост",
                callback_data=quiz_callback.new(next="10m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard10 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="1911",
                callback_data=quiz_callback.new(next="11m",answer="1911")),
],[InlineKeyboardButton(
                text="1860",
                callback_data=quiz_callback.new(next="11m",answer="2")),
],
[InlineKeyboardButton(
                text="1952",
                callback_data=quiz_callback.new(next="11m",answer="3")),
],[InlineKeyboardButton(
                text="1900",
                callback_data=quiz_callback.new(next="11m",answer="4")),
],[InlineKeyboardButton(
                text="1789",
                callback_data=quiz_callback.new(next="11m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard11 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="Ампир",
                callback_data=quiz_callback.new(next="12m",answer="1")),
],[InlineKeyboardButton(
                text="Классицизм",
                callback_data=quiz_callback.new(next="12m",answer="2")),
],
[InlineKeyboardButton(
                text="Барокко",
                callback_data=quiz_callback.new(next="12m",answer="3")),
],[InlineKeyboardButton(
                text="Необарокко",
                callback_data=quiz_callback.new(next="12m",answer="Необарокко")),
],[InlineKeyboardButton(
                text="Рококо",
                callback_data=quiz_callback.new(next="12m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard12 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="1900",
                callback_data=quiz_callback.new(next="13m",answer="1")),
],[InlineKeyboardButton(
                text="1911",
                callback_data=quiz_callback.new(next="13m",answer="2")),
],
[InlineKeyboardButton(
                text="1899",
                callback_data=quiz_callback.new(next="13m",answer="3")),
],[InlineKeyboardButton(
                text="1901",
                callback_data=quiz_callback.new(next="13m",answer="1901")),
],[InlineKeyboardButton(
                text="1910",
                callback_data=quiz_callback.new(next="13m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)
medium_keyboard13 = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(
                text="1920",
                callback_data=quiz_callback.new(next="14m",answer="1")),
],[InlineKeyboardButton(
                text="1914",
                callback_data=quiz_callback.new(next="14m",answer="1914")),
],
[InlineKeyboardButton(
                text="1941",
                callback_data=quiz_callback.new(next="14m",answer="3")),
],[InlineKeyboardButton(
                text="1910",
                callback_data=quiz_callback.new(next="14m",answer="4")),
],[InlineKeyboardButton(
                text="1917",
                callback_data=quiz_callback.new(next="14m",answer="5")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0m", answer="End"))
        ]]
)

CorrectAnswersMediumQuiz=["Одну","Петр","Суд","Стулья","Дума","1941","Врангель","Юнг","Мост","1911","Необарокко","1901","1914"]




med_photo_keyboard1= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 2 вопроса",callback_data=quiz_photo_callback.new(next="m1"))]])
med_photo_keyboard2= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 3 вопроса",callback_data=quiz_photo_callback.new(next="m2"))]])
med_photo_keyboard3= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 4 вопроса",callback_data=quiz_photo_callback.new(next="m3"))]])
med_photo_keyboard4= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 5 вопроса",callback_data=quiz_photo_callback.new(next="m4"))]])
med_photo_keyboard5= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 6 вопроса",callback_data=quiz_photo_callback.new(next="m5"))]])
med_photo_keyboard6= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 7 вопроса",callback_data=quiz_photo_callback.new(next="m6"))]])
med_photo_keyboard7= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 8 вопроса",callback_data=quiz_photo_callback.new(next="m7"))]])
med_photo_keyboard8= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 9 вопроса",callback_data=quiz_photo_callback.new(next="m8"))]])
med_photo_keyboard9= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 10 вопроса",callback_data=quiz_photo_callback.new(next="m9"))]])
med_photo_keyboard10= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 11 вопроса",callback_data=quiz_photo_callback.new(next="m10"))]])
med_photo_keyboard11= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 12 вопроса",callback_data=quiz_photo_callback.new(next="m11"))]])
med_photo_keyboard12= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 13 вопроса",callback_data=quiz_photo_callback.new(next="m12"))]])