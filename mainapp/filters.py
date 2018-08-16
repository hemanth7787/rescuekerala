from django_filters import rest_framework as filters
from mainapp.models import Request


class RequestAPIFilter(filters.FilterSet):
    status = filters.CharFilter()

    class Meta:
        model = Request
        fields = '__all__'
