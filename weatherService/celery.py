import os
from celery import Celery
from celery.schedules import crontab

from weatherService.settings import WEATHER_CITY, OPENWEATHER_API_KEY

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weatherService.settings')
app = Celery('weatherService')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get-hourly-weather-data': {
        'task': 'get_weather_data',
        'schedule': crontab(minute='0', hour='*'),
        # 'schedule': crontab(minute='*/5', hour='*'),
        'args': (WEATHER_CITY, OPENWEATHER_API_KEY, ),
    }
}
