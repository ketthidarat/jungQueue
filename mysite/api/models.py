from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Farmer(models.Model):
    id = models.AutoField(primary_key=True) 
    # farmer_id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=1000, verbose_name = 'ชื่อ-สกุล')
    # farmer_lastname = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media/', verbose_name = 'รูปโปรไฟล์')
    address = models.CharField(max_length=1000, verbose_name = 'ที่อยู่')
    phone = models.CharField(max_length=1000, verbose_name = 'เบอร์โทรศัพท์')
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    
    def __str__(self):
        return f'{self.farmer_name} '

    class Meta:
        verbose_name = 'เกษตรกร'
class Owner(models.Model):
    id = models.AutoField(primary_key=True) 
    # owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=1000, verbose_name = 'ชื่อ-สกุล')
    # owner_lastname = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media/', verbose_name = 'รูปโปรไฟล์')
    address = models.CharField(max_length=1000, verbose_name = 'ที่อยู่')
    phone = models.CharField(max_length=1000, verbose_name = 'เบอร์โทรศัพท์')
    email = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.owner_name} {self.phone}'

    class Meta:
        verbose_name = 'เจ้าของรถ'

class Tractor_status(models.Model):
    id = models.AutoField(primary_key=True) 
    tractor_status = models.CharField(max_length=1000, verbose_name = 'สถานะรถเกี่ยวนวดข้าว')

    def __str__(self):
        return f'{self.tractor_status}'

    class Meta:
        verbose_name = 'สถานะรถเกี่ยวนวดข้าว'


class Tractor(models.Model):
    id = models.AutoField(primary_key=True) 
    # owner_name = models.ForeignKey(Owner, on_delete=models.CASCADE)
    tractor = models.CharField(max_length=1000)
    tractor_status = models.ForeignKey(Tractor_status, on_delete=models.CASCADE, null=True, default=1 )
    # work = models.ForeignKey(Owner, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.owner}'

    def __str__(self):
        return f'{self.tractor} {self.tractor_status}'
    class Meta:
        verbose_name = 'รถเกี่ยวนวดข้าว'


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
    money_status = models.CharField(max_length=100, verbose_name = 'สถานะการชำระเงิน') 

    def __str__(self):
         return f'{self.money_status}'

    class Meta:
        verbose_name = 'สถานะการชำระเงิน'

class Work(models.Model):
    # id = models.AutoField(primary_key=True) 
    # farmer_name = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=True,  verbose_name='เกษตรกร')
    # farmer_lastname = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    # tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE, null=True,  verbose_name='รถเกี่ยวนวดข้าว')
    # work_id = models.AutoField(primary_key=True)
    # work_status = models.CharField(max_length=1000)
    # lat = models.CharField(max_length=1000, verbose_name='ละติจูด')
    # lng = models.CharField(max_length=1000, verbose_name='ลองติจูด')
    area = models.IntegerField(verbose_name='พื้นที่ (ไร่)')
    rice_type = models.ForeignKey(Rice_type, on_delete=models.CASCADE, null=True, default=1, verbose_name='ลักษณะข้าวที่จะให้เกี่ยว')
    rice = models.CharField(max_length=1000,  verbose_name='พันธุ์ข้าว') 
    workDetail = models.CharField(max_length=1000,  verbose_name='รายละเอียด')
    # RepairTime = models.CharField(max_length=1000,  verbose_name='เวลาที่ใช้ซ่อมรถ (ชม.)') 
    # Harverstime = models.CharField(max_length=1000,  verbose_name='เวลาที่ใช้เก็บเกี่ยว (ชม.)') 
    # date_start = models.DateTimeField(auto_now=False,  verbose_name='วันที่เริ่มเก็บเกี่ยว')
    # date_end = models.DateTimeField(auto_now=False,  verbose_name='วันสิ้นสุดการเก็บเกี่ยว')
    # money = models.IntegerField(  verbose_name='จำนวนเงิน (บาท)')
    # tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE, null=True,  verbose_name='รถเกี่ยวนวดข้าว')
    # tractor_status = models.ForeignKey(Tractor_status, on_delete=models.CASCADE, null=True, default=1,  verbose_name='สถานะรถเกี่ยวนวดข้าว')
    # money_status = models.ForeignKey(Money_status, on_delete=models.CASCADE, null=True, default=1,  verbose_name='สถานะการชำระเงิน') # ให้นิยามเพิ่มเติม
    # work_status = models.ForeignKey(Work_status, on_delete=models.CASCADE, null=True, default=1, verbose_name='สถานะงาน') # รับ ไม่รับ จ่าย
    # moneyStatus = models.CharField(max_length=100) 
    # work_status = models.CharField(max_length=100) 
   
    def __str__(self):
         return f'{self.area}'

    class Meta:
        verbose_name = 'งานที่ต้องเก็บเกี่ยว'

# class Venue(models.Model):

#     name = models.CharField(max_length=255)
#     latitude = models.DecimalField(
#                 max_digits=9, decimal_places=6, null=True, blank=True)
#     longitude = models.DecimalField(
#                 max_digits=9, decimal_places=6, null=True, blank=True)
    
class addTractor(models.Model):
    # tractor_owner = models.CharField(max_length=1000)
    tractor_name = models.CharField(max_length=1000)
    tractor_detail = models.CharField(max_length=1000)
    # tractor_img = models.ImageField(max_length=1000)
    tractor_timeHarvers = models.CharField(max_length=1000)
    tractor_timeRepair = models.CharField(max_length=1000)
    tractor_status = models.ForeignKey(Tractor_status, on_delete=models.CASCADE, null=True, default=1 )

    def __str__(self):
        return f'{self.tractor_name}'
    class Meta:
        verbose_name = 'เพิ่มข้อมูลรถเกี่ยวนวดข้าว'

   

    # def get_absolute_url(self):
    #     return reverse("addTractor_detail", kwargs={"pk": self.pk})

"""
class queue(models.Model):
    tractor = models.ForeignKey(tractor, on_delete=models.CASCADE)
    farmer_id = models.IntegerField()
    work_id = models.IntegerField()
    # queue_id = models.IntegerField()
    statusQueue = models.CharField(max_length=1000)
"""
