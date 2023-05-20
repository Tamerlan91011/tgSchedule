"""
Команды, по которым пользователь осуществляет запросы чат-боту.
"""

from aiogram import types
from bot_app import messages

from bot_app import dp
from bot_app.utils import *

import bot_app.data_fetcher as data_fetcher

from bot_app.settings import Student as StudentData

# Здесь должна проходить авторизация пользователя, и инициализация дата класса студента

StudentData.group_id = data_fetcher.get_group_id('ППСА-3') 


# Первый запуск
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(messages.GREETINGS)


# Показ кнопок для получения расписания
@dp.message_handler(commands=['schedule'])
async def buttons(message: types.Message):
    buttons = [
        [types.KeyboardButton(text=f"{messages.TODAY}")],
        [types.KeyboardButton(text=f"{messages.TOMOROW}")],
        [types.KeyboardButton(text=f"{messages.THIS_WEEK}")],
        [types.KeyboardButton(text=f"{messages.NEXT_WEEK}")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons, one_time_keyboard=True)
    await message.answer(text=messages.START_SCHEDULE, reply_markup=keyboard)


# Получить расписание по ID даты в базе расписаний
async def getLessonsByDateID(message: types.Message, date_id: int):
    # Если расписание найдено, то выводим занятие с соответствующей датой
    # Иначе пишем, что занятий в расписании нет
    if (date_id):
        res = await data_fetcher.get_dated_lessons(StudentData.group_id, date_id)
        
        # Если в попытках получить запрос что-то сломалось, 
        # то сообщим об этом пользоваетлю
        if not res:
            await message.reply(messages.SOMETHING_BROKEN)
        else:
            return await message.reply(fillLessonsMessage(res=res))
    else:
        await message.reply(messages.NO_LESSONS)


# Получить занятия на текущий день
@dp.message_handler(regexp=f"{messages.TODAY}")
async def getTodayLessons(messages: types.Message):
    date_id = data_fetcher.get_date_id(getTodayDate())
    await getLessonsByDateID(messages, date_id=date_id)


# Получить занатия на следующий день от текущего
@dp.message_handler(regexp=f"{messages.TOMOROW}")
async def getTomorrowLessons(messages: types.Message):
    date_id = data_fetcher.get_date_id(getTomorrowDate())
    await getLessonsByDateID(messages, date_id=date_id)


async def getLessonsByWeekNumber(message: types.Message, week_number:int):
    res = await data_fetcher.get_week_lessons(StudentData.group_id, week_number)
    return await message.reply(fillLessonsMessage(res=res))


# Получение расписания на первую неделю
@dp.message_handler(regexp=f"{messages.THIS_WEEK}")
async def getThisWeekLessons(message: types.Message):
    await getLessonsByWeekNumber(message=message, week_number=getWeekNumber())


# Получение расписания на вторую неделю
@dp.message_handler(regexp=f"{messages.NEXT_WEEK}")
async def getNextWeekLessons(message: types.Message):
    week_number = getWeekNumber()
    
    # Если текущая неделя первая, то показывает вторую. Иначе наоборот
    if week_number == 1:
        await getLessonsByWeekNumber(message=message, week_number=2)
    else:
        await getLessonsByWeekNumber(message=message, week_number=1)


# Любой текст, который не попал в остальные команды
# @dp.message_handler()
# async def allMessagesHandler(message: types.Message):
#     cursor = connection.cursor()
#     cursor.execute(allPersonnelUser)

#     dbData = cursor.fetchall()

#     try:
#         intUserWithId = dbData[int(message.text) - 1]
#         userName = intUserWithId[1]

#         await message.answer(intUserWithId)
#         await message.answer(userName)
#     except:
#         await message.answer(f"Введите целое число от 1 до {len(dbData)}")