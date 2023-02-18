from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)


help_btn = KeyboardButton('/help')
jokes_about_programmers_btn = KeyboardButton('/jokes_about_programmers')
jokes_about_shtirlitz_btn = KeyboardButton('/jokes_about_shtirlitz')
jokes_about_vovochka_btn = KeyboardButton('/jokes_about_vovochka')
odesa_humor_btn = KeyboardButton('/odesa_humor')
jokes_about_clowns_btn = KeyboardButton('/jokes_about_clowns')
# donate_btn = KeyboardButton('/donate')


keyboard.add(help_btn)
keyboard.add(jokes_about_programmers_btn).insert(jokes_about_shtirlitz_btn)
keyboard.add(jokes_about_vovochka_btn).insert(odesa_humor_btn)
keyboard.add(jokes_about_clowns_btn)
# keyboard.add(donate_btn)
