"""Ядро приложения, хранящее в себе инициализацию главных компонентов: объект класса 'бот', и объект класса 'диспетчер'"""

from aiogram import Bot, Dispatcher

from .config import API_TOKEN

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
