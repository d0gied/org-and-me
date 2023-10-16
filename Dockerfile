# Use an official Python runtime as a parent image
FROM python:3.11.2-slim

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi

CMD ["python", "main.py"]
