"""
Команды, по которым пользователь осуществляет запросы чат-боту.
"""

from aiogram import types
from bot_app import messages

from bot_app import dp
from bot_app import utils

import bot_app.data_fetcher as data_fetcher

from bot_app.settings import Student as StudentData

# Здесь должна проходить авторизация пользователя, и инициализация дата класса студента

StudentData.group_id = data_fetcher.getGroupID('ППСА-3')


# Первый запуск
@dp.message_handler(commands=['start'])
async def startDialog(message: types.Message):
    await message.reply(messages.GREETINGS.substitute(user=message.from_user.username))


# Показ кнопок для получения расписания
@dp.message_handler(commands=['schedule'])
async def showButtons(message: types.Message):
    
    today_button = types.KeyboardButton(text="Занятия сегодня")
    tommorow_button = types.KeyboardButton(text="Занятия завтра")
    this_week_button = types.KeyboardButton(text="Текущая неделя")
    next_week_button = types.KeyboardButton(text="Следующая неделя")
    
    
    keyboard = types.ReplyKeyboardMarkup(
        one_time_keyboard=False, resize_keyboard=True
    ).row(today_button, tommorow_button).row(this_week_button, next_week_button)

    await message.answer(text=messages.START_SCHEDULE, reply_markup=keyboard)


# ===== ОТПРАВИТЬ РАСПИСАНИЕ ПО ID ДАТЫ  =====
async def sendLessonsByDateID(message: types.Message, date_id: int):
    # Если расписание найдено, то выводим занятие с соответствующей датой
    # Иначе пишем, что занятий в расписании нет
    if (date_id):
        res = await data_fetcher.getDatedLessons(StudentData.group_id, date_id)

        # Если в попытках получить запрос что-то сломалось,
        # то сообщим об этом пользоваетлю
        if not res:
            await message.reply(messages.SOMETHING_BROKEN)
        else:
            return await message.reply(utils.fillLessonsMessage(res=res))
    else:
        await message.reply(messages.NO_LESSONS)


# Отправить занятия на текущий день
@dp.message_handler(lambda msg: any(word in msg.text.lower() for word in messages.TODAY))
async def sendTodayLessons(messages: types.Message):
    date_id = data_fetcher.getDateID(utils.returnTodayDate())
    await sendLessonsByDateID(messages, date_id=date_id)


# Отправить занятия на следующий день от текущего
@dp.message_handler(lambda msg: any(word in msg.text.lower() for word in messages.TOMORROW))
async def sendTomorrowLessons(messages: types.Message):
    date_id = data_fetcher.getDateID(utils.returnTomorrowDate())
    await sendLessonsByDateID(messages, date_id=date_id)


# ===== ОТПРАВИТЬ ЗАНЯТИЯ ПО НОМЕРУ НЕДЕЛИ =====
async def sendLessonsByWeekNumber(message: types.Message, week_number: int):
    res = await data_fetcher.getWeekLessons(StudentData.group_id, week_number)
    return await message.reply(f'Занятия {week_number}-ой недели\n' + utils.fillLessonsMessage(res=res))


# Отправить расписание на текущую неделю
@dp.message_handler(lambda msg: any(word in msg.text.lower() for word in messages.THIS_WEEK))
async def sendThisWeekLessons(message: types.Message):
    return await sendLessonsByWeekNumber(message=message, week_number=utils.returnWeekNumber())


# Отправить расписания на следующую неделю
@dp.message_handler(lambda msg: any(word in msg.text.lower() for word in messages.NEXT_WEEK))
async def sendNextWeekLessons(message: types.Message):
    week_number = utils.returnWeekNumber()

    # Если текущая неделя первая, то показывает вторую. Иначе наоборот
    if week_number == 1:
        return await sendLessonsByWeekNumber(message=message, week_number=2)
    else:
        return await sendLessonsByWeekNumber(message=message, week_number=1)


# Любой текст, который не попал в остальные команды
@dp.message_handler()
async def allMessagesHandler(message: types.Message):
    await message.reply(messages.SOMETHING_BROKEN)
