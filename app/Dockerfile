FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV TZ Europe/Moscow

CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]