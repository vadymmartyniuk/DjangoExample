from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

from lab6.models import Lab6
from lab6.api.serializers import Lab6Serializer


class Lab6ApiViewSet(viewsets.ModelViewSet):
    queryset = Lab6.objects.all()
    serializer_class = Lab6Serializer

    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('id',)
    permission_classes = (AllowAny,)

    ordering_field = ('id',)
    ordering = ('-id',)
