from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINS
from keyboards import client_kb
from database.bot_db import sql_command_insert
import uuid


# print(uuid.uuid1())
# gen_id=uuid.uuid1()
class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    direction = State()
    grup = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message):
    # if message.from_user.id not in ADMINS:
    #     await message.answer('Ты не мой босс')
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer("Как звать?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в личке!")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Скока лет?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа")
    elif int(message.text) < 5 or int(message.text) > 50:
        await message.answer("Возростное ограничение!")
    else:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Какого пола?", reply_markup=client_kb.gender_markup)


async def load_gender(message: types.Message, state: FSMContext):
    if message.text not in ["Мужчина", "Женщина", "Незнаю"]:
        await message.answer("Выбери из списка!")
    else:
        async with state.proxy() as data:
            data['gender'] = message.text
        await FSMAdmin.next()
        await message.answer("Какое направление??", reply_markup=client_kb.direct_markup)


async def load_direct(message: types.Message, state: FSMContext):
    if message.text not in ["Backend", "Android", "UX/UI", "Apple", "Frontend"]:
        await  message.answer("Выберите из списка!!")
    else:
        async with state.proxy() as data:
            data['direction'] = message.text
        await FSMAdmin.next()
        await message.answer("Группа?"
                         "Пример:241", reply_markup=client_kb.cancel_markup)


async def load_grup(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("ЧИСЛАААА!!!!!")
    else:
        async with state.proxy() as data:
            data['grup']=message.text
        await FSMAdmin.next()
        await message.answer("Скинь фотку?)")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await message.answer_photo(data['photo'],
                                   caption=f"{data['name']} {data['age']} {data['gender']} "
                                           f"{data['direction']} {data['grup']}\n{data['username']}")
    await FSMAdmin.next()
    await message.answer("Все верно?", reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Ты зареган")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Ну и пошел ты!")
    else:
        await message.answer('НИПОНЯЛ!?')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Ну и пошел ты!")


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_direct, state=FSMAdmin.direction)
    dp.register_message_handler(load_grup, state=FSMAdmin.grup)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSMAdmin.submit)