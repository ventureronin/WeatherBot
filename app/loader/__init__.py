import json
# from app.config import tg_token
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import StatesGroup, State

with open('config', 'r')as file:
    tg_token = file.read().strip()
bot = Bot(token=tg_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
# dp.middleware.setup(LoggingMiddleware())
with open('opt.json', 'r') as f:
    data = json.load(f)
admin_id = data['424567224']['id']


class CurrentState(StatesGroup):
    city = State()
    choice_day = State()
    settings = State()
