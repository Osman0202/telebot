from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')
quiz_button = KeyboardButton('/quiz')

share_location = KeyboardButton ('location', request_location=True)
share_contact = KeyboardButton ('contact_location', request_contact=True)


start_markup.add(start_button, info_button, quiz_button, share_location, share_contact)