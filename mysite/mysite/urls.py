from django.contrib import admin
from django.urls import path
from api import views
from api.views import router
from django.urls import include, path
from django.utils import translation
from django.conf import settings # new
from django.conf.urls.static import static
from django.conf.urls import url

translation.activate('th')

urlpatterns = [
    path('admin/', admin.site.urls),
     path('index',views.index),
    path('', views.index, name='index'),
    path('login/',views.login),
    path('register/',views.register), 
    path('logout/',views.logout),
    path('addWork',views.addWork),
    path('showWork',views.showWork),
    path('tractor',views.tractor),
    path('addTractor',views.addTractor),
    path('showaddTractor',views.showaddTractor),
    path('profile',views.profile),
    path('profileAdmin',views.profileAdmin),
    path('farmerWork',views.farmerWork),
    path('schedule',views.schedule),
    path('ownerBase',views.ownerBase),
    path('ownerShowaddWork',views.ownerShowaddWork),
    path('editShowaddWork/<int:id>/',views.editShowaddWork),
    path('editShowWork/<int:id>/',views.editShowWork),
    path('deleteShowaddWork/<int:id>', views.deleteShowaddWork),
    path('addShowaddTractor/<int:id>/',views.addTractor),
    path('editShowaddTractor/<int:id>/',views.editShowaddTractor),
    path('editProfile/<int:id>/',views.editProfile),
    path('deleteShowaddTractor/<int:id>', views.deleteShowaddTractor),
    path('ownerShowaddTractor',views.ownerShowaddTractor),
    path('deleteShowWork/<int:id>', views.deleteShowWork),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('cal/', include('api.urls')),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)