# Generated by Django 4.2 on 2024-03-28 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_usermodel_coin_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='coin_status',
        ),
        migrations.AddField(
            model_name='cointypemodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]