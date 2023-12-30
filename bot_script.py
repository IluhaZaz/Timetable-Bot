from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from parse import parse

BOT_TOKEN = ''

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_help_command(message: Message):
    await message.answer('Хей, я твое карманное рассписание на сегодня!\nОтправь команду today, чтобы узнать какие сегодня пары')


async def process_today_command(message: Message):
    await message.answer(parse("Социологический факультет", "5401-390301D"))


async def process_no_command(message: Message):
    await message.reply("Не знаю такой команды...")


# Регистрируем хэндлеры
dp.message.register(process_start_help_command, Command(commands=['start', 'help']))
dp.message.register(process_today_command, Command(commands='today'))
dp.message.register(process_no_command)

if __name__ == '__main__':
    dp.run_polling(bot)