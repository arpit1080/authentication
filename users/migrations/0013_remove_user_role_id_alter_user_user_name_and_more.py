# Generated by Django 5.0.1 on 2024-03-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_options_alter_user_role_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='PasswordReset',
        ),
    ]
