from django.urls import path, include
from rest_framework import routers
from .views import TaskappViewSet, TagappViewSet
# from taskapp.views import TaskappViewSet, TagappViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskappViewSet, basename='tasks')
router.register(r'tags', TagappViewSet, basename='tags')
# router.register('user/', TaskappViewSet)
urlpatterns = router.urls


# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]






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