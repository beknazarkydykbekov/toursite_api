FROM python:3.11

RUN apt-get update

RUN pip install --upgrade pip

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip install -r requirements.txt

RUN chmod +x web-runner.sh