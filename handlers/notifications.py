import  aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio

async def get_chat_id(message:types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("OK")



async def go_to_scholl():
    await bot.send_message(chat_id=chat_id, text="Иди на учебу!")


async def scheduler():
    aioschedule.every().tuesday.at("17:00").do(go_to_scholl)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp:Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'Напомни' in word.text)