from rest_framework import serializers
from users.models import permission




class permissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = permission
        fields = ['permission_id','permission_name','description']

