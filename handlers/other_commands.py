import re

from aiogram import types
from aiogram.dispatcher.filters import Command, CommandStart

from loader import dp
from utils.throttlig import rate_limit


@rate_limit(limit=4)
@dp.message_handler(Command('help'))
async def command_help(message: types.Message):
    text = f'❔<b>Как пользоваться ботом</b>❔\n\n' \
           f'Всё очень просто, напиши боту название книги и бот выдаст тебе все подходящие книги\n' \
           f'Либо ты можешь воспользоваться более точным поиском, с помощью следующих комманд: 👇\n\n' \
           f'/start - стартовая команда, чтобы впервые запустить бота\n' \
           f'/author <i>имя автора</i> - поиск только по авторам\n' \
           f'/series <i>название серии</i> - поиск только по названию серии\n' \
           f'/help - вызов справки, если ты забыл как пользоваться ботом🙃\n\n' \
           f'Например:\n' \
           f'/author Джоан Роулинг\n' \
           f'/series песнь льда и пламени\n\n' \
           f'<b>P.S.</b>\n' \
           f'Книги доступны во всех форматах для скачивания\n' \
           f'По вопросам, недочетам и предложениям - писать: @soldatov_ss'
    await message.answer(text)


@rate_limit(limit=4)
@dp.message_handler(CommandStart())
async def command_start(message: types.Message):
    text = f'Привет, {message.from_user.full_name}! \nЯ помогу найти тебе любую книгу!😇\n' \
           f'Чтобы начать, пришли мне название книги 📖\n' \
           f'Я также могу производить поиск по ФИО автора или названию книжной серии ☺\n' \
           f'Ты можешь узнать больше обо мне здесь 👉 /help\n'
    await message.answer(text)


@dp.message_handler(regexp=re.compile(r'^/.+'))
async def other_command(message: types.Message):
    # Проверям на битую любую битую ссылку
    text = f'У меня нет такой комманды 😨\n' \
           f'Попробуй еще раз\n' \
           f'Либо можешь ознакомится со справкой 👉 /help'
    return await message.answer(text)
