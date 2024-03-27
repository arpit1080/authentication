from django.db import models

class RolePermission(models.Model):
    role_id = models.IntegerField()
    permission_id = models.IntegerField()
