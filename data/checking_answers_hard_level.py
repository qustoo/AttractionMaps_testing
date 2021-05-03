import re

from aiogram import types

from loader import db

List_Of_Pattern_regex = [
    "^((стало)\s+(перв(ым|ой))\s+(зданием|постройкой)?\s*(в)\s+(стране|россии)\s*,*\s*(спроектированным|построенным|созданным)?\s*(специально)?\s*для\s*(размещения)?\s*(морских)\s+(животных)\s*)$",
    "^((является|это)?\s*(развитие)\s+(творческого\s+потенциал(а|ов)|творчества)\s+(студент(ов|а)|ученик(ов|а)),?\s*(а\*так\s+же|и|,)?\s*(организация|предоставление)?\s*(и[х|м])?\s*(полного|полноценного)?\s*(досуга)?\s*)$",
    "^((как)?\s*(поздний)?\s+(памятник)?\s+(конструктивизм[ау])\s*)$",
    "^(((15[.,/\\]0?4[.,/\\]2?0?18)|(15\s*апреля\s*2018\s*(год(а)?)?))\s*матчем\s*чемпионата\s*россии\s*(между)?\s*[,<«]{0,2}\s*(ростов(а|ом)?)[,>»]{0,2}\s*[иc:/]?\s*[,<«]{0,2}\s*(ска[- ]*хабаровск)[,>»]{0,2}\s*([([<{]*2[:/ ]*0[>})])?\s*((15[.,/\\]0?4[.,/\\]2?0?18)|(15\s*апреля\s*2018\s*(год(а)?)?))?\s*|((15[.,/\\]0?4[.,/\\]2?0?18)|(15\s*апреля\s*2018\s*(год(а)?)?))?\s*матчем\s*чемпионата\s*россии\s*(между)?\s*[,<«]{0,2}\s*(ростов(а|ом)?)[,>»]{0,2}\s*[иc:/]?\s*[,<«]{0,2}\s*(ска[- ]*хабаровск)[,>»]{0,2}\s*([([<{]*2[:/ ]*0[>})])?\s*((15[.,/\\]0?4[.,/\\]2?0?18)|(15\s*апреля\s*2018\s*(год(а)?)?))\s*)$",
    "^((эклектик[ау]*|барокко|классицизм[ау]*)\s+((?!\2)(эклектик[ау]*|барокко|классицизм[ау]*))\s+((?!\2|\3)(эклектик[ау]*|барокко|классицизм[ау]*))\s*)$",
    "^(в?\s*1967\s*(год[у]?)?[аи]?[,. ]+(скульптор(ом)?)?\s*(был|явля(естся|лся))?\s*((э[., ]+м[., ]+)?\s*мирзоев)\s*)$",
    "^((в\s*)?2019\s+(год(у)?)[, ]+(по\s+инициативе)?\s+ветеранских\s+организаций\s+воинов-интернационалистов\s+и\s+(также)?\s*(лично(го|му)*)?\s*(содейств(ию|у))?\s*(губернатор[ау]?)?\s*(ростов(ской|а)?)?\s*(обл(асти|[.]?))\s+(в[., ]+ю[., ]+)?\s*(голубев[ау]*)\s*)$"
    "^((что)?\s*(на|у|вдоль)?\s*алле[яуеи]\s*((вы|по|у)сажен[оа])\s*(6[,.]5\s*тысяч[и]?|((6|шесть)\s*тысяч[и]?\s*(500|пятьсот)))\s*((этих)?\s*(красив(ейших|ых))?\s*(цветов|роз)\s*))$",
    "^((первое)?\s*(богослужение)?\s*в?\s*(церкви)?\s*(было)?\s*(совершено)?\s*в?\s*1994\s*(год[еуа]?)\s*(в\s*память)?\s*(святого|преподобного)\s*(велико)?мученика\s*георги[яй]\s*победоносца\s*)$",
    "^((обратить|привлечь|ознакомить|ознакомление|привлечение|ознакомление)\s*(внимани[яеи])?\s*(читател(я|ей)|людей|человек|прихожан|приоходящих)\s*[кс]\s*(литературно-историческому|историко-литературному)\s*наследи[ею]\s*(н[,.]?\s*м[,.]?\s*)?\s*карамзин[ау]?\s*)$"
    "^(\s*[,.(<'\"}\[]*\s*вечен\s*ваш\s*подвиг\s*в\s*сердцах\s*поколений\s*грядущих\s*[,,'\")>}\]]*\s*)$",
    "^(\s*(он[о]?)?\s*было?\s*национализировано?\s*[,.]?\s*и?\s*в\s*н[её]м\s*(разместилась|расположилась)\s*(10|десятая)?\s*(городская)?\s*(больница|(поли)?клиника)\s*)$"
    "^((\s*в\s*связи\s*)?\s*с\s*отсутствием\s*(православных)?\s*(храмов|церквей)\s*в\s*(большом)?\s*(жилом)?\s*(районе|рай-оне|рай.)\s*(города)?.*)$",
    "^((для)?\s*(того\s*чтобы)?\s*(было)?\s*(возможно|можно\s*было)?\s*(спуск[ау]?|спуститься)\s*к\s*(дону|набережной).*)$",
    "^((((\s*церковь)\s*всех\s*святых\s*)|(новопоселенское\s*(городское)?\s*кладбище\s*))[,.и]{0,2}((?!\2)(((\s*церковь)\s*всех\s*святых\s*)|(\s*новопоселенское\s*(городское)?\s*кладбище\s*))?))$"
]


async def check_answer_hard_1(message: types.Message, str_ans1):
    result = re.search(str(List_Of_Pattern_regex[0]), str(str_ans1), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 1: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 1: Неправильный ответ!")


async def check_answer_hard_2(message: types.Message, str_ans2):
    result = re.search(str(List_Of_Pattern_regex[1]), str(str_ans2), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 2: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 2: Неправильный ответ!")


async def check_answer_hard_3(message: types.Message, str_ans3):
    result = re.search(str(List_Of_Pattern_regex[2]), str(str_ans3), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 3: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 3: Неправильный ответ!")


async def check_answer_hard_4(message: types.Message, str_ans4):
    result = re.search(str(List_Of_Pattern_regex[3]), str(str_ans4), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 4: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 4: Неправильный ответ!")


async def check_answer_hard_5(message: types.Message, str_ans5):
    result = re.search(str(List_Of_Pattern_regex[4]), str(str_ans5), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 5: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 5: Неправильный ответ!")


async def check_answer_hard_6(message: types.Message, str_ans6):
    result = re.search(str(List_Of_Pattern_regex[5]), str(str_ans6), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 6: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 6: Неправильный ответ!")


async def check_answer_hard_7(message: types.Message, str_ans7):
    result = re.search(str(List_Of_Pattern_regex[6]), str(str_ans7), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 7: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 7: Неправильный ответ!")


async def check_answer_hard_8(message: types.Message, str_ans8):
    result = re.search(str(List_Of_Pattern_regex[7]), str(str_ans8), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 8: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 8: Неправильный ответ!")


async def check_answer_hard_9(message: types.Message, str_ans9):
    result = re.search(str(List_Of_Pattern_regex[8]), str(str_ans9), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 9: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 9: Неправильный ответ!")


async def check_answer_hard_10(message: types.Message, str_ans10):
    result = re.search(str(List_Of_Pattern_regex[9]), str(str_ans10), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 10: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 10: Неправильный ответ!")
