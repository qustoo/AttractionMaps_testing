import re

from aiogram import types
from aiogram.utils.markdown import hbold

from loader import db

List_Of_Pattern_regex = [
    "^((стало)\s+(перв(ым|ой))\s+(зданием|постройкой)?\s*(в)\s+(стране|россии)\s*,*\s*(спроектированным|построенным|созданным)?\s*(специально)?\s*для\s*(размещения)?\s*(морских)\s+(животных)\s*)$",
    "^((является|это)?\s*(развитие)\s+(творческого\s+потенциал(а|ов)|творчества)\s+(студент(ов|а)|ученик(ов|а)),?\s*(а\*так\s+же|и|,)?\s*(организация|предоставление)?\s*(и[х|м])?\s*(полного|полноценного)?\s*(досуга)?\s*)$",
    "^((как)?\s*(поздний)?\s+(памятник)?\s+(конструктивизм[ау])\s*)$",
    "^(\s*((состоял[оа]сь|произошл[аоу]|открытие)?\s*(откры(тие|лась)|состоял[оа]сь|произошл[аоу]|[«,.\({\[\'\"]*\s*ростов\s*арен[ыа]\s*[»,.\"\'\)}\]]*)?\s*([«,.\({\[\'\"]*\s*ростов\s*арен[ыа]\s*[»,.\"\'\)}\]]*|откры(тие|лась)|состоял[оа]сь|произошл[аоу])?\s*)?\s*(15\s*апреля\s*2018\s*(г\.?(од[ау]?)?)|15[.,/\\:;]?0?4[.,/\\:;]?(20)?18\s*)?\s*матч(ем)?\s*(чемпионат(а|ом)?|ч\s*м\s*)\s*россии\s*(между)?\s*[«,.\({\[\'\"]*\s*ростов(а|ом)?\s*[»,.\"\'\)}\]]*\s*[ис]?\s*[«,.\({\[\'\"]*ска\s*[-—–]*\s*хабаровск(ом)?\s*[»,.\"\'\)}\]]*\s*[\(\[\{]*\s*2\s*[:;/\\]*\s*0\s*[\)\}\}]*\s*(15\s*апреля\s*2018\s*(г\.?\s*(од[ау]?)?)|15[.,/\\:;]?0?4[.,/\\:;]?(20)?18\s*)?\s*)$",
    "^((эклектик[ау]*|барокко|классицизм[ау]*)\s*,?\s*((?!\2)(эклектик[ау]*|барокко|классицизм[ау]*))\s*,?\s*((?!\2|\3)(эклектик[ау]*|барокко|классицизм[ау]*))\s*)$",
    "^(в?\s*1967\s*(год[у]?)?[аи]?[,. ]+(скульптор(ом)?)?\s*(был|явля(естся|лся))?\s*((э[., ]+м[., ]+)?\s*мирзоев)\s*)$",
    "^((в\s*)?2019\s+(год(у)?)[, ]+(по\s+инициативе)?\s+ветеранских\s+организаций\s+воинов-интернационалистов\s+и\s+(также)?\s*(лично(го|му)*)?\s*(содейств(ию|у))?\s*(губернатор[ау]?)?\s*(ростов(ской|а)?)?\s*(обл(асти|[.]?))\s+(в[., ]+ю[., ]+)?\s*(голубев[ау]*)\s*)$",
    "^((что)?\s*(на|у|вдоль)?\s*алле[яуеи]\s*((вы|по|у)сажен[оа])\s*(6[,.]5\s*тысяч[и]?|((6|шесть)\s*тысяч[и]?\s*(500|пятьсот)))\s*((этих)?\s*(красив(ейших|ых))?\s*(цветов|роз)\s*))$",
    "^((первое)?\s*(богослужение)?\s*в?\s*(церкви)?\s*(было)?\s*(совершено)?\s*в?\s*1994\s*(год[еуа]?)\s*(в\s*память)?\s*(святого|преподобного)\s*(велико)?мученика\s*георги[яй]\s*победоносца\s*)$",
    "^((обратить|привлечь|ознакомить|ознакомление|привлечение|ознакомление)\s*(внимани[яеи])?\s*(читател(я|ей)|людей|человек|прихожан|приоходящих)\s*[кс]\s*(литературно-историческому|историко-литературному)\s*наследи[ею]\s*(н[,.]?\s*м[,.]?\s*)?\s*карамзин[ау]?\s*)$",
    "^(\s*[,.(<'\"}\[]*\s*вечен\s*ваш\s*подвиг\s*в\s*сердцах\s*поколений\s*грядущих\s*[,,'\")>}\]]*\s*)$",
    "^(\s*(он[о]?)?\s*было?\s*национализировано?\s*[,.]?\s*и?\s*в\s*н[её]м\s*(разместилась|расположилась)\s*(10|десятая)?\s*(городская)?\s*(больница|(поли)?клиника)\s*)$",
    "^((\s*в\s*связи\s*)?\s*с\s*отсутствием\s*(православных)?\s*(храмов|церквей)\s*в\s*(большом)?\s*(жилом)?\s*(районе|рай-оне|рай.?)\s*(города)?\s*)$",
    "^((для)?\s*(того\s*чтобы)?\s*(было)?\s*(можно\s*было)?\s*(спуск[ау]?|спуститься)\s*к\s*(дону|набережной)\s*)$",
    "^((((\s*церковь)\s*всех\s*святых\s*)|(новопоселенское\s*(городское)?\s*кладбище\s*))\s*(,|.|и|или){0,2}\s*((?!\2)(((\s*церковь)\s*всех\s*святых\s*)|(\s*новопоселенское\s*(городское)?\s*кладбище\s*))?)\s*)$"
]

List_Of_correct_answers = [
    "стало первым в стране, спроектированным специально для размещения морских животных",
    "развитие творческого потенциала студентов и организация их полноценного досуга",
    "поздний памятник конструктивизма",
    "открытие «ростов арены» состоялось  15 апреля 2018 г  матчем чемпионата россии между «ростовом» и «ска-хабаровск» (2:0)",
    "эклектика барокко классицизм",
    "1967 Э. М. Мирзоев",
    "по инициативе ветеранских организаций воинов-интернационалистов и личному содействию Губернатора Ростовской области В.Ю.Голубева",
    "на аллее высажено 6,5 тысяч этих красивейших цветов",
    "было совершено в 1994 году в память святого великомученика Георгия Победоносца",
    "привлечение внимания читателей к литературно-историческому наследию Н. М. Карамзина",
    "Вечен ваш подвиг в сердцах поколений грядущих",
    "был национализирован и в нем расположилась больница",
    "с отсутствием православных храмов в районе",
    "для того чтобы можно было спуститься к дону",
    "церковь всех святых или новопоселенское городское кладбище"
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


async def check_answer_hard_11(message: types.Message, str_ans):
    result = re.search(str(List_Of_Pattern_regex[10]), str(str_ans), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 11: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 11: Неправильный ответ!")


async def check_answer_hard_12(message: types.Message, str_ans):
    result = re.search(str(List_Of_Pattern_regex[11]), str(str_ans), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 12: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 12: Неправильный ответ!")


async def check_answer_hard_13(message: types.Message, str_ans):
    result = re.search(str(List_Of_Pattern_regex[12]), str(str_ans), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 13: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 13: Неправильный ответ!")


async def check_answer_hard_14(message: types.Message, str_ans):
    result = re.search(str(List_Of_Pattern_regex[13]), str(str_ans), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 14: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 14: Неправильный ответ!")


async def check_answer_hard_15(message: types.Message, str_ans):
    result = re.search(str(List_Of_Pattern_regex[14]), str(str_ans), re.IGNORECASE)
    if result is not None:
        await message.answer("Вопрос 15: Правильный ответ!")
        RATE = db.select_user(id=message.from_user.id)[-1]
        db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    else:
        await message.answer("Вопрос 15: Неправильный ответ!")


async def check_answer_hard(message: types.Message, answers):
    assert (len(answers) == len(List_Of_Pattern_regex))
    res = ""
    for i in range(0, len(answers)):
        if re.search(List_Of_Pattern_regex[i], answers[i], re.IGNORECASE) is not None:
            res += hbold(f"Правильный ответ : {int(i) + 1}\n")
            RATE = db.select_user(id=message.from_user.id)[-1]
            db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
        else:
           res += hbold(f"Неправильный ответ : {int(i) + 1}\n Верным ответом будет :") + f" {List_Of_correct_answers[i]}\n"
    return res

