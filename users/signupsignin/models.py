from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        (4, 'Role 4'),
    )
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    role_id = models.IntegerField(choices=ROLE_CHOICES, default=4)

    class Meta:
        db_table = 'user'