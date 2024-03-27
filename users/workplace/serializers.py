from rest_framework import serializers
from users.workplace.models import workplace


class workplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = workplace
        fields = ['workplace_id', 'workplace_name','description']

