from django.db import models


class role (models.Model):

    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100 ,unique=True)

    class Meta:
        db_table = 'role'

