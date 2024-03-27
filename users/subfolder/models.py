from django.db import models

class subfolder (models.Model):
    subfolder_id = models.AutoField(primary_key=True)
    subfolder_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'subfolder'