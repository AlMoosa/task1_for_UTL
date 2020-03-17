from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .models import Taskapp, Tagapp
from .serializers import TaskappSerializer, TagappSerializer, UserSerializer

# User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class TaskappViewSet(viewsets.ModelViewSet):
    serializer_class = TaskappSerializer
    lookup_field = 'id'
    queryset = Taskapp.objects.all()



class TagappViewSet(viewsets.ModelViewSet):
    serializer_class = TagappSerializer
    lookup_field = 'id'
    queryset = Tagapp.objects.all()
