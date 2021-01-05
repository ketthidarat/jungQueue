from django.shortcuts import render
from django.http import HttpResponse
from django.utils import translation
from rest_framework import routers, serializers, viewsets
from .models import *
from .serializers import *

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class TractorStatusViewSet(viewsets.ModelViewSet):
    queryset = Tractor_status.objects.all()
    serializer_class = TractorStatusSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

router = routers.DefaultRouter()
router.register(r'farmer', FarmerViewSet)
router.register(r'owner', OwnerViewSet)
router.register(r'tractorstatus', TractorStatusViewSet)
router.register(r'work', WorkViewSet)

def index(request):
      translation.activate('th')
      return HttpResponse("<h1>JungQueue</h1>")
# Create your views here.
