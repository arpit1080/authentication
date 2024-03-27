from django.db import models

class userworkplace(models.Model):
    user_id = models.IntegerField()
    workplace_id = models.IntegerField()
