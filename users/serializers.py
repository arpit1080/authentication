from rest_framework import serializers
from users.models import role
from users.models import permission
from .models import RolePermission,userPermission
from .models import User
from django.contrib.auth.hashers import make_password


class permissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = permission
        fields = ['permission_id','permission_name','description']



class roleSerializers(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = ['role_id','role_name']


class userPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = userPermission
        fields = ['id', 'permission_id']


class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = ['role_id', 'permission_id']


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'user_name', 'email', 'password']

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'password']



# class project(serializers.ModelSerializer):
#     class meta:
#         model = project
#         fields = ['project_id','name','description','startdate','enddate','projectmanager','status','filemanagement']


