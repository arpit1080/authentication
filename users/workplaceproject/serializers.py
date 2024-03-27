from rest_framework import serializers
from users.workplaceproject.models import workplaceproject


class workplaceprojectSerializer(serializers.ModelSerializer):
    class Meta:
        model = workplaceproject
        fields = ['project_id', 'user_id']
