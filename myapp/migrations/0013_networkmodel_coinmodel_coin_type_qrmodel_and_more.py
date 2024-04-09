# Generated by Django 4.2 on 2024-03-29 03:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_coinmodel_status_usermodel_coin_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='coinmodel',
            name='coin_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.cointypemodel'),
        ),
        migrations.CreateModel(
            name='QRModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrcode', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('link_name', models.CharField(max_length=20)),
                ('link_address', models.CharField(max_length=50)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.usermodel')),
            ],
        ),
        migrations.CreateModel(
            name='DepositModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.BigIntegerField(default=0)),
                ('screenshot', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('coin_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.cointypemodel')),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.usermodel')),
                ('network_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.networkmodel')),
            ],
        ),
        migrations.AddField(
            model_name='coinmodel',
            name='network_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.networkmodel'),
        ),
    ]