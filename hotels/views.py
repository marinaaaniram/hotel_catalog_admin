import django_filters
from rest_framework import viewsets
from hotels.models import Hotel
from hotels.serializers import HotelSerializer


class HotelFilter(django_filters.FilterSet):
    city_id = django_filters.NumberFilter(name='city__id')
    from_id = django_filters.NumberFilter(name='id', lookup_expr='gte')
    # limit = django_filters.CharFilter(name='category')

    class Meta:
        model = Hotel
        fields = ['city_id', 'from_id']


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [HotelFilter]
