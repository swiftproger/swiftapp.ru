FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . .

RUN pip install -no-cashe-dir -r requirements.txt