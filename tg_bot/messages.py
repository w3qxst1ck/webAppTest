def get_all_messages_answer(response: dict, idx: int) -> str:
    """Create all messages answer"""
    message = f"Всего сообщений <b>{response['total']}</b> | Страница <b>{response['page']}/{response['pages']}</b> | Сообщений на странице <b>{response['size']}</b>\n\n"

    if response["items"]:
        for idx, item in enumerate(response['items'], start=idx):
            message += f'{idx}. ID: <b>{item["id"]}</b> From user: {item["user"]} Text: {item["text"]} Time: {item["date"]}\n\n'

    return message.strip()


def get_message_answer(response: dict) -> str:
    """Create one message answer"""
    message = f"ID: <b>{response['id']}</b> From user: {response['user']} Text: {response['text']} Time: {response['date']}"
    return message