import re

from aiogram import types

from loader import db

List_Of_Pattern_regex = [
    "^((1)|([оО]дну( звезду)?)|([оО]дин))$",
    "^([Пп][её]тр\s([Аа]лексеевич|2|[iI]{2}|[Вв]торой))$",
    "^(([Пп]ятнадцатый\s)?([Аа]рбитражный\s)?([Аа]пелляционный\s)?[Сс]уд)$",
    "^(['']?(12|[Дд]венадцать)\sстульев['']?)$",
    "^(([Гг]ородская\s[Дд]ума)|[Дд]ума)$",
    "^(([Вв]\s)?1941(\s?[Гг]((\.)|(од[у]?))?)?)|(([Вв]\s)?[Тт]ысяча девятьсот сорок первом(\s?г((\.)|(оду))?)?)$",
    "^(([Пп][её]тр\s)?[Вв]рангель)$",
    "^(([Фф]рейд(\s*,*\s*|\.|\sи\s)[Юю]нг)|([Юю]нг(\s*,*\s*|\.|\sи\s)[Фф]рейд))$",
    "^(\s*[Аа]мерикански(м|й)\s*(\s[Мм]ост(ом)?)?\s?)$",
    "^(([Вв]\s)?1911(\s?[Гг]((\.)|(од[у]?))?)?)|(([Вв]\s)?[Тт]ысяча девятьсот одиннадцатом(\s?г((\.)|(оду))?)?)$",
    "^(\s*[Нн]еобарокко\s*)$",
    "^(([Вв]\s)?1901(\s?[Гг]((\.)|(од[у]?))?)?)|(([Вв]\s)?[Тт]ысяча девятьсот первом(\s?г((\.)|(оду))?)?)$",
    "^(([Вв]\s)?1914(\s?[Гг]((\.)|(од[у]?))?)?)|(([Вв]\s)?[Тт]ысяча девятьсот четырнадцатом(\s?г((\.)|(оду))?)?)$"
]


async def check_answer_medium_1(message: types.Message, str_ans1):
    result = re.search(str(List_Of_Pattern_regex[0]), str(str_ans1), re.IGNORECASE)
    if result is not None:
        return "Вопрос 1: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 1: Неправильный ответ!"


async def check_answer_medium_2(message: types.Message, str_ans2):
    result = re.search(str(List_Of_Pattern_regex[1]), str(str_ans2), re.IGNORECASE)
    if result is not None:
        return "Вопрос 2: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 2: Неправильный ответ!"


async def check_answer_medium_3(message: types.Message, str_ans3):
    result = re.search(str(List_Of_Pattern_regex[2]), str(str_ans3), re.IGNORECASE)
    if result is not None:
        return "Вопрос 3: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 3: Неправильный ответ!"


async def check_answer_medium_4(message: types.Message, str_ans4):
    result = re.search(str(List_Of_Pattern_regex[3]), str(str_ans4), re.IGNORECASE)
    if result is not None:
        return "Вопрос 4: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 4: Неправильный ответ!"


async def check_answer_medium_5(message: types.Message, str_ans5):
    result = re.search(str(List_Of_Pattern_regex[4]), str(str_ans5), re.IGNORECASE)
    if result is not None:
        return "Вопрос 5: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 5: Неправильный ответ!"


async def check_answer_medium_6(message: types.Message, str_ans6):
    result = re.search(str(List_Of_Pattern_regex[5]), str(str_ans6), re.IGNORECASE)
    if result is not None:
        return "Вопрос 6: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 6: Неправильный ответ!"


async def check_answer_medium_7(message: types.Message, str_ans7):
    result = re.search(str(List_Of_Pattern_regex[6]), str(str_ans7), re.IGNORECASE)
    if result is not None:
        return "Вопрос 7: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 7: Неправильный ответ!"


async def check_answer_medium_8(message: types.Message, str_ans8):
    result = re.search(str(List_Of_Pattern_regex[7]), str(str_ans8), re.IGNORECASE)
    if result is not None:
        return "Вопрос 8: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 8: Неправильный ответ!"


async def check_answer_medium_9(message: types.Message, str_ans9):
    result = re.search(str(List_Of_Pattern_regex[8]), str(str_ans9), re.IGNORECASE)
    if result is not None:
        return "Вопрос 9: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 9: Неправильный ответ!"


async def check_answer_medium_10(message: types.Message, str_ans10):
    result = re.search(str(List_Of_Pattern_regex[9]), str(str_ans10), re.IGNORECASE)
    if result is not None:
        return "Вопрос 10: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 10: Неправильный ответ!"


async def check_answer_medium_11(message: types.Message, str_ans11):
    result = re.search(str(List_Of_Pattern_regex[10]), str(str_ans11), re.IGNORECASE)
    if result:
        return "Вопрос 11: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 11: Неправильный ответ!"


async def check_answer_medium_12(message: types.Message, str_ans12):
    result = re.search(str(List_Of_Pattern_regex[11]), str(str_ans12), re.IGNORECASE)
    if result is not None:
        return "Вопрос 12: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 12: Неправильный ответ!"


async def check_answer_medium_13(message: types.Message, str_ans13):
    result = re.search(str(List_Of_Pattern_regex[12]), str(str_ans13), re.IGNORECASE)
    if result is not None:
        return "Вопрос 13: Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос 13: Неправильный ответ!"


async def check_answer_medium(message: types.Message, str_ans, num):
    result = re.search(str(List_Of_Pattern_regex[num-1]), str(str_ans), re.IGNORECASE)
    if result is not None:
        return "Вопрос " + str(num) + ": Правильный ответ!"
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        return "Вопрос " + str(num) + ": Неправильный ответ!"

