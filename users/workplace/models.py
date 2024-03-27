from django.db import models

class workplace (models.Model):
    workplace_id = models.AutoField(primary_key=True)
    workplace_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'workplace'

