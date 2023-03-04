import asyncio
from aiogram import executor
# token, storage, bot, dp, CurrentState
from loader.handlers import *  # !!!!!!!!!!!!!!!

from utils import set_default_commands
from utils.scheduler import set_scheduler


async def on_startup(dispatcher):
    # для всех пользователей
    with open('opt.json', 'r') as f:
        data = json.load(f)
    f.close()
    # for i in data:
    #     await bot .send_message(chat_id=i,
    #                            text=f"Бот перезапущен, что бы он 'слышал' названия городов - введите команду /start")
    await set_default_commands(dispatcher)
    asyncio.ensure_future(set_scheduler())
    print("Bot starting... OK🤖")


async def on_shutdown(dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           skip_updates=True)
