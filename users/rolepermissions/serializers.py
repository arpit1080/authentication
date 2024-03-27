from rest_framework import serializers
from .models import RolePermission


class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = ['role_id', 'permission_id']
