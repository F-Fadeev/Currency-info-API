# FastAPI Bitcoin Dashboard

Этот проект - простая панель инструментов, которая отображает текущие курсы обмена Bitcoin с использованием FastAPI и Celery.

## Установка

1. Клонируйте этот репозиторий
2. Установите менеджер пакетов Poetry, следуя официальной документации: `https://python-poetry.org/docs/#installation`
3. Установите зависимости: `poetry install`
4. Запустите Redis и MongoDB с помощью docker-compose: `docker-compose up`
5. Запустите Celery: `celery -A source.tasks.task:celery_app worker --loglevel=INFO`
6. Запустите Flower: `celery -A source.tasks.task:celery_app flower`
7. Запустите приложение: `python main.py`

## Использование

1. Откройте `http://localhost:8000/docs` в браузере, чтобы получить доступ к FastAPI Swagger UI.
2. Нажмите на тег `Currency`, чтобы раскрыть доступные конечные точки.
3. Нажмите на конечную точку `/`, чтобы просмотреть все доступные данные из MongoDB.
4. Чтобы обновить данные, перейдите на страницу `http://localhost:8000/report/dashboard`.

## Конфигурация

Конфигурация для этого проекта хранится в файле `.env`, расположенном в корневом каталоге. Следующие переменные обязательны:

- `DB_USER`: имя пользователя для базы данных MongoDB
- `DB_PASS`: пароль для базы данных MongoDB
- `DB_HOST`: хост для базы данных MongoDB
- `DB_PORT`: порт для базы данных MongoDB
- `DB_NAME`: имя базы данных MongoDB

## Используемые технологии

- [FastAPI](https://fastapi.tiangolo.com/) для создания API
- [Celery](https://docs.celeryproject.org/en/stable/index.html) для планирования задач
- [MongoDB](https://www.mongodb.com/) для хранения данных
- [Redis](https://redis.io/) для сообщений Celery-брокера
- [Docker](https://www.docker.com/) для контейнеризации

## Лицензия

Этот проект распространяется по лицензии MIT - см. файл `LICENSE` для получения дополнительной информации.
