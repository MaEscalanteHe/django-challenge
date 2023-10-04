FROM python:3.10.9-alpine

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

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
# ENTRYPOINT [ "python" "manage.py"]
CMD [ "runserver", "0.0.0.0:8080" ]
