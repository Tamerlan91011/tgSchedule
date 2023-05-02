"""
Команды, по которым пользователь осуществляет запросы чат-боту.
"""

from aiogram import types

from bot_app.config import connection
from bot_app import messages

from bot_app import dp

# Первый запуск
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(messages.GREETINGS)


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
    await message.answer(text="Расписание на:", reply_markup=keyboard)


# Любой текст, который не попал в остальные команды
@dp.message_handler()
async def allMessagesHandler(message: types.Message):
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM personnel_user")

    dbData = cursor.fetchall()

    try:
        intUserWithId = dbData[int(message.text) - 1]
        userName = intUserWithId[1]

        await message.answer(intUserWithId)
        await message.answer(userName)
    except:
        await message.answer(f"Введите целое число от 1 до {len(dbData)}")

 
