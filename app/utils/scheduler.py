import json
import aioschedule
from datetime import datetime, timedelta, timezone
import asyncio
from utils.get_weather import weather


async def scheduled_weather(mode):
    with open('opt.json', 'r') as f:
        data = json.load(f)
    for i in data:
        if data[str(i)]['alarm_mode'] == 1 and mode == 1 and data[str(i)]['alarm_on'] == 1:
            await weather('Полтава', 8, i)
        elif data[str(i)]['alarm_mode'] == 2 and mode == 2 and data[str(i)]['alarm_on'] == 1:
            await weather('Pruszcz gdański', 8, i)
    f.close()


async def set_scheduler():
    kiev_timezone = timezone(timedelta(hours=3))
    aioschedule.set_timezone(kiev_timezone)
    aioschedule.every().monday.at("7:00").do(scheduled_weather, 1)
    aioschedule.every().tuesday.at("7:00").do(scheduled_weather, 1)
    aioschedule.every().wednesday.at("7:00").do(scheduled_weather, 1)
    aioschedule.every().thursday.at("7:00").do(scheduled_weather, 1)
    aioschedule.every().friday.at("7:00").do(scheduled_weather, 1)
    aioschedule.every().saturday.at("10:00").do(scheduled_weather, 1)
    aioschedule.every().sunday.at("10:00").do(scheduled_weather, 1)

    aioschedule.every().monday.at("6:00").do(scheduled_weather, 2)
    aioschedule.every().monday.at("18:00").do(scheduled_weather, 2)
    aioschedule.every().tuesday.at("6:00").do(scheduled_weather, 2)
    aioschedule.every().tuesday.at("18:00").do(scheduled_weather, 2)
    aioschedule.every().wednesday.at("6:00").do(scheduled_weather, 2)
    aioschedule.every().wednesday.at("18:00").do(scheduled_weather, 2)
    aioschedule.every().thursday.at("6:00").do(scheduled_weather, 2)
    aioschedule.every().thursday.at("18:00").do(scheduled_weather, 2)
    aioschedule.every().friday.at("6:00").do(scheduled_weather, 2)
    aioschedule.every().friday.at("18:00").do(scheduled_weather, 2)
    aioschedule.every().saturday.at("11:00").do(scheduled_weather, 2)
    aioschedule.every().sunday.at("11:00").do(scheduled_weather, 2)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
