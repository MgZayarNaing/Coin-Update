# Generated by Django 4.2 on 2024-03-29 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_depositmodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrmodel',
            name='customer',
        ),
    ]
