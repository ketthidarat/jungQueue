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

    def __str__(self):
        return f'{self.owner_name} {self.phone}'

class work(models.Model):
    #farmer
    #tractor
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
    moneyStatus = models.CharField(max_length=1000) # ให้นิยามเพิ่มเติม
    workstatus = models.CharField(max_length=1000) # รับ ไม่รับ จ่าย

class tractor(models.Model):
    owner = models.ForeignKey(owner, on_delete=models.CASCADE)
    # tractor_id = models.AutoField(primary_key=True)
    work_id = models.IntegerField()

    def __str__(self):
        return f'{self.owner}'

"""
class queue(models.Model):
    tractor = models.ForeignKey(tractor, on_delete=models.CASCADE)
    farmer_id = models.IntegerField()
    work_id = models.IntegerField()
    # queue_id = models.IntegerField()
    statusQueue = models.CharField(max_length=1000)
"""
