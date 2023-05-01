import logging
from aiogram import Bot, Dispatcher, executor, types
from dbConnection import connection
import json

# Configure logging
logging.basicConfig(level=logging.INFO)


API_TOKEN = '6229035910:AAERoS5lCJaFZbGaAaJrTDOeCCF3syV9eYc'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# * Если команда start...
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nВведи число и получишь фамилию одного из преподавателей")


# * Если отправляешь какой либо текст, бот вернет полученные данные из bd
@dp.message_handler()
async def echo(message: types.Message):
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
