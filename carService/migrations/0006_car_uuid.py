# Generated by Django 3.1 on 2020-10-09 07:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('carService', '0005_auto_20201008_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
