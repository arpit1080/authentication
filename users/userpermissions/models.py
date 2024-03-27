from django.db import models

class userPermission(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()   
    permission_id = models.IntegerField()