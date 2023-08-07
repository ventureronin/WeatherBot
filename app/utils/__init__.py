from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить/перезапустить бота"),
            types.BotCommand("help", "Вывести 'помощь':объяснения и обозначения"),
            types.BotCommand("settings", "Настройки"),
            types.BotCommand("location", "Поделиться с ботом своей геолокацией")
        ]
    )
