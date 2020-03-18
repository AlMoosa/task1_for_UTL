from django.urls import path
from .views import UserDetail, UserList
# from rest_framework import routers
# from rest_framework import generics


urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
]