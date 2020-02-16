from rest_framework import viewsets

from .models import Taskapp, Tagapp
from .serializers import TaskappSerializer, TagappSerializer


class TaskappViewSet(viewsets.ModelViewSet):
    serializer_class = TaskappSerializer
    lookup_field = 'id'
    queryset = Taskapp.objects.all()


class TagappViewSet(viewsets.ModelViewSet):
    serializer_class = TagappSerializer
    lookup_field = 'id'
    queryset = Tagapp.objects.all()
