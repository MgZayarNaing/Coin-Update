# Generated by Django 4.2 on 2024-04-01 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_delete_heromodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(default=None)),
                ('background_image', models.ImageField(default=None, upload_to='')),
                ('image', models.ImageField(default=None, upload_to='')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
