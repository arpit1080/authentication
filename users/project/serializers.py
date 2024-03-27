from rest_framework import serializers
from users.project.models import project

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ['project_id', 'project_name','description','startdate','enddate','projecmanager','status']
