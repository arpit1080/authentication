from rest_framework import serializers
from users.models import role



class roleSerializers(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = ['role_id','role_name']
