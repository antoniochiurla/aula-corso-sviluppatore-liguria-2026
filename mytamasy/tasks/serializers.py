from rest_framework import serializers
from .models import Task, BugTask, FeatureTask

class TaskSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    task_type = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'created_by', 'created_by_username', 'status', 'task_type']
        read_only_fields = ['created_by', 'created_at']

    def get_task_type(self, obj):
        if hasattr(obj, 'bugtask'):
            return 'bug'
        elif hasattr(obj, 'featuretask'):
            return 'feature'
        return 'base'

class BugTaskSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = BugTask
        fields = ['id', 'title', 'description', 'created_at', 'created_by', 'created_by_username', 'status', 'severity']
        read_only_fields = ['created_by', 'created_at']

class FeatureTaskSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = FeatureTask
        fields = ['id', 'title', 'description', 'created_at', 'created_by', 'created_by_username', 'status', 'priority']
        read_only_fields = ['created_by', 'created_at']
