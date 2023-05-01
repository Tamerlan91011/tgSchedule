import commands
from config import API_TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


#
# * Команда start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await commands.startHandler(message)


#
# * Вызов расписания и кнопок к нему
@dp.message_handler(commands=['schedule'])
async def scheduleHandler(message: types.Message):
    await commands.buttonsHandler(message)


#
# * Любой текст, который не попал в остальные команды
@dp.message_handler()
async def messageHandler(message: types.Message):
    await commands.allMessagesHandler(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
