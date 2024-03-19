# Generated by Django 5.0.1 on 2024-02-27 10:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_passwordreset_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]