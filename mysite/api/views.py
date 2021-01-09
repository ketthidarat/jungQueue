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

class TractorViewSet(viewsets.ModelViewSet):
    queryset = Tractor.objects.all()
    serializer_class = TractorSerializer

# class RiceTypeViewSet(viewsets.ModelViewSet):
#     queryset = Rice_type.objects.all()
#     serializer_class = RiceTypeSerializer

# class TractorStatusViewSet(viewsets.ModelViewSet):
#     queryset = Tractor_status.objects.all()
#     serializer_class = TractorStatusSerializer

# class MoneyStatusViewSet(viewsets.ModelViewSet):
#     queryset = Money_status.objects.all()
#     serializer_class = MoneyStatusSerializer


# class WorkStatusViewSet(viewsets.ModelViewSet):
#     queryset = Work_status.objects.all()
#     serializer_class = WorkStatusSerializer

# class WorkViewSet(viewsets.ModelViewSet):
#     queryset = Work.objects.all()
#     serializer_class = WorkSerializer

router = routers.DefaultRouter()
router.register(r'farmer', FarmerViewSet)
router.register(r'owner', OwnerViewSet)
router.register(r'tractor', TractorViewSet)
# router.register(r'ricetypestatus', RiceTypeViewSet)
# router.register(r'tractorstatus', TractorStatusViewSet)
# router.register(r'moneystatus', MoneyStatusViewSet)
# router.register(r'workstatus', WorkStatusViewSet)
# router.register(r'work', WorkViewSet)

def index(request):
      translation.activate('th')
      return HttpResponse("<h1>JungQueue</h1>")
# Create your views here.
