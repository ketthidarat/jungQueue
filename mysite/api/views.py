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

def schedule(req):
    return render(req, 'api/schedule.html')

def ownerBase(req):
    return render(req, 'api/ownerBase.html')

def addWork(req):
    if req.method == 'POST':
        form = WorkForm(req.POST ,req.FILES)
        if form.is_valid():
            form.save()
            return redirect('/addWork')
    else:
        form = WorkForm()
    return render(req, 'api/addWork.html',
                  {
                      'form': form,
                      'rice_type': Rice_type.objects.all(),
                    #   'money_status': Money_status.objects.all(),
                    #   'workt_statuss': workt_Status.objects.all(),

                  })

def editShowaddWork(request, id=0):
    print(f'/editShowAddWork id={id}')
    work = Work.objects.get(pk=id)
    rice_type = Rice_type.objects.all()
    money_status = Money_status.objects.all()
    work_status = Work_status.objects.all()
    if request.method == 'POST':
        print(request.POST)
        form = FarmerWorkForm(request.POST, request.FILES, instance=work)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            work = form.instance
            print(work)
            # messages.success(request, 'Member was created successfully!')
            # return redirect('/editproduct/{<int:id>/')
        else:
            print("==== form.errors ====")
            print(form.errors)
    else:
        form = FarmerWorkForm(work)
       
    return render(request, 'api/editShowaddWork.html' ,{ 
        'form': form,
        'work': work,
        'rice_type': rice_type,
        'money_status': money_status,
        'work_status': work_status,
        # 'product_statuss': product_statuss,
    })

def deleteShowaddWork(req, id=0):
    work = Work.objects.get(pk=id)
    # product_types = Product_Type.objects.all()
    # product_statuss = Product_Status.objects.all()
    work.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

def ownerShowaddWork(req):
    ownerShowaddWork = Work.objects.all() 
    return render(req, 'api/ownerShowaddWork.html', {
        'ownerShowaddWork': ownerShowaddWork,
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
def showaddTractor(req):
    showaddTractor = AddTractor.objects.all() 
    return render(req, 'api/showaddTractor.html', {
        'showaddTractor': showaddTractor,
    })

def ownerShowaddTractor(req):
    ownerShowaddTractor = AddTractor.objects.all() 
    return render(req, 'api/ownerShowaddTractor.html', {
        'ownerShowaddTractor': ownerShowaddTractor,
    })


def editShowaddTractor(request, id=0):
    addTractor = AddTractor.objects.get(pk=id)
    tractor_status = Tractor_status.objects.all()
    # product_statuss = Product_Status.objects.all()
    if request.method == 'POST':
        form = TractorForm(request.POST, request.FILES, instance=addTractor)
        if form.is_valid():
            
            form.save()
            # messages.success(request, 'Member was created successfully!')
            # return redirect('/editproduct/{<int:id>/')
        else:
            print("==== form.errors ====")
            print(form.errors)
    else:
        form = TractorForm(addTractor)
       
    return render(request, 'api/editShowaddTractor.html' ,{ 
        'form': form,
        'addTractor': addTractor,
        'tractor_status': tractor_status,
        # 'product_types': product_types,
        # 'product_statuss': product_statuss,
    })

def deleteShowaddTractor(req, id=0):
    addTractor = AddTractor.objects.get(pk=id)
    addTractor.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))






























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
