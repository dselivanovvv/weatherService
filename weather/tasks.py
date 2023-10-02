import requests
from celery import shared_task

from weather.models import WeatherData


@shared_task(name='get_weather_data')
def get_weather_data(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?' \
          f'units=metric&' \
          f'appid={api_key}&' \
          f'q={city}'

    res = requests.get(url).json()

    main_data = res.get('main', None)
    if main_data:
        temperature = main_data.get('temp', None)
        if temperature:
            wd = WeatherData.objects.create(temperature=temperature, city=city)
            return f'Weather data received and saved: id={wd.id}, date={wd.date}, temp={wd.temperature}, city={wd.city}'
        else:
            return f'Weather data received but not saved: temp={temperature}'
    return f'Weather data not received: main={main_data}'
