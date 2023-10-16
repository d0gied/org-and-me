# Use an official Python runtime as a parent image
FROM python:3.11.2-slim

WORKDIR /app

RUN pip install poetry

# Copy the current directory contents into the container at /app
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi

COPY . /app

CMD ["python", "main.py"]
