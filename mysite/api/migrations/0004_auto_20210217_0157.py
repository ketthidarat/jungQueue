# Generated by Django 2.2.7 on 2021-02-16 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210217_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='money_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Money_status', verbose_name='สถานะการชำระเงิน'),
        ),
        migrations.AlterField(
            model_name='work',
            name='work_status',
            field=models.ForeignKey(default=' ', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Work_status', verbose_name='สถานะงาน'),
        ),
    ]
