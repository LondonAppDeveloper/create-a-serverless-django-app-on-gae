# Cheatsheet

## Docker Compose Commands

Create Django project:

```sh
docker-compose run --rm app sh -c "django-admin startproject app ."
```

Start app called `bouncer`:

```sh
docker-compose run --rm app sh -c "python manage.py startapp bouncer
```

Run development server:

```sh
docker-compose up
```
