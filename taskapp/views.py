from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Taskapp, Tagapp
from .permissions import IsAuthorOrReadOnly
# , IsAuthenticatedOrReadOnly  # IsAuthenticated
from rest_framework.permissions import IsAdminUser
from .serializers import TaskappSerializer, TagappSerializer, UserSerializer

#   такая моделька пойдет), я так думаю
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class TaskappViewSet(viewsets.ModelViewSet):
    serializer_class = TaskappSerializer
    lookup_field = 'id'
    queryset = Taskapp.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)


class TagappViewSet(viewsets.ModelViewSet):
    serializer_class = TagappSerializer
    lookup_field = 'id'
    queryset = Tagapp.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)


#   IsAuthorOrReadOnly плюс в том что таски может
#   редактировать и удалять только Текущий пользователь.
# Но минус в том что у Неавторизованных есть все права на CRUD
# 
# 
##  IsAuthenticatedOrReadOnly  # IsAuthenticated  плюсы что 
#   НеАвторизованные могут только читать или вообще Ничего.
# Но минус: Авторизованные могут удалять таски Других Юзеров

# pipenv install autopep8 --dev
