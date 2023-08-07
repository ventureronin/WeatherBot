from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

ib1 = InlineKeyboardButton("1 сутки", callback_data="day_1")
ib2 = InlineKeyboardButton("2 суток", callback_data="day_2")
ib3 = InlineKeyboardButton("3 суток", callback_data="day_3")
ib4 = InlineKeyboardButton("4 суток", callback_data="day_4")
ib5 = InlineKeyboardButton("5 суток", callback_data="day_5")
ib6 = InlineKeyboardButton("Cейчас", callback_data="day_now")

ikb = InlineKeyboardMarkup(row_width=2)\
    .add(ib1).insert(ib2).insert(ib3).insert(ib4).insert(ib5).add(ib6)

b1 = KeyboardButton("Полтава")
b2 = KeyboardButton("Зеньков")
b3 = KeyboardButton("Pruszcz gdański")
main_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)\
    .add(b1, b2, b3)

sb0 = KeyboardButton("Выйти из настроек")
sb1 = KeyboardButton("Выкл рассылку")
sb2 = KeyboardButton("отправить боту свою геолокацию", request_location=True)
sb3 = KeyboardButton("Вкл 1 режим")
sb4 = KeyboardButton("Вкл 2 режим")
settings_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)\
    .add(sb2).add(sb1).insert(sb3).insert(sb4).add(sb0)
