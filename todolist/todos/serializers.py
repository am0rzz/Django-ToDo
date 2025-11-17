from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.IntegerField(write_only = True)
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "is_completed", "due_date", "owner"]
        read_only_fields = ["id", "owner"]
    

    def create(self, validated_data):
        """
        Create and return a new Todo instance
        """
        return Todo.objects.create(**validated_data)
    

    


