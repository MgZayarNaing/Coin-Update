# Generated by Django 4.2 on 2024-04-01 08:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_delete_qrmodel_remove_coinmodel_network_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('qrcode', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('link_name', models.CharField(max_length=20)),
                ('link_address', models.CharField(max_length=50)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='coinmodel',
            name='network_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.networkmodel'),
        ),
        migrations.AddField(
            model_name='depositmodel',
            name='network_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.networkmodel'),
        ),
        migrations.AddField(
            model_name='withdrawmodel',
            name='network_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.networkmodel'),
        ),
    ]
