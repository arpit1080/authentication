from rest_framework import serializers
from users.userproject.models import userproject


class userprojectSerializer(serializers.ModelSerializer):
    class Meta:
        model =userproject
        fields = ['project_id', 'user_id']
