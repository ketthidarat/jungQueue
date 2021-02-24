from django.contrib import admin
from django.urls import path
from api import views
from api.views import router
from django.urls import include, path
from django.utils import translation

translation.activate('th')

urlpatterns = [
    path('admin/', admin.site.urls),
     path('index',views.index),
    path('', views.login, name='login'),
    path('login/',views.login),
    path('register/',views.register), 
    path('logout/',views.logout),
    path('addWork',views.addWork),
    path('showWork',views.showWork),
    path('tractor',views.tractor),
    path('addTractor',views.addTractor),
    path('showaddTractor',views.showaddTractor),
    # path('FarmerCalendarView',views.FarmerCalendarView),
    # path('farmerCalendar',views.farmerCalendar),
    path('ownerBase',views.ownerBase),
    path('ownerShowaddWork',views.ownerShowaddWork),
    path('editShowaddWork/<int:id>/',views.editShowaddWork),
    path('deleteShowaddWork/<int:id>', views.deleteShowaddWork),
    path('addShowaddTractor/<int:id>/',views.addTractor),
    path('editShowaddTractor/<int:id>/',views.editShowaddTractor),
    path('deleteShowaddTractor/<int:id>', views.deleteShowaddTractor),
    path('ownerShowaddTractor',views.ownerShowaddTractor),
    path('deleteShowWork/<int:id>', views.deleteShowWork),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('cal/', include('api.urls')),

]
