import os
from celery import Celery

# set the default Django settings for `celery` program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jazz_reader.settings.development")

# pass the application name for prefixing task names
app = Celery('jazz_reader')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(['feeds'])

# debug task
@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
