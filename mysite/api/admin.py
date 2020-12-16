from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(farmer)
admin.site.register(owner)
admin.site.register(work)
admin.site.register(tractor)
admin.site.register(queue)
