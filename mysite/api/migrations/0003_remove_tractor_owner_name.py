# Generated by Django 2.2.7 on 2021-01-03 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210103_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tractor',
            name='owner_name',
        ),
    ]
