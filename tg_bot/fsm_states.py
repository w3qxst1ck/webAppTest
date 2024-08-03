from aiogram.fsm.state import StatesGroup, State


class CreateMessageFSM(StatesGroup):
    text = State()


class GetMessageByIDFSM(StatesGroup):
    id = State()