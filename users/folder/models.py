from django.db import models

class folder (models.Model):
    folder_id = models.AutoField(primary_key=True)
    folder_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'folder'
