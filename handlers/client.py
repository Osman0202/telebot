from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from keyboards.client_kb import start_markup


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салам хозяин {message.from_user.first_name}",
                           reply_markup=start_markup)

async def info_hendler(message:types.Message):
    await message.reply("САМ РАЗБИРАЙСЯ!")

async def meme_1(message: types.Message):
    photo = open("media/mem-kot-tom-10-1600x1532.jpg", "rb")
    await bot.send_photo(message.from_user.id, photo=photo)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Язык программирования?"
    answers = [
        'Python',
        'Английский',
        'Русский',
        ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_hendler, commands=['info'])
    dp.register_message_handler(meme_1, commands=['meme'])