# Generated by Django 3.1.1 on 2021-03-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carService', '0028_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='isSendMail',
            field=models.BooleanField(default=False),
        ),
    ]