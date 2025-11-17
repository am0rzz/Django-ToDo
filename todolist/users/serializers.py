from .models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "date_of_birth"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
