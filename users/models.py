from django.db import models


# Create your models here.
class permission (models.Model):

    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'permission'
    
class role (models.Model):

    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100 ,unique=True)

    class Meta:
        db_table = 'role'


class RolePermission(models.Model):
    role_id = models.IntegerField()
    permission_id = models.IntegerField()

class userPermission(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()   
    permission_id = models.IntegerField()

class User(models.Model):
    ROLE_CHOICES = (
        (4, 'Role 4'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    role_id = models.IntegerField(choices=ROLE_CHOICES, default=4)

    class Meta:
        db_table = 'user'

    @property
    def role_choices_dict(self):
        return {4: 'Role 4'}
    
# class project (models.Model):
#     STATUS_CHOICES = (
#         ('TO-DO', 'To-Do'),
#         ('IN-PROGRESS', 'In Progress'),
#         ('COMPLETED', 'Completed'),
#     )
#     name = models.CharField(unique = True)
#     description = models.CharField(max_length=100)
#     startdate = models.DateField()
#     enddate = models.DateField()
#     projectmanager = models.ForeignKey('user',on_delete = models.CASCADE)
#     status = models.CharField(choices=STATUS_CHOICES, default='TO-DO')
#     priority = models.CharField()
#     filemanagement = models.FileField(upload_to='project_files/')
#     image =  models.ImageField(upload_to='project_query_files/')

#     class Meta:
#         db_table = 'project'


# class task (models.Model):
#     STATUS_CHOICES = (
#         ('TO-DO', 'To-Do'),
#         ('IN-PROGRESS', 'In Progress'),
#         ('COMPLETED', 'Completed'),
#     )
#     name = models.CharField(unique = True)
#     description = models.CharField(max_length=100)
#     startdate = models.DateField()
#     enddate = models.DateField()
#     user = models.ForeignKey('user',on_delete = models.CASCADE)
#     status = models.CharField(choices=STATUS_CHOICES, default='TO-DO')
#     priority = models.CharField()
#     filemanagement = models.FileField(upload_to='task_files/')
#     image =  models.ImageField(upload_to='task_query_files/')

#     class Meta:
#         db_table = 'task'
