from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')
quiz_button = KeyboardButton('/quiz')
reg_button = KeyboardButton('/reg')
meme_button = KeyboardButton('/meme')

share_location = KeyboardButton ('location', request_location=True)
share_contact = KeyboardButton ('contact_location', request_contact=True)


start_markup.add(start_button, info_button, quiz_button, share_location, share_contact, reg_button, meme_button)

cancel_button = KeyboardButton('CANCEL')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(cancel_button)

gender_m = KeyboardButton("Мужчина")
gender_f = KeyboardButton("Женщина")
gender_u = KeyboardButton("Незнаю")

d_backend=KeyboardButton("Backend")
d_android=KeyboardButton("Android")
d_uxui=KeyboardButton("UX/UI")
d_apple=KeyboardButton("Apple")
d_frontend=KeyboardButton("Frontend")

direct_markup = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(d_backend, d_android, d_uxui, d_apple, d_frontend)

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(gender_m, gender_f, gender_u, cancel_button)


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('НЕТ'))