from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserSerializer

from taskapp.permissions import IsAuthorOrReadOnly # new
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import IsAdminUser



class UserList(generics.ListAPIView):   #ListCreateAPIView
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


#    ListCreateAPIView не добавил. единственный минус думаю