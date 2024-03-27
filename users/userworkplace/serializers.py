from rest_framework import serializers
from users.userworkplace.models import userworkplace


class userworkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model =userworkplace
        fields = ['user_id', 'workplace_id']
