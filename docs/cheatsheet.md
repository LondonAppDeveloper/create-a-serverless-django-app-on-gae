# Cheatsheet

## Docker Compose Commands

### Django Commands

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

### Deployment Commands

Check version of CloudSDK:

```sh
docker-compose -f docker-compose-deploy.yml run gcloud gcloud version
```

Authenticate with Google Cloud Platform (GCP):

```sh
docker-compose -f docker-compose-deploy.yml run gcloud gcloud auth login
```

Deploy to GAE:

 * Replace `PROJECT_ID` with your Google Cloud Project ID.

```sh
docker-compose run --rm app sh -c "python manage.py collectstatic --noinput"
docker-compose -f docker-compose-deploy.yml run gcloud gcloud app deploy --project PROJECT_ID
```


