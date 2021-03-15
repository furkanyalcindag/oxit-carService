# Generated by Django 3.1.7 on 2021-03-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carService', '0028_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
    ]
