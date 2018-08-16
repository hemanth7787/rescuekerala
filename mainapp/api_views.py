from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import viewsets

from mainapp.models import Request
from mainapp.serializers import RequestSerializer


class RequestViewSet(viewsets.ModelViewSet):
    """
    ## *Viewset for CRUD operations of predefined rescue requests*
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
