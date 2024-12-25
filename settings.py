import os

from dotenv import load_dotenv

load_dotenv()

"""Токен доступа к данным Практикум.Домашка."""
PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')

"""Токен доступа к Telegram боту."""
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

"""ID чата в Telegram для отправки сообщений."""
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

"""Период ожидания между запросами."""
RETRY_PERIOD = 600

"""Метод получения данных из сервиса Практикум.Домашка"""
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'

"""Хедеры для отправки запроса к методу сервиса Практикум.Домашка"""
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}

"""Список сообщений для статусов."""
HOMEWORK_VERDICTS = {
    'approved': 'Работа проверена: ревьюеру всё понравилось. Ура!',
    'reviewing': 'Работа взята на проверку ревьюером.',
    'rejected': 'Работа проверена: у ревьюера есть замечания.'
}
