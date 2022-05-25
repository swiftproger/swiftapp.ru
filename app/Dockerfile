FROM python:3.10
RUN mkdir -p /usr/src/app/
WORKDIR /app/
COPY . /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV TZ Europe/Moscow