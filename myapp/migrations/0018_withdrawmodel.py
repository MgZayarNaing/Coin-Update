# Generated by Django 4.2 on 2024-03-29 12:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_qrmodel_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithDrawModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.BigIntegerField(default=0)),
                ('address', models.TextField(default=None)),
                ('status', models.BooleanField(default=False)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('coin_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.cointypemodel')),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.usermodel')),
                ('network_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.networkmodel')),
            ],
        ),
    ]
