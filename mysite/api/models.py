from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Farmer(AbstractUser):
    id = models.AutoField(primary_key=True) 
    # farmer_id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=1000, verbose_name = 'ชื่อ-สกุล')
    # farmer_lastname = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/farmer',verbose_name = 'รูปโปรไฟล์')
    address = models.CharField(max_length=1000, verbose_name = 'ที่อยู่')
    phone = models.CharField(max_length=1000, verbose_name = 'เบอร์โทรศัพท์')
    email = models.CharField(max_length=1000)
    # username = models.CharField(max_length=1000)
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
    farmer_name = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=True,  verbose_name='เกษตรกร')
    # farmer_lastname = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    # tractor = models.ForeignKey(Tractor, on_delete=models.CASCADE, null=True,  verbose_name='รถเกี่ยวนวดข้าว')
    # work_id = models.AutoField(primary_key=True)
    # work_status = models.CharField(max_length=1000)
    lat = models.CharField(max_length=1000, verbose_name='ละติจูด')
    lng = models.CharField(max_length=1000, verbose_name='ลองติจูด')
    area = models.CharField(max_length=1000, verbose_name='พื้นที่ (ไร่)')
    rice_type = models.ForeignKey(Rice_type, on_delete=models.CASCADE, null=True, default=1, verbose_name='ลักษณะข้าวที่จะให้เกี่ยว')
    rice = models.CharField(max_length=1000, null=True, verbose_name='พันธุ์ข้าว') 
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    workDetail = models.TextField(max_length=1000, null=True,  verbose_name='รายละเอียด')
    price = models.CharField(max_length=1000, null=True, verbose_name='จำนวนเงิน (บาท)')
    money_status = models.ForeignKey(Money_status, on_delete=models.CASCADE, default=1,null=True, verbose_name='สถานะการชำระเงิน') # ให้นิยามเพิ่มเติม
    work_status = models.ForeignKey(Work_status, on_delete=models.CASCADE, default=1,null=True, verbose_name='สถานะงาน') # รับ ไม่รับ จ่าย

    def __str__(self):
         return f'{self.area} {self.rice_type} {self.rice}'

    class Meta:
        verbose_name = 'งานที่ต้องเก็บเกี่ยว'

class AddTractor(models.Model):
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

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('api:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'ตารางงานรถเกี่ยวนวดข้าว'