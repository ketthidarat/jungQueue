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
    #  path('index',views.index),
    path('', views.work, name='work'),
    path('work',views.work),
    path('showWork',views.showWork),
    path('tractor',views.tractor),
    path('addTractor',views.addTractor),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
