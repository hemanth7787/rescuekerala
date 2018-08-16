from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from mainapp.filters import RequestAPIFilter
from mainapp.models import Request
from mainapp.serializers import RequestSerializer
from django_filters import rest_framework as filters


class RequestViewSet(viewsets.ModelViewSet):
    """
    ## *Viewset for CRUD operations of predefined rescue requests*
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RequestAPIFilter
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
