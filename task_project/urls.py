
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.2/topics/http/urls/


from django.contrib import admin
from django.urls import path, include
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='TaskManager')

urlpatterns = [
    # path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include('taskapp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
]


'''
    django-rest-auth endpoints
|Endpoint                          |HTTP Verb|
|----------------------------------|---------|
|/                                 |GET      |
|/:pk/                             |GET      |
|/rest-auth/registration           |POST     |
|/rest-auth/login                  |POST     |
|/rest-auth/logout                 |GET      |
|/rest-auth/password/reset         |POST     |
|/rest-auth/password/reset/confirm |POST     |
'''