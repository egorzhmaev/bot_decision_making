from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
from random import shuffle

BOT_TOKEN = ''

ANSWERS = [
    'Думаю, да!',
    'Не стоит.',
    'Я сомневаюсь в этом',
    'Вероятно, да',
    'Бесспорно',
    'Не могу сказать',
    'Не сейчас',
    'Спросите позже',
    'Решительно, да!'
]

router: Router = Router()


@router.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Привет! Я бот для принятия решений. Просто спроси меня о чём угодно.')


@router.message(F.text.endswith('?'))
async def answer_to_questions(message: Message):
    shuffle(ANSWERS)
    await message.answer(ANSWERS[0])


@router.message()
async def answer(message: Message):
    await message.answer('Не понимаю о чем ты... Просто задай вопрос.')


async def start():
    bot: Bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

    dp: Dispatcher = Dispatcher()
    dp.include_router(router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
