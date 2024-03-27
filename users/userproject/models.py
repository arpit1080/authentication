from django.db import models

class userproject(models.Model):
    project_id = models.IntegerField()
    user_id = models.IntegerField()
