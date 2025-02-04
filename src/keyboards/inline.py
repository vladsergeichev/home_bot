from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def keyboard_main():
    kb_list = [
        [KeyboardButton(text="Заявка на въезд")],
        [KeyboardButton(text="Информация")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)


def keyboard_type_entry():
    kb_list = [
        [KeyboardButton(text="Доставка")],
        [KeyboardButton(text="Гость")],
        [KeyboardButton(text="Постоянный пропуск")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
