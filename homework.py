
import time
import logging
from http import HTTPStatus as status

import requests
import telegram

from exceptions import (
    EnvironmentError,
    NotOkHTTPCodeError,
    NotKeyError
)
from settings import (
    PRACTICUM_TOKEN,
    TELEGRAM_TOKEN,
    TELEGRAM_CHAT_ID,
    RETRY_PERIOD,
    ENDPOINT,
    HEADERS,
    HOMEWORK_VERDICTS
)


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
)


def check_tokens():
    """Проверка доступности переменных окружения."""
    required_tokens = [PRACTICUM_TOKEN, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID]
    return all(required_tokens)


def get_api_answer(timestamp):
    """Запрос адресу API."""
    pass


def check_response():
    """Проверка ответа API."""
    pass


def parse_status():
    """Парсинг ответа API."""
    pass


def send_message():
    """Отправка сообщения в Telegram."""
    pass
