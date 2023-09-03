from keyboards import more
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from main import get_first_news
from aiogram.types import CallbackQuery

TOKEN = 'TOKEN'

bot = Bot(token=TOKEN, parse_mode='HTML')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           'Привет путник, Нажми на кнопку ниже для нового анекдота',
                           reply_markup=more())


async def send_anekdot(chat_id):
    await bot.send_message(chat_id,
                           f'Рандомный анекдот🍀: <span class="tg-spoiler"> \n \n {get_first_news()} </span>',
                           reply_markup=more())


@dp.callback_query_handler(lambda c: c.data == 'more')
async def anekdot(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Загружаем новый анекдот...")
    await send_anekdot(callback_query.from_user.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)

# Я ЛОХ
executor.start_polling(dp)
