# Import celery when Django starts for shared_tasks
from .celery import app as celery_app
