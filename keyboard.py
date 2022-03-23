from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_period_keyboard():
    start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('24 часа')
    button_2 = KeyboardButton('3 дня')
    button_3 = KeyboardButton('Неделя')
    button_4 = KeyboardButton('За все время')
    start.add(button_1, button_2, button_3, button_4)
    return start


def get_agreement_keyboard():
    sport_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_1 = KeyboardButton('Да')
    button_2 = KeyboardButton('Нет')
    sport_keyboard.add(button_1, button_2)
    return sport_keyboard


def get_experience_keyboard():
    films_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_1 = KeyboardButton('Без опыта')
    button_2 = KeyboardButton('От 1 года')
    button_3 = KeyboardButton('От 3 лет')
    button_4 = KeyboardButton('От 6 лет')
    films_keyboard.add(button_1, button_2, button_3, button_4)
    return films_keyboard
