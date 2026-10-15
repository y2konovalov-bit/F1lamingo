from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def gender_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton("Мужской👨", callback_data="gender_male"),
        InlineKeyboardButton("Женский👩", callback_data="gender_female"),
    ]
    keyboard.add(*buttons)
    return keyboard

def name_keyboard(message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(message.from_user.first_name, callback_data="send_name")
    keyboard.add(button)
    return keyboard
