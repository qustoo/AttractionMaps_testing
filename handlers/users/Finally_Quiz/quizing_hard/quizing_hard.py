import re

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hitalic, hbold

from handlers.users.get_my_rating import get_my_rating
from keyboards.inline.quiz_keyboard import YesOrNoFinishKeyboard
from quiz_all_files.Quiz_Questions.questions_quiz import Hard_Array_Questions
from loader import dp, photo_db, db
from aiogram import types
from states.MachineStates_For_Quiz import QuizHard, YesOrNoFinishShowRating

ListPatternsRegexHardLevel = [
    "^((стало)\s+(перв(ым|ой))\s+(зданием|постройкой)?\s*(в)\s+(стране|россии)\s*,*\s*(спроектированным|построенным|созданным)?\s*(специально)?\s*для\s*(размещения)?\s*(морских)\s+(животных)\s*)$",
    "^((является|это)?\s*(развитие)\s+(творческого\s+потенциал(а|ов)|творчества)\s+(студент(ов|а)|ученик(ов|а)),?\s*(а\*так\s+же|и|,)?\s*(организация|предоставление)?\s*(и[х|м])?\s*(полного|полноценного)?\s*(досуга)?\s*)$",
    "^((как)?\s*(поздний)?\s+(памятник)?\s+(конструктивизм[ау])\s*)$",
    "^(\s*((состоял[оа]сь|произошл[аоу]|открыт(ие|ем))?\s*(откры(тие|лась|тием)|состоял[оа]сь|произошл[аоуи]|[«,.\({\[\'\"]*\s*ростов\s*арен[ыа]\s*[»,.\"\'\)}\]]*)?\s*([«,.\({\[\'\"]*\s*ростов\s*арен[ыа]\s*[»,.\"\'\)}\]]*|откры(тие|лась)|состоял[оа]сь|произошл[аоу])?\s*)?\s*(15\s*апреля\s*2018\s*(г\.?(од[ау]?)?)|15[.,/\\:;]?0?4[.,/\\:;]?(20)?18\s*)?\s*матч(ем)?\s*(чемпионат(а|ом)?|ч\s*м\s*)\s*россии\s*(между)?\s*[«,.\({\[\'\"]*\s*ростов(а|ом)?\s*[»,.\"\'\)}\]]*\s*[ис]?\s*[«,.\({\[\'\"]*ска\s*[-—–]*\s*хабаровск(ом)?\s*[»,.\"\'\)}\]]*\s*([\(\[\{]*\s*2\s*[:;/\\]*\s*0\s*[\)\}\}])?\s*(15\s*апреля\s*2018\s*(г\.?\s*(од[ау]?)?)|15[.,/\\:;]?0?4[.,/\\:;]?(20)?18\s*)?\s*)$"
    "^((эклектик[ау]*|барокко|классицизм[ау]*)\s*[,и]?\s*((?!\2)(эклектик[ау]*|барокко|классицизм[ау]*))\s*([аи]\s*так\s*же\s*)?\s*[,и]?\s*((?!\2|\3)(эклектик[ау]*|барокко|классицизм[ау]*))\s*)$",
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

ListCorrectAnswersHardLevel = [
    "стало первым в стране, спроектированным специально для размещения морских животных",
    "развитие творческого потенциала студентов и организация их полноценного досуга",
    "поздний памятник конструктивизма",
    "открытие «ростов арены» состоялось  15 апреля 2018 г  матчем чемпионата россии между «ростовом» и «ска-хабаровск» (2:0)",
    "эклектика барокко классицизм",
    "1967 Э. М. Мирзоев",
    "в 2019 году по инициативе ветеранских организаций воинов-интернационалистов и личному содействию губернатора ростовской области В.Ю. Голубева",
    "на аллее высажено 6,5 тысяч этих красивейших цветов",
    "было совершено в 1994 году в память святого великомученика Георгия Победоносца",
    "привлечение внимания читателей к литературно-историческому наследию Н. М. Карамзина",
    "Вечен ваш подвиг в сердцах поколений грядущих",
    "был национализирован и в нем расположилась больница",
    "с отсутствием православных храмов в районе",
    "для того чтобы можно было спуститься к дону",
    "церковь всех святых или новопоселенское городское кладбище"
]


@dp.message_handler(Command("quiz_hard"), state=None)
async def enter_hard_test(message: types.Message):
    # присылаем фотку и клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_1'), 'rb'))
    await message.answer("Вопрос 1:\n" + Hard_Array_Questions[0])

    await QuizHard.Q1.set()


@dp.message_handler(state=QuizHard.Q1)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_first_hard = message.text
    await state.update_data(answer1=answer_first_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_2'), 'rb'))
    await message.answer("Вопрос 2:\n" + Hard_Array_Questions[1])
    await QuizHard.Q2.set()


@dp.message_handler(state=QuizHard.Q2)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_2nd_hard = message.text
    await state.update_data(answer2=answer_2nd_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_3'), 'rb'))
    await message.answer("Вопрос 3:\n" + Hard_Array_Questions[2])
    await QuizHard.Q3.set()


@dp.message_handler(state=QuizHard.Q3)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_3rd_hard = message.text
    await state.update_data(answer3=answer_3rd_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_4'), 'rb'))
    await message.answer("Вопрос 4:\n" + Hard_Array_Questions[3])
    await QuizHard.Q4.set()


@dp.message_handler(state=QuizHard.Q4)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_4th_hard = message.text
    await state.update_data(answer4=answer_4th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_5'), 'rb'))
    await message.answer("Вопрос 5:\n" + Hard_Array_Questions[4])
    await QuizHard.Q5.set()


@dp.message_handler(state=QuizHard.Q5)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_5th_hard = message.text
    await state.update_data(answer5=answer_5th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_6'), 'rb'))
    await message.answer("Вопрос 6:\n" + Hard_Array_Questions[5])
    await QuizHard.Q6.set()


@dp.message_handler(state=QuizHard.Q6)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_6th_hard = message.text
    await state.update_data(answer6=answer_6th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_7'), 'rb'))
    await message.answer("Вопрос 7:\n" + Hard_Array_Questions[6])
    await QuizHard.Q7.set()


@dp.message_handler(state=QuizHard.Q7)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_7th_hard = message.text
    await state.update_data(answer7=answer_7th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_8'), 'rb'))
    await message.answer("Вопрос 8:\n" + Hard_Array_Questions[7])
    await QuizHard.Q8.set()


@dp.message_handler(state=QuizHard.Q8)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_8th_hard = message.text
    await state.update_data(answer8=answer_8th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_9'), 'rb'))
    await message.answer("Вопрос 9:\n" + Hard_Array_Questions[8])
    await QuizHard.Q9.set()


@dp.message_handler(state=QuizHard.Q9)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_9th_hard = message.text
    await state.update_data(answer9=answer_9th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_10'), 'rb'))
    await message.answer("Вопрос 10:\n" + Hard_Array_Questions[9])
    await QuizHard.Q10.set()


@dp.message_handler(state=QuizHard.Q10)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_10th_hard = message.text
    await state.update_data(answer10=answer_10th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_11'), 'rb'))
    await message.answer("Вопрос 11:\n" + Hard_Array_Questions[10])
    await QuizHard.Q11.set()


@dp.message_handler(state=QuizHard.Q11)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_11th_hard = message.text
    await state.update_data(answer11=answer_11th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_12'), 'rb'))
    await message.answer("Вопрос 12:\n" + Hard_Array_Questions[11])
    await QuizHard.Q12.set()


@dp.message_handler(state=QuizHard.Q12)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_12th_hard = message.text
    await state.update_data(answer12=answer_12th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_13'), 'rb'))
    await message.answer("Вопрос 13:\n" + Hard_Array_Questions[12])
    await QuizHard.Q13.set()


@dp.message_handler(state=QuizHard.Q13)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_13th_hard = message.text
    await state.update_data(answer13=answer_13th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_14'), 'rb'))
    await message.answer("Вопрос 14:\n" + Hard_Array_Questions[13])
    await QuizHard.Q14.set()


@dp.message_handler(state=QuizHard.Q14)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_11th_hard = message.text
    await state.update_data(answer14=answer_11th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_15'), 'rb'))
    await message.answer("Вопрос 15:\n" + Hard_Array_Questions[14])
    await QuizHard.Q15.set()


@dp.message_handler(state=QuizHard.Q15)
async def check_answers_finish(message: types.Message, state: FSMContext):
    # получаем все данные
    data = await state.get_data()

    # пишем их в переменные
    answer_first = data.get("answer1")
    answer_second = data.get("answer2")
    answer_third = data.get("answer3")
    answer_fourth = data.get("answer4")
    answer_5th = data.get("answer5")
    answer_6th = data.get("answer6")
    answer_7th = data.get("answer7")
    answer_8th = data.get("answer8")
    answer_9th = data.get("answer9")
    answer_10th = data.get("answer10")
    answer_11th = data.get("answer11")
    answer_12th = data.get("answer12")
    answer_13th = data.get("answer13")
    answer_14th = data.get("answer14")
    answer_15th = data.get("answer15")
    ListAnswersFromUserHardLevel = [answer_first,
                                    answer_second,
                                    answer_third,
                                    answer_fourth,
                                    answer_5th,
                                    answer_6th,
                                    answer_7th,
                                    answer_8th,
                                    answer_9th, answer_10th, answer_11th, answer_12th, answer_13th, answer_14th,
                                    answer_15th]

    # Обнуляем рейтинг
    db.update_rating_hard(message.from_user.id, 0)

    result_str = ""
    for i in range(0, len(ListAnswersFromUserHardLevel)):
        if re.search(ListPatternsRegexHardLevel[i], str(ListAnswersFromUserHardLevel[i]), re.IGNORECASE) is not None:
            result_str += hbold(f'Вопрос {i + 1}') + hbold(' - Правильный ответ!') + "\n\n"
            # postgresql : rate = await db.get_rating_hard(id=message.from_user.id, name=message.from_user.full_name)
            rate = db.get_rating_hard(id=message.from_user.id)
            # postgresql :  await db.update_rating_hard(id=message.from_user.id, rating=rate + 6.0)
            db.update_rating_hard(id=message.from_user.id, rating=rate + 6.0)
        else:
            result_str += hitalic(f'Вопрос {i + 1}') + hbold(' - Неправильный ответ!\n') + hitalic(
                f'Корректным ответом будет: \n') + hbold(f'{ListCorrectAnswersHardLevel[i]}') + "\n\n"
    await message.answer(text="Ваши ответы:\n\n" + result_str)

    await message.answer(text="Хотите увидеть свой рейтинг?", reply_markup=YesOrNoFinishKeyboard)
    await YesOrNoFinishShowRating.Q1.set()


@dp.message_handler(text="Да", state=YesOrNoFinishShowRating.Q1)
async def YesShowRating(message: types.message, state: FSMContext):
    await get_my_rating(message)
    await message.answer(text="Спасибо за прохождение викторины", reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(text="Нет", state=YesOrNoFinishShowRating.Q1)
async def YesShowRating(message: types.message, state: FSMContext):
    await message.answer(text=hitalic("Спасибо за прохождение викторины"), reply_markup=ReplyKeyboardRemove())
    await state.finish()
