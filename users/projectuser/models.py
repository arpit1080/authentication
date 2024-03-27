from django.db import models

class projectuser(models.Model):
    project_id = models.IntegerField()
    user_id = models.IntegerField()
