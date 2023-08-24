import requests
import datetime
import json
import html
from loader import types, bot, admin_id

emoji = {
    "Clear": "\U00002600",
    "Clouds": "\U00002601",
    "Rain": "\U00002614",
    "Drizzle": "\U00002614",
    "Thunderstorm": "\U000026A1",
    "Snow": "\U0001F328",
    "Mist": "\U0001F32B",
    "Skeleton": "\U00002620"
}


async def scheduled_weather(city, num, given_id):
    for item in given_id:
        await weather(city, num, item)


async def single_weather(city, num, callback_query: types.CallbackQuery):
    await weather(city, num, callback_query)


async def weather(city, num, idd):
    try:
        with open('opt.json', 'r') as f:
            my_data = json.load(f)
        f.close()
        logs = open('logs.log', 'a', encoding='utf-8')

        if num == 0:
            r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}"
                             f"&appid=4c67e8632dcc4debbd6a8c08f72cc618&units=metric")
            data = r.json()
            city = data["name"]
            cur_weather = data["main"]["temp"]
            weather_desc = data["weather"][0]["main"]
            if weather_desc in emoji:
                wd = emoji[weather_desc]
            else:
                wd = emoji["Skeleton"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            sunrise_t = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset_t = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
            len_of_day = sunset_t - sunrise_t
            await bot.send_message(chat_id=idd,
                                   text=f"###{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}###\n"
                                        f"Погода в городе: {city}\nТемпература: {cur_weather}°C {wd}\n"
                                        f"Влажность: {humidity}%\nВетер: {wind} м/с\n"
                                        f"Восход: {sunrise_t} Закат: {sunset_t}\n"
                                        f"Продолжительность дня: {len_of_day}")
            await bot.send_message(chat_id=admin_id,
                                   text=f"User:{my_data[str(idd)]['name']}\n Погода в текущий момент в городе {city}")
        else:
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/forecast?q={city}"
                f"&appid=4c67e8632dcc4debbd6a8c08f72cc618&cnt={num}&units=metric"
            )
            data = r.json()
            city = data["city"]["name"]
            output = "###" + city + "###\n"
            zerodate, t = data["list"][0]["dt_txt"].split(' ')
            output += '            ' + zerodate + '\n'
            for i in range(data["cnt"]):
                wea = emoji["Skeleton"]
                dat, tim = data["list"][i]["dt_txt"].split(' ')
                tem = data["list"][i]["main"]["temp"]  #
                hum = data["list"][i]["main"]["humidity"]  #
                clo = data["list"][i]["clouds"]["all"]  #
                pop = data["list"][i]["pop"] * 100  #
                win = data["list"][i]["wind"]["speed"]  #
                if data["list"][i]["weather"][0]["main"] in emoji:  # /emoji_with_text
                    wea = emoji[data["list"][i]["weather"][0]["main"]]
                if dat > zerodate:
                    output += f"\n            {dat}\n"
                    zerodate = dat
                out = f"{tim[:2]}|{wea}|" \
                      f"{tem:5.1f}°C|\U0001F4A7{hum}|\U00002601{clo:3}|\U0001F52E{pop:3}|\U0001F32C{win:5.1f}ms\n"
                output += out

            await bot.send_message(chat_id=idd, text=f"{output}")

            await bot.send_message(chat_id=admin_id,text=f"User:{my_data[str(idd)]['name']}\n Погода на {int(num / 8)} суток, в городе {html.escape(city)}")  # Экранирование города
            logs.write(f"[{datetime.datetime.now()}] User:{my_data[str(idd)]['name']} Погода на {int(num / 8)} суток, в городе {html.escape(city)}\n")
    except Exception as e:
        error_message = f"{emoji['Skeleton']}Что-то пошло не так{emoji['Skeleton']}\nОшибка: {html.escape(str(e))}"  # Экранирование ошибки
        await bot.send_message(chat_id=idd, text=error_message)
        admin_error_message = f"Somthing went wrong! Ошибка: {html.escape(str(e))} in get_weather.weather\n User:{html.escape(my_data[str(idd)]['name'])}"  # Экранирование имени пользователя
        await bot.send_message(chat_id=admin_id, text=admin_error_message)
        logs.write(f"[{datetime.datetime.now()}] -('v')- -('v')- -('v')- Somthing went wrong! {html.escape(str(e))} in get_weather.weather User:{html.escape(my_data[str(idd)]['name'])}\n")