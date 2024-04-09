# Generated by Django 4.2 on 2024-03-26 10:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_usermodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.BigIntegerField(default=0)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.usermodel')),
            ],
        ),
    ]