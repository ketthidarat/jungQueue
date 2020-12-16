from django.db import models

# Create your models here.
class farmer(models.Model):
    # farmer_id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=1000)
    farmer_lastname = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    phone = models.IntegerField()
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

class owner(models.Model):
    # owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=1000)
    owner_lastname = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    phone = models.IntegerField()
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

class work(models.Model):
    # work_id = models.AutoField(primary_key=True)
    work_status = models.CharField(max_length=1000)
    lat = models.CharField(max_length=1000)
    lng = models.CharField(max_length=1000)
    are = models.CharField(max_length=1000)
    workDetail = models.CharField(max_length=1000)
    RepairTime = models.DateTimeField(auto_now_add=True)
    Harverstime = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    money = models.IntegerField()
    moneyStatus = models.CharField(max_length=1000)

class tractor(models.Model):
    # tractor_id = models.AutoField(primary_key=True)
    owner_id = models.IntegerField()
    work_id = models.IntegerField()

class queue(models.Model):
    tractor_id = models.IntegerField()
    farmer_id = models.IntegerField()
    work_id = models.IntegerField()
    # queue_id = models.IntegerField()
    statusQueue = models.CharField(max_length=1000)