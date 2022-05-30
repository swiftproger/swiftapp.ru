FROM python:3.10
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
#EXPOSE 80
ENV TZ Europe/Moscow
#CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:4000", "main:app"]