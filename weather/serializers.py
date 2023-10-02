from rest_framework.serializers import ModelSerializer

from weather.models import WeatherData


class WeatherDataSerializer(ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'
