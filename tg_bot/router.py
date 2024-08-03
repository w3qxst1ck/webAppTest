from aiogram import Router, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from api import message_api as api
from messages import get_all_messages_answer, get_message_answer
from fsm_states import CreateMessageFSM, GetMessageByIDFSM
from keyboards import cancel_keyboard, pagination_keyboard
from utils import is_valid, get_pagination_params

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message) -> None:
    """Start message"""
    await message.answer("Hello!")


@router.message(Command("help"))
async def start_handler(message: types.Message) -> None:
    """Help message"""
    await message.answer("Бот сделан для тестового задания. Хранит, записывает и выводит сообщения")


@router.message(Command("messages"))
async def get_messages(message: types.Message) -> None:
    """Print all messages"""
    params, idx = get_pagination_params(first_page=True)

    response = api.get_messages(params)

    if response.get("error") is not None:
        await message.answer(response["error"])
    else:
        mes = get_all_messages_answer(response, idx)
        current_page = 1
        num_pages = response["pages"]
        await message.answer(mes, reply_markup=pagination_keyboard(current_page, num_pages).as_markup())


@router.callback_query(lambda callback: callback.data.split("_")[0] == "pagination")
async def get_messages_pagination(callback: types.CallbackQuery) -> None:
    """Pagintion print messages"""
    params, idx = get_pagination_params(callback=callback, first_page=False)

    response = api.get_messages(params)

    if response.get("error") is not None:
        await callback.message.answer(response["error"])
    else:
        mes = get_all_messages_answer(response, idx)
        num_pages = response["pages"]
        await callback.message.edit_text(mes, reply_markup=pagination_keyboard(params["page"], num_pages).as_markup())


@router.message(Command("create"))
async def create_messages(message: types.Message, state: FSMContext) -> None:
    """Create message, start FSM"""
    await state.set_state(CreateMessageFSM.text)
    await message.answer("Отправьте текст сообщения", reply_markup=cancel_keyboard().as_markup())


@router.message(CreateMessageFSM.text)
async def create_messages(message: types.Message, state: FSMContext) -> None:
    """End FSM for creating message"""
    await state.clear()
    text = message.text
    user = str(message.from_user.id)

    response = api.create_message(text, user)
    if response.get("error") is not None:
        await message.answer(response["error"])
    else:
        await message.answer(f"Сообщение создано с ID <b>{response['id']}</b>")


@router.message(Command("find"))
async def get_message_by_id(message: types.Message, state: FSMContext) -> None:
    """Get message by ID, start FSM"""
    await state.set_state(GetMessageByIDFSM.id)
    await message.answer("Отправьте ID сообщения", reply_markup=cancel_keyboard().as_markup())


@router.message(GetMessageByIDFSM.id)
async def create_messages(message: types.Message, state: FSMContext) -> None:
    """End FSM for getting message by ID"""
    message_id = message.text
    if not is_valid(message_id):
        await message.answer("Неверный формат ID сообщения", reply_markup=cancel_keyboard().as_markup())
    else:
        await state.clear()
        response = api.get_message_by_id(message_id)
        if response is None or response.get("error") is not None:
            await message.answer("Сообщение не найдено")
        else:
            mes = get_message_answer(response)
            await message.answer(mes)


@router.callback_query(lambda callback: callback.data == "cancel", StateFilter("*"))
async def cancel_handler(callback: types.CallbackQuery, state: FSMContext):
    """Cancel FSM and delete last message"""
    await state.clear()
    await callback.message.answer("Действие отменено")
    try:
        await callback.message.delete()
    except TelegramBadRequest:
        pass
