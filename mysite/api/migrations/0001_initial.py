# Generated by Django 2.2.7 on 2020-12-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=1000)),
                ('farmer_lastname', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=1000)),
                ('owner_lastname', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tractor_id', models.IntegerField()),
                ('farmer_id', models.IntegerField()),
                ('work_id', models.IntegerField()),
                ('statusQueue', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='tractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField()),
                ('work_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_status', models.CharField(max_length=1000)),
                ('lat', models.CharField(max_length=1000)),
                ('lng', models.CharField(max_length=1000)),
                ('are', models.CharField(max_length=1000)),
                ('workDetail', models.CharField(max_length=1000)),
                ('RepairTime', models.DateTimeField(auto_now_add=True)),
                ('Harverstime', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('money', models.IntegerField()),
                ('moneyStatus', models.CharField(max_length=1000)),
            ],
        ),
    ]
