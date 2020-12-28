from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Farmer(models.Model):
    # farmer_id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=1000)
    # farmer_lastname = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    
    def __str__(self):
        return f'{self.farmer_name} {self.address} {self.phone} {self.email} {self.username} {self.password}'
class Owner(models.Model):
    # owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=1000)
    # owner_lastname = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.owner_name} {self.phone}'


class Tractor(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    # tractor_id = models.AutoField(primary_key=True)
    work_id = models.CharField(max_length=1000)

    # def __str__(self):
    #     return f'{self.owner}'

class Rice_type(models.Model):
    rice_type = models.CharField(max_length=100) 
    
    def __str__(self):
         return f'{self.rice_type}'

class Work_status (models.Model):
    work_status  = models.CharField(max_length=100) 
    def __str__(self):
         return f'{self.work_status}'

class Money_status(models.Model):
    moneyStatus = models.CharField(max_length=100) 
    def __str__(self):
         return f'{self.moneyStatus}'

class Work(models.Model):
    #farmer
    #tractor
    # work_id = models.AutoField(primary_key=True)
    # work_status = models.CharField(max_length=1000)
    lat = models.CharField(max_length=1000)
    lng = models.CharField(max_length=1000)
    area = models.IntegerField()
    # rice_type = models.CharField(max_length=100) 
    rice_type = models.ForeignKey(Rice_type, on_delete=models.CASCADE)
    other = models.CharField(max_length=1000) 
    workDetail = models.CharField(max_length=1000)
    RepairTime = models.CharField(max_length=1000) 
    Harverstime = models.CharField(max_length=1000) 
    date = models.CharField(max_length=1000) 
    money = models.IntegerField()
    moneyStatus = models.ForeignKey(Money_status, on_delete=models.CASCADE) # ให้นิยามเพิ่มเติม
    workstatus = models.ForeignKey(Work_status, on_delete=models.CASCADE) # รับ ไม่รับ จ่าย
    # moneyStatus = models.CharField(max_length=100) 
    # work_status = models.CharField(max_length=100) 
   

   
"""
class queue(models.Model):
    tractor = models.ForeignKey(tractor, on_delete=models.CASCADE)
    farmer_id = models.IntegerField()
    work_id = models.IntegerField()
    # queue_id = models.IntegerField()
    statusQueue = models.CharField(max_length=1000)
"""
