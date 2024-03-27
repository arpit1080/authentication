from rest_framework import serializers

from .models import User
from django.contrib.auth.hashers import make_password



class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['user_id','first_name', 'last_name', 'user_name', 'email', 'password']

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'password']