from django.db import models


class WeatherData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    city = models.CharField(max_length=255)

    class Meta:
        ordering = ('-date', )
