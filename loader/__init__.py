import json
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import StatesGroup, State

token = "475802048:AAGqfuSimHHzr3sJFhE_xzSLs3Cl6n4xCS8"  # main
# token = "6179975818:AAEoZFFdUIxPF8cJJbAQpSFFSKuv73_ZLzY"  # test

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
# dp.middleware.setup(LoggingMiddleware())
with open('opt.json', 'r') as f:
    data = json.load(f)
admin_id = data['424567224']['id']


class CurrentState(StatesGroup):
    city = State()
    choice_day = State()
    settings = State()
