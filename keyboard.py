from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)


help_btn = KeyboardButton('/help')
jokes_about_programmers_btn = KeyboardButton('/jokes_about_programmers')
jokes_about_shtirlitz_btn = KeyboardButton('/jokes_about_shtirlitz')
jokes_about_vovochka_btn = KeyboardButton('/jokes_about_vovochka')
odesa_humor = KeyboardButton('/odesa_humor')
donate_btn = KeyboardButton('/donate')


keyboard.add(help_btn)
keyboard.add(jokes_about_programmers_btn).insert(jokes_about_shtirlitz_btn)
keyboard.add(jokes_about_vovochka_btn).insert(odesa_humor)
keyboard.add(donate_btn)
