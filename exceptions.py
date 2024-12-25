class EnvironmentError(Exception):
    """Исключение для отсутствия обязательных переменных окружения."""

    pass


class NotOkHTTPCodeError(Exception):
    """Исключение для неожидаемого статус-кода в ответе API."""

    pass


class NotKeyError(Exception):
    """Исключение при отсутствии запрашиваемого ключа."""

    pass
