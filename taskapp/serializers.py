from rest_framework import serializers
from .models import Taskapp, Tagapp


class TaskappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskapp
        fields = ('id', 'title', 'description', 'tags', 'created_at',)


class TagappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tagapp
        fields = ('id', 'title', 'tasks', 'created_at',)
