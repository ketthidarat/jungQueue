from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Farmer(models.Model):
    id = models.AutoField(primary_key=True) 
    # farmer_id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=1000)
    # farmer_lastname = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media/')
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    
    def __str__(self):
        return f'{self.farmer_name} {self.address} {self.phone} {self.email} {self.username} {self.password}'
class Owner(models.Model):
    id = models.AutoField(primary_key=True) 
    # owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=1000)
    # owner_lastname = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media/')
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.owner_name} {self.phone}'

class Tractor_status(models.Model):
    id = models.AutoField(primary_key=True) 
    tractor_status = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.tractor_status}'


class Tractor(models.Model):
    id = models.AutoField(primary_key=True) 
    # owner_name = models.ForeignKey(Owner, on_delete=models.CASCADE)
    tractor = models.CharField(max_length=1000)
    tractor_status = models.ForeignKey(Tractor_status, on_delete=models.CASCADE)
    # work = models.ForeignKey(Owner, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.owner}'



class Rice_type(models.Model):
    id = models.AutoField(primary_key=True) 
    rice_type = models.CharField(max_length=100) 
    
    def __str__(self):
         return f'{self.rice_type}'

    class Meta:
        verbose_name = 'ลักษณะข้าวที่จะให้เกี่ยว'

class Work_status (models.Model):
    id = models.AutoField(primary_key=True) 
    work_status  = models.CharField(max_length=100, verbose_name="สถานะงาน") 
    def __str__(self):
         return f'{self.work_status}'

    class Meta:
        verbose_name = 'สถานะงาน'

class Money_status(models.Model):
    id = models.AutoField(primary_key=True) 
    money_status = models.CharField(max_length=100) 

    def __str__(self):
         return f'{self.money_status}'

class Work(models.Model):
    id = models.AutoField(primary_key=True) 
    farmer_name = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    # farmer_lastname = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE)
    # work_id = models.AutoField(primary_key=True)
    # work_status = models.CharField(max_length=1000)
    lat = models.CharField(max_length=1000, verbose_name='ละติจูด')
    lng = models.CharField(max_length=1000, verbose_name='ลองติจูด')
    area = models.IntegerField(verbose_name='พืนที่ (ตรว)')
    rice_type = models.ForeignKey(Rice_type, on_delete=models.CASCADE, verbose_name='ลักษณะข้าวที่จะให้เกี่ยว')
    other = models.CharField(max_length=1000) 
    workDetail = models.CharField(max_length=1000)
    RepairTime = models.CharField(max_length=1000) 
    Harverstime = models.CharField(max_length=1000) 
    date_start = models.DateTimeField(auto_now=False)
    date_end = models.DateTimeField(auto_now=False)
    money = models.IntegerField()
    tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE)
    tractor_status = models.ForeignKey(Tractor_status, on_delete=models.CASCADE)
    money_status = models.ForeignKey(Money_status, on_delete=models.CASCADE) # ให้นิยามเพิ่มเติม
    work_status = models.ForeignKey(Work_status, on_delete=models.CASCADE) # รับ ไม่รับ จ่าย
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
