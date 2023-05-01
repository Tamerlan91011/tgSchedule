from aiogram import types
from config import connection
import MESSAGES


async def startHandler(message: types.Message):
    await message.reply("Привет!\nВведи число и получишь фамилию одного из преподавателей")


async def buttonsHandler(message: types.Message):
    buttons = [
        [types.KeyboardButton(text=f"{MESSAGES.TODAY}")],
        [types.KeyboardButton(text=f"{MESSAGES.TOMOROW}")],
        [types.KeyboardButton(text=f"{MESSAGES.THIS_WEEK}")],
        [types.KeyboardButton(text=f"{MESSAGES.NEXT_WEEK}")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons, one_time_keyboard=True)
    await message.answer(text="Расписание на:", reply_markup=keyboard)


async def allMessagesHandler(message: types.Message):
    with connection:
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
