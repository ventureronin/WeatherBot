import json
import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, ContentTypeFilter
from aiogram.types import ReplyKeyboardRemove
# <em>text<b> some </b> shit </em>

from loader import CurrentState, dp, bot, types, admin_id, keyboards
from utils.get_weather import single_weather


@dp.message_handler(commands=["start"], state="*")
async def start_command(msg: types.Message) -> None:
    await CurrentState.city.set()
    with open("opt.json", "r") as f:
        data = json.load(f)
    f.close()
    user_id = msg.from_user.id
    if str(user_id) not in data:
        if msg.from_user.username:
            username = msg.from_user.username
        elif msg.from_user.first_name:
            username = msg.from_user.first_name
        else:
            username = msg.from_user.last_name

        with open('opt.json', 'w') as f:
            data[user_id] = {'id': user_id, 'name': username, 'alarm_mode': 1, 'alarm_on': 0}
            json.dump(data, f, indent=4, ensure_ascii=False)
        f.close()
        await bot.send_message(chat_id=admin_id,
                               text=f"У нас новый юзер: {msg.from_user.username}, {msg.from_user.first_name} "
                                    f"{msg.from_user.last_name} \n {msg.from_user.id}")
    await bot.send_message(chat_id=msg.from_user.id,
                           text=f"Привет, {msg.from_user.username}! Если тебе нужны объяснения что тут происходит"
                                f" - жми команду /help (выпадающее меню слева вверху от клавиатуры, или прям в этом"
                                f" сообщении)",
                           parse_mode="HTML",
                           reply_markup=keyboards.main_kb)
    await msg.delete()


@dp.message_handler(commands=["help"], state="*")
async def help_command(message: types.Message) -> None:
    help_text1 = '<em>Бот может выдавать погоду на <b>текущий момент</b> (+восход/заход солнца) или на <b>выбранное количество суток </b>, с промежутком в три часа (т.е. в полночь, в 3, 6, 9 и тд).\nСамое далёкое будущее, доступное боту - 5 суток (120 часов).</em>'
    help_text2 = '<b>Обозначения:</b>\n<em>Погодные(слева от градусов):</em>\n\U00002600 - ясно\n\U00002601 - облачно\n\U00002614 - дождь\n\U00002614 - морось\n\U000026A1 - гроза\n\U0001F328 - снег\n\U0001F32B - туман\n<em>Остальные:</em>\n\U0001F4A7 - влажность, %\n\U00002601 - облачность, %\n\U0001F52E -вероятность осадков, %\n\U0001F32C - скорость ветра, метр/сек'
    help_text3 = '<b>Команды бота:</b>\n<em>/start - Запустить/перезапустить бота\n/help - Вывести эту справку\n/settings - Настройки(пока не работает)</em>\nЭти команды есть в "быстром доступе" слева от поля ввода в кнопке"Меню"\n\nБот "слушает" названия городов в чате <b>ТОЛЬКО</b> после ввода команды <em>/start</em>.\nИсключение: города,указанные в клавиатуре главного меню(Полтава, Зеньков, Гданьск). Они будут услышаны всегда и доступны по нажатию кнопки. Клавиатура появляетсяпосле любого сообщения в чат(если она "закрылась" справа от поля ввода есть квадратный значок с 4мя точками)\n\nP.S.Если черепок \U00002620 мелькает слишком часто и причины не ясны - отличный повод написать админу \U0001F643 @Rishard_S'
    await bot.send_message(chat_id=message.from_user.id,
                           text=help_text1,
                           parse_mode="HTML")
    await bot.send_message(chat_id=message.from_user.id,
                           text=help_text2,
                           parse_mode="HTML")
    await bot.send_message(chat_id=message.from_user.id,
                           text=help_text3,
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=["settings"], state='*')
async def settings_command(msg: types.Message) -> None:
    with open('opt.json', 'r') as f:
        data = json.load(f)
    f.close()
    await bot.send_message(chat_id=msg.from_user.id,
                           text=f"Настройки.\n"
                                f"Геолокация:\n"
                                f"Автоматическая рассылка погоды(): {data[str(msg.from_user.id)]['alarm_mode']}\n"
                                f"0-выкл, 1-2 режимы",
                           reply_markup=keyboards.settings_kb,
                           parse_mode="HTML")
    await bot.send_message(chat_id=msg.from_user.id,
                           text="пока работает только кнопка выхода из настроек =)")
    await msg.delete()
    await CurrentState.settings.set()


# @dp.message_handler(commands=["выключить уведомления"], state="settings")
# async def settings_exit(msg: types.Message) -> None:
#     await CurrentState.city.set()
#     await msg.delete()
#     with open('opt.json', 'w') as f:
#         data = json.load(f)
#     f.close()
#     print('we are here')
#     if data[str(msg.from_user.id)]['notify_on']:
#         data[str(msg.from_user.id)]['notify_on'] = 0
#         await bot.send_message(chat_id=msg.from_user.id,
#                                text=f"Уведомления выключены")
#     else:
#         data[str(msg.from_user.id)]['notify_on'] = 1
#         await bot.send_message(chat_id=msg.from_user.id,
#                                text=f"Уведомления включены")
#     json.dump(data)
#
#
# @dp.message_handler(content_types=types.ContentType.LOCATION, state="settings")
# async def settings_exit(msg: types.Message) -> None:
#     pass


@dp.message_handler(Text(equals="Выйти из настроек"), state=CurrentState.settings)
async def settings_exit(msg: types.Message) -> None:
    await bot.send_message(chat_id=msg.from_user.id, text=f"Выход из настроек", reply_markup=keyboards.main_kb)
    await CurrentState.city.set()
    await msg.delete()


# @dp.message_handler(commands=["Вкл/выкл рассылку погоды"], state="settings")
# async def settings_exit(msg: types.Message) -> None:
#     pass


@dp.message_handler(Text(equals="Полтава"))
@dp.message_handler(Text(equals="Зеньков"))
@dp.message_handler(Text(equals="Pruszcz gdański"))
@dp.message_handler(state=CurrentState.city)
async def get_city(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['city'] = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Город:{data['city']}\nна сколько суток погода?",
                           parse_mode="HTML",
                           reply_markup=keyboards.ikb)
    await CurrentState.choice_day.set()


@dp.callback_query_handler(text_startswith='day_', state=CurrentState.choice_day)
async def ikb_handler(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['choice_day'] = callback_query.data.split("_")[1]
    if data['choice_day'] == '1':
        await single_weather(data['city'], 8, callback_query.from_user.id)
    elif data['choice_day'] == '2':
        await single_weather(data['city'], 16, callback_query.from_user.id)
    elif data['choice_day'] == '3':
        await single_weather(data['city'], 24, callback_query.from_user.id)
    elif data['choice_day'] == '4':
        await single_weather(data['city'], 32, callback_query.from_user.id)
    elif data['choice_day'] == '5':
        await single_weather(data['city'], 40, callback_query.from_user.id)
    elif data['choice_day'] == 'now':
        await single_weather(data['city'], 0, callback_query.from_user.id)
    else:
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"\U00002620Что-то пошло не так",
                               parse_mode="HTML")
        await bot.send_message(chat_id=admin_id,
                               text=f"something went wrong(ikb_handler)\nUser:{callback_query.from_user.id}")
    await CurrentState.city.set()
    await callback_query.answer()


@dp.message_handler()
async def echo_cmd(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text, reply_markup=keyboards.main_kb)
