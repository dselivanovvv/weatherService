from django.apps import AppConfig


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'

    def ready(self):
        # Import celery app now that Django is mostly ready.
        # This initializes Celery and autodiscovers tasks
        import weatherService.celery
