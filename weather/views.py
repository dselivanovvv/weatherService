from django_filters import rest_framework as filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from weather.models import WeatherData
from weather.serializers import WeatherDataSerializer


class ProductFilter(filters.FilterSet):
    day = filters.DateFilter(field_name="date", lookup_expr='contains')

    class Meta:
        model = WeatherData
        fields = ['date']


class WeatherDataReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    filterset_class = ProductFilter
