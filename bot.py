from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from token_ import tok
from func_for_bot import *
from morse_dict import *

bot = Bot(token=tok)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def answer_start(message: types.Message):
    await message.answer('Введите слово или символы азбуки морзе и я конвертирую их.')


# на русском
@dp.message_handler()
async def answer(message: types.Message):
    if message.text.lower()[0] in rus_to_m:
        try:
            await message.answer(rus_l_to_morse(message.text))
        except:
            await message.answer('Вы ввели неверные символы')
    else:
        try:
            await message.answer(morse_to_rus_l(message.text))
        except:
            await message.answer('Вы ввели неверные символы')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
