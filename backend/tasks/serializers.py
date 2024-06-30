from rest_framework import serializers
from .models import Task

class TaskSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'done', 'created_at')
        read_only_fields = ('id', 'created_at')