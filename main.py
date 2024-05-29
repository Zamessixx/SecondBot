from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from datetime import datetime


TOKEN_API = '7309138691:AAHQ2yjXagL1C5LUznwH14Sh-4A7I5mXM08'
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


keyboard1 = InlineKeyboardMarkup(row_with=1)
button1 = InlineKeyboardButton('Переключение на следующую клавиатуру', callback_data= 'go_to_2')
button2 = InlineKeyboardButton('Отправь случайное число', callback_data= 'send_random_number')
keyboard1.add(button1, button2)

keyboard2 = InlineKeyboardMarkup(row_width=1)
button3 = InlineKeyboardButton('Переключение на предыдущую клавиатуру', callback_data= 'go_to_1')
button4 = InlineKeyboardButton('Текущее время', callback_data= 'send_datetime')
keyboard2.add(button3, button4)

@dp.message_handler(commands= 'start')
async def start(message: types.message):
    await message.reply('Нажми на кнопку 1 чтобы перейти на 2 клавиатуру', reply_markup= keyboard1)


@dp.callback_query_handler(lambda c: c.data == 'send_random_number')
async def random_number(callback_query: types.callback_query):
    random_num = random.randint(1, 1000)
    await callback_query.message.answer(f'Случайное число: {random_num}')

@dp.callback_query_handler(lambda c: c.data == 'send_datetime')
async def send_datetime(callback_query: types.callback_query):
    curent_time = datetime.now().strftime("%H:%M:%S")
    await callback_query.message.answer(f'Текущее время: {curent_time}')

@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.callback_query):
    await callback_query.message.edit_text('Ты перешёл на 1 клавиатуру, нажми на кнопку, чтобы вернуться на 2', reply_markup= keyboard1)

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.callback_query):
    await callback_query.message.edit_text('Ты перешёл на 1 клавиатуру, нажми на кнопку, чтобы вернуться на 2', reply_markup= keyboard2)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)