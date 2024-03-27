from django.db import models

class permission (models.Model):

    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'permission'
  