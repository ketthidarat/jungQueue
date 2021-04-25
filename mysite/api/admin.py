from django.contrib import admin
# from django.contrib.gis.admin import OSMGeoAdmin
from .models import *

# Register your models here.
admin.site.register(Farmer)
# admin.site.register(Owner)
admin.site.register(Work)
# admin.site.register(Tractor)
admin.site.register(Tractor_status)
admin.site.register(Work_status)
admin.site.register(Money_status)
admin.site.register(Rice_type)
admin.site.register(AddTractor)
admin.site.register(Event)

# @admin.register(Shop)
# class ShopAdmin(OSMGeoAdmin):
#     list_display = ('farmer_name', 'location')
