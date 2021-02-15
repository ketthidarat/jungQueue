from api.form import *
from django.http import HttpResponse
# from django.utils import translation
from .models import *
from .serializers import *
from django.core.checks import messages
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

def index(req):
    return render(req, 'api/index.html')

def work(request):
    if request.method == 'POST':
        form = WorkForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/work')
    else:
        form = WorkForm()
    return render(request, 'api/work.html',
                  {
                      'form': form,
                      'rice_type': Rice_type.objects.all(),
                    #   'workt_statuss': workt_Status.objects.all(),

                  }) 

def showWork(req):
    showWork = Work.objects.all() 
    return render(req, 'api/showWork.html', {
        'showWork': showWork,
    })

def tractor(req):
    tractor = Tractor.objects.all() 
    return render(req, 'api/tractor.html', {
        'tractor': tractor,
    })

def addTractor(request):
    if request.method == 'POST':
        form = TractorForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/addTractor')
    else:
        form = TractorForm()
    return render(request, 'api/addTractor.html',
                  {
                      'form': form,
                      'tractor_status': Tractor_status.objects.all(),
                    

                  }) 
# def tractor_status(req):
#     tractor_status = Tractor_status.objects.all() 
#     return render(req, 'api/tractor.html', {
#         'tractor_status': tractor_status,
#     })

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class TractorViewSet(viewsets.ModelViewSet):
    queryset = Tractor.objects.all()
    serializer_class = TractorSerializer

class RiceTypeViewSet(viewsets.ModelViewSet):
    queryset = Rice_type.objects.all()
    serializer_class = RiceTypeSerializer

class TractorStatusViewSet(viewsets.ModelViewSet):
    queryset = Tractor_status.objects.all()
    serializer_class = TractorStatusSerializer

class MoneyStatusViewSet(viewsets.ModelViewSet):
    queryset = Money_status.objects.all()
    serializer_class = MoneyStatusSerializer


class WorkStatusViewSet(viewsets.ModelViewSet):
    queryset = Work_status.objects.all()
    serializer_class = WorkStatusSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

router = routers.DefaultRouter()
router.register(r'farmer', FarmerViewSet)
router.register(r'owner', OwnerViewSet)
router.register(r'tractor', TractorViewSet)
router.register(r'ricetype', RiceTypeViewSet)
router.register(r'tractorstatus', TractorStatusViewSet)
router.register(r'moneystatus', MoneyStatusViewSet)
router.register(r'workstatus', WorkStatusViewSet)
router.register(r'work', WorkViewSet)

# def index(request):
#       translation.activate('th')
#       return HttpResponse("<h1>JungQueue</h1>")
# Create your views here.
