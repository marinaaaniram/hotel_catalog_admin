import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from hotels.models import Hotel
from hotels.serializers import HotelSerializer


class HotelFilter(django_filters.FilterSet):
    city_id = django_filters.NumberFilter(field_name='city__id')
    from_id = django_filters.NumberFilter(field_name='id', lookup_expr='gte')
    limit = django_filters.NumberFilter(method='filter_limit')

    class Meta:
        model = Hotel
        fields = ['city_id', 'from_id']

    def filter_limit(self, queryset, name, value):
        return queryset[:value]


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HotelFilter
