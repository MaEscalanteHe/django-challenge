# Product Inventory System

Project of Manuel Escalante's technical interview for RatherLabs in which he developed a product inventory system API. This API provides functionalities like CRUD operations on products, and querying products based on different filters. Developed in Django with SQLite for local executions and PostgreSQL when running within Docker.

# Initial Setup

### Requirements

1. Install [docker](https://docs.docker.com/engine/install/)
2. Install [docker-compose](https://docs.docker.com/compose/install/)

3. Copy the `.env.example` to `.env` and adjust the values accordingly.

```bash
cp .env.example .env
```

If you wish to interact with the bash shell within the container:

```bash
docker compose exec web bash
```

### Database

For local executions, SQLite is used and no further configuration is required.

For Docker executions:

```bash
NAME: rather
USER: rather
PASSWORD: rather_password123
HOST: localhost
PORT: 5432
```

With the virtual environment active:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
