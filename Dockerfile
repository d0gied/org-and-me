# Use an official Python runtime as a parent image
FROM python:3.11.2-slim

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY handlers /app/handlers
COPY main.py /app/main.py
COPY poetry.lock /app/poetry.lock
COPY pyproject.toml /app/pyproject.toml

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi

CMD ["python", "main.py"]
