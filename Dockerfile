FROM python:3.11.5-alpine

EXPOSE 8080

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
