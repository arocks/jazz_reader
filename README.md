# Jazz Reader

Jazz Reader is a minimal news reader built with Django and Celery.

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv jazz_reader`
    2. `$ . jazz_reader/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

Start Redis and Celery in seperate terminals or as daemons:

    redis-server --port 6379
    celery --app=dj_news.celery:app --loglevel=INFO worker
    celery --app=dj_news.celery:app --loglevel=INFO beat -s /tmp/celerybeat-schedule
