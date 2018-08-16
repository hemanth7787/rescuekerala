from rest_framework import serializers
from mainapp.models import Request


class RequestSerializer(serializers.ModelSerializer):
    """
    Serializer for Request model
    """
    pass

    class Meta:
        model = Request
        fields = '__all__'

