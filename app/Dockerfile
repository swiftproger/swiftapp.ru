FROM python:3.10

RUN mkdir -p /app/
WORKDIR /app/
COPY . /app/


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
ENV TZ Europe/Moscow

