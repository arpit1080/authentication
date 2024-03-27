from django.db import models


class project (models.Model):
    ROLE_CHOICES = (
        ('TO-DO', 'to-do'),
        ('IN_PROGRESS', 'in progress'),
        ('COMPLETED', 'completed'),
    )

    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()
    projecmanager = models.CharField(max_length=100)
    status = models.CharField(max_length=20,choices=ROLE_CHOICES,default='TO-DO')

    class Meta:
        db_table = 'project'
