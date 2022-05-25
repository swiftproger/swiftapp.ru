FROM python:3.10

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . /usr/src/app/

RUN pip install -no-cashe-dir -r requirements.txt