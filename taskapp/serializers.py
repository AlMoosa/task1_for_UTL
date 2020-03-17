from rest_framework import serializers
from .models import Taskapp, Tagapp

# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User


class TaskappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taskapp
        fields = ('id', 'title', 'description', 'created_at', 'finished_date')


class TagappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tagapp
        fields = ('id', 'title', 'date')
