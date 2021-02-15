# Generated by Django 2.2.7 on 2021-02-15 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='workDetail',
            field=models.CharField(max_length=1000, verbose_name='รายละเอียด'),
        ),
        migrations.CreateModel(
            name='addTractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tractor_owner', models.CharField(max_length=1000)),
                ('tractor_name', models.CharField(max_length=1000)),
                ('tractor_detail', models.CharField(max_length=1000)),
                ('tractor_img', models.ImageField(max_length=1000, upload_to='')),
                ('tractor_timeHarvers', models.CharField(max_length=1000)),
                ('tractor_timeRepair', models.CharField(max_length=1000)),
                ('tractor_status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Tractor_status')),
            ],
            options={
                'verbose_name': 'เพิ่มข้อมูลรถเกี่ยวนวดข้าว',
            },
        ),
    ]