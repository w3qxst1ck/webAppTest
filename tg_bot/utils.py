from aiogram import types
from config import PAGE_SIZE

VALID_CHARS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]


def is_valid(message_id: str) -> bool:
    """Check valid message ID"""
    if len(message_id) != 24:
        return False

    for char in message_id:
        if char not in VALID_CHARS:
            return False
    return True


def get_pagination_params(callback: types.CallbackQuery = None, first_page: bool = False) -> (dict, int):
    """Get params for pagination in get request"""
    if first_page:
        params = {"page": 1, "size": PAGE_SIZE}
        idx = 1
        return params, idx

    move = callback.data.split("_")[1]
    current_page = int(callback.data.split("_")[2])
    num_pages = int(callback.data.split("_")[3])

    if move == "prev":
        if current_page == 1:
            next_page = num_pages
            idx = PAGE_SIZE * num_pages + 1 - PAGE_SIZE
        else:
            next_page = current_page - 1
            idx = PAGE_SIZE * next_page + 1 - PAGE_SIZE
    else:
        if current_page == num_pages:
            next_page = 1
            idx = 1
        else:
            next_page = current_page + 1
            idx = PAGE_SIZE * current_page + 1

    params = {
        "page": next_page,
        "size": PAGE_SIZE
    }

    return params, idx