from rest_framework import serializers
from .models import userPermission


class userPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = userPermission
        fields = ['id','permission_id']
