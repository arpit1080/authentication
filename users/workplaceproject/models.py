from django.db import models

class workplaceproject(models.Model):
    workplace_id = models.IntegerField()
    project_id = models.IntegerField()
