# Generated by Django 5.0.1 on 2024-02-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.IntegerField(choices=[(1, 'Role 1'), (2, 'Role 2'), (3, 'Role 3'), (4, 'Role 4')]),
        ),
    ]
