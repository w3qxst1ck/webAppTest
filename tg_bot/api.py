import requests

from config import DOMEN


class API:
    def __init__(self, domen: str):
        self.domen = domen
        self.headers = {
            "Content-Type": "application/json"
        }

    def _get_request(self, url: str, params) -> str | dict:
        response = requests.get(self.domen + url, headers=self.headers, params=params)
        if response.status_code != 200:
            return self._handle_error(response)
        return response.json()

    def _post_request(self, url: str, body: dict) -> dict:
        response = requests.post(self.domen + url, json=body, headers=self.headers)
        if response.status_code != 200:
            return self._handle_error(response)
        return response.json()

    def _handle_error(self, response: requests.Response) -> dict:
        code = response.status_code
        message = {
            "error": "Ошибка на сервере. Повторите попытку позже.",
            "code": code
        }
        return message

    def create_message(self, text: str, user: str) -> dict:
        """Create message"""
        body = {
            "text": text,
            "user": user
        }
        response = self._post_request("/messages", body)
        return response

    def get_messages(self, params: dict) -> dict:
        """Get all messages"""
        response = self._get_request("/messages/", params)
        return response

    def get_message_by_id(self, message_id: str) -> dict:
        """Get message by ID"""
        response = self._get_request(f"/messages/{message_id}", None)
        return response


message_api = API(DOMEN)