from django.urls import path
# from .views import TaskappView, TagappView
from .views import TaskappViewSet, TagappViewSet
# from users.views import UserList, UserDetail
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('tasks', TaskappViewSet, basename='tasks')
# router.register('tags', TagappViewSet, basename='tags')

# urlpatterns = router.urls

# req1 = {'get': 'list', 'post': 'create'}
# req2 = {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}

# urlpatterns = [
#     path('tasks/', TaskappView.as_view(req1), name='tasks_list_url'),
#     path('tasks/<int:id>/', TaskappView.as_view(req2), name='tasks_detail_url'),

#     path('tags/', TagappView.as_view(req1), name='tags_list_url'),
#     path('tags/<int:id>/', TagappView.as_view(req2), name='tags_detail_url'),

#     path('users/', UserList.as_view(), name='users_list_url'),
#     path('users/<int:id>/', UserDetail.as_view(req2), name='users_detail_url'),
    
# ]



urlpatterns = [
    path('tasks/', TaskappViewSet.as_view({
        'get': 'list', 'post': 'create'}),
        name='tasks_list_url'),
    path('tasks/<int:id>/', TaskappViewSet.as_view({
        'get': 'retrieve', 'delete': 'destroy',
        'put': 'update', 'patch': 'partial_update'}),
        name='tasks_detail_url'),

        
    #   for Tags
    path('tags/', TagappViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='tag_list_url'),

    path('tags/<int:id>/', TagappViewSet.as_view({
        'get': 'retrieve', 'delete': 'destroy', 'put': 'update',
        'patch': 'partial_update'}),
        name='tag_detail_url'),
]
