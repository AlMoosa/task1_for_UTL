from django.urls import path
from .views import TaskappViewSet, TagappViewSet
# from taskapp.views import TaskappViewSet, TagappViewSet

urlpatterns = [
    path('tasks/', TaskappViewSet.as_view({
        'get': 'list', 'post': 'create'}),
         name='task_list_url'),
    path('tasks/<int:id>/', TaskappViewSet.as_view({
        'get': 'retrieve', 'delete': 'destroy',
        'put': 'update', 'patch': 'partial_update'}),
         name='task_detail_url'),
#   for Tags
    path('tags/', TagappViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='tag_list_url'),

    path('tags/<int:id>/', TagappViewSet.as_view({
        'get': 'retrieve', 'delete': 'destroy', 'put': 'update',
        'patch': 'partial_update'}),
         name='tag_detail_url'),
]