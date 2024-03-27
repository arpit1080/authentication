from rest_framework import serializers

from users.subfolder.models import subfolder

class subfolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = subfolder
        fields = ['subfolder_id', 'subfolder_name','description']
