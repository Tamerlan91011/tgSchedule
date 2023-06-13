"""Ядро приложения, хранящее в себе инициализацию главных компонентов: объект класса 'бот', и объект класса 'диспетчер'"""

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .settings import API_TOKEN


storage = MemoryStorage()
# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
