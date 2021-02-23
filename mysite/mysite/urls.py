"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('', views.index, name='index'),
    # path('login/',views.login),
    # path('register/',views.register), 
    # path('logout/',views.logout),
    path('addWork',views.addWork),
    path('showWork',views.showWork),
    path('tractor',views.tractor),
    path('addTractor',views.addTractor),
    path('showaddTractor',views.showaddTractor),
    path('schedule',views.schedule),
    path('ownerBase',views.ownerBase),
    path('ownerShowaddWork',views.ownerShowaddWork),
    path('editShowaddWork/<int:id>/',views.editShowaddWork),
    path('deleteShowaddWork/<int:id>', views.deleteShowaddWork),
    path('addShowaddTractor/<int:id>/',views.addTractor),
    path('editShowaddTractor/<int:id>/',views.editShowaddTractor),
    path('deleteShowaddTractor/<int:id>', views.deleteShowaddTractor),
    path('ownerShowaddTractor',views.ownerShowaddTractor),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('calendar', include('api.urls')),
]
