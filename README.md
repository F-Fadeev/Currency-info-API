# FastAPI Bitcoin Dashboard

This project is a simple dashboard that displays current Bitcoin exchange rates using FastAPI and Celery.

## Installation

1. Clone this repository
2. Install Poetry package manager following the official documentation: `https://python-poetry.org/docs/#installation`
3. Install dependencies: `poetry install`
4. Run Redis and MongoDB with docker-compose: `docker-compose up`
5. Run Celery: `celery -A source.tasks.task:celery_app worker --loglevel=INFO`
6. Run Flower: `celery -A source.tasks.task:celery_app flower`
7. Start the application: `python main.py`
## Usage

1. Open `http://localhost:8000/docs` in your browser to access the FastAPI Swagger UI.
2. Click on the `Currency` tag to expand the available endpoints.
3. Click on the `/` endpoint to view all available data in the dashboard.
4. To update the data, go to `http://localhost:8000/report/dashboard`.

## Configuration

The configuration for this project is stored in a `.env` file located in the root directory. The following variables are required:

- `DB_USER`: the username for the MongoDB database
- `DB_PASS`: the password for the MongoDB database
- `DB_HOST`: the host for the MongoDB database
- `DB_PORT`: the port for the MongoDB database
- `DB_NAME`: the name of the MongoDB database

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) for building the API
- [Celery](https://docs.celeryproject.org/en/stable/index.html) for task scheduling
- [MongoDB](https://www.mongodb.com/) for storing the data
- [Redis](https://redis.io/) for Celery message broker
- [Docker](https://www.docker.com/) for containerization

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.