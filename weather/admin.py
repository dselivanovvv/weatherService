from django.contrib import admin

from weather.models import WeatherData


@admin.register(WeatherData)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'temperature', 'city',)
