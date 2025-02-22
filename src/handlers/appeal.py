from aiogram.types import Message
from aiogram import Bot, Dispatcher, F, Router
from aiogram.fsm.context import FSMContext

from keyboards.inline import keyboard_type_entry
from utils.stateform import AppealsForm

router = Router()


@router.message(F.text == "Заявка на въезд")
async def appeal_start(message: Message, state: FSMContext):
    await message.answer("Укажите номер автомобиля с кодом региона\nНапример, А123БВ99")
    await state.set_state(AppealsForm.GET_NUMBER)


@router.message(AppealsForm.GET_NUMBER)
async def number(message: Message, state: FSMContext):
    await message.answer("Укажите тип пропуска", reply_markup=keyboard_type_entry())
    await state.update_data(number=message.text)
    await state.set_state(AppealsForm.TYPE_ENTRY)


@router.message(AppealsForm.TYPE_ENTRY)
async def type_entry(message: Message, state: FSMContext):
    context_data = await state.get_data()
    context_data['type'] = message.text
    await message.answer(f"Заявка отправлена!\n{context_data['number']}({context_data['type']})")
    await state.clear()
