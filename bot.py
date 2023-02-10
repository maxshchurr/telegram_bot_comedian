import time
import logging

from aiogram import Bot, Dispatcher, executor, types
from settings import BOT_TOKEN


HELP_COMMAND = """
Will be soon
"""

bot = Bot(token=BOT_TOKEN)
disp = Dispatcher(bot=bot)


@disp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    logging.info(f'{user_id} {user_full_name} {time.asctime()}')

    await message.reply(f'Hi, {user_full_name}')


@disp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@disp.message_handler(commands=['description'])
async def description_handler(message: types.Message):
    await message.answer('This is a comedian bot.')


@disp.message_handler(commands=['jokes_about_programmers'])
async def programmists_jokes_handler(message: types.Message):
    igor_link_programmer_sticker = 'CAACAgIAAxkBAAEHqrlj5ghUIFoSm5nkAehN41frtW5EcQACJgAD1b4hJ0mtVouBBU_ULgQ'
    await bot.send_sticker(message.from_user.id, sticker=igor_link_programmer_sticker)
    await message.answer("You've selected jokes about programmers, great choice!")

if __name__ == '__main__':
    executor.start_polling(disp)


