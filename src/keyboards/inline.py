from typing import List

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# def list_kb_build(queues: List[Queue]):
#     keyboard_builder = InlineKeyboardBuilder()
#     for i, queue in enumerate(queues):
#         keyboard_builder.button(
#             text=queue.name,
#             callback_data=f"items_{i}"
#         )
#     keyboard_builder.button(
#         text='+ Добавить',
#         callback_data='added'
#     )
#     keyboard_builder.adjust(2)
#     return keyboard_builder.as_markup()

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
