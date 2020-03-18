from django.urls import path, include
# from .views import TaskappViewSet, TagappViewSet
from rest_framework import routers
from taskapp.views import TaskappViewSet, TagappViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskappViewSet, basename='tasks')
router.register('tags', TagappViewSet, basename='tags')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls








# urlpatterns = [
#     path('tasks/', TaskappViewSet.as_view({
#         'get': 'list', 'post': 'create'}),
#          name='task_list_url'),
#     path('tasks/<int:id>/', TaskappViewSet.as_view({
#         'get': 'retrieve', 'delete': 'destroy',
#         'put': 'update', 'patch': 'partial_update'}),
#          name='task_detail_url'),
# #   for Tags
#     path('tags/', TagappViewSet.as_view({'get': 'list', 'post': 'create'}),
#          name='tag_list_url'),

#     path('tags/<int:id>/', TagappViewSet.as_view({
#         'get': 'retrieve', 'delete': 'destroy', 'put': 'update',
#         'patch': 'partial_update'}),
#          name='tag_detail_url'),
# ]