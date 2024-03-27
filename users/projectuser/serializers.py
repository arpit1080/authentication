from rest_framework import serializers
from users.projectuser.models import projectuser


class projectuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectuser
        fields = ['project_id', 'user_id']
