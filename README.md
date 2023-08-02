# Satellite Monitoring

A web application to monitor status of the statellite on space.


## Run the application
    $ python -m venv <virtual env path>
    $ source <virtual env path>/bin/activate
    $ pip install -r requirements/local.txt
    $ createdb satellite_monitoring_db
    $ python manage.py migrate
    $ python manage.py runserver

## Basic Commands

### Setting Up Your Users

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser


## Celery

This app comes with Celery.

To run a celery worker:

You can embed the beat service inside a worker with the `-B` option (not recommended for production use):

This allows you to run the periodic task

```bash
cd satellite_monitoring
celery -A config.celery_app worker -B -l info
```

## Running the periodic tasks:

After running the celery command, please create a data inside `IntervalSchedule` using Django Admin.

Set the periods to `every 10 seconds`

Then, create a `PeriodicTask` which will run the task inside `Task (registered)` field.

Make sure to set a value under the interval schedule field based on the data you just created.

This will run all necessary actions needed.


## Environment variables

Please make sure you create a `.env` file and write include this variables.

```bash
DJANGO_READ_DOT_ENV_FILE=True
CELERY_BROKER_URL="redis://localhost:6379/0"
```



