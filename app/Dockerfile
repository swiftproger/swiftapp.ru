FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . .

RUN apk add --update --no-cashe --virtual .tmp-build-deps \
    pip install -no-cashe-dir -r requirements.txt