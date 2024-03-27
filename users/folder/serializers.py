from rest_framework import serializers
from users.folder.models import folder

class folderSerializer(serializers.ModelSerializer):
    class Meta:
        model = folder
        fields = ['folder_id', 'folder_name','description']


