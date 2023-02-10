from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


# По умолчанию False - скрывает клавиатуру после нажатия на кнопку
keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
keyboard.add(KeyboardButton('/jokes_about_programmers'))
keyboard.add(KeyboardButton('/jokes_about_shtirliz'))