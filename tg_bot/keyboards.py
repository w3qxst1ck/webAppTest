from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def cancel_keyboard() -> InlineKeyboardBuilder:
    """Keyboard with cancel button"""
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Отмена", callback_data=f"cancel"))
    return keyboard


def pagination_keyboard(current_page: int, num_pages: int) -> InlineKeyboardBuilder:
    """Keyboard for message pagination"""
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="<", callback_data=f"pagination_prev_{current_page}_{num_pages}"))
    keyboard.row(InlineKeyboardButton(text=">", callback_data=f"pagination_next_{current_page}_{num_pages}"))
    keyboard.adjust(2)
    return keyboard