from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Taskapp, Tagapp

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class TaskappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskapp
        fields = ('id', 'title', 'description', 'created_at', 'finished_date')


class TagappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tagapp
        fields = ('id', 'title', 'date')
