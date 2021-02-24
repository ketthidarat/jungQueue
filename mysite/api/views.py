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
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta, date
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from .models import *
from .utils import Calendar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import make_password

def index(req):
    return render(req, 'api/index.html')

def ownerBase(req):
    return render(req, 'api/ownerBase.html')

# def farmerCalendar(req):
#     return render(req, 'api/farmerCalendar.html')

def register(req):
    print('register()')
    form = FarmerForm()
    print(req)
    if req.method == 'POST':
        form = FarmerForm(req.POST, req.FILES)
        print("req.POST")
        print(req.POST)
        if form.is_valid():
            print('form valid')
            form.instance.password = make_password(req.POST['password'])
            form.save()
        else:
            print("==== form.errors ====")
            print(form.errors)
    return render(req, 'api/register.html', { 
        'form': form,
       
        })

def login(req):
    if req.method == 'POST':
        print(req.POST)
        users = authenticate(username=req.POST['username'], password=req.POST['password'])
        print(users)
        if users is not None:
            print(users)
            auth_login(req, users)
            return redirect('/index')
    else:
        print('ยังไม่ได้กรอก login/password')
    return render(req, 'api/login.html')

def addWork(req):
    if req.method == 'POST':
        print(req.POST)
        form = FarmerWorkForm(req.POST ,req.FILES)
        if form.is_valid():
            form.save()
            # print(form)

            return redirect('/addWork')
    else:
        form = FarmerWorkForm()
    return render(req, 'api/addWork.html',
                  {
                      'form': form,
                      'rice_type': Rice_type.objects.all(),
                    #   'money_status': Money_status.objects.all(),
                    #   'workt_statuss': workt_Status.objects.all(),
                  })

def logout(req):
    # if req.adminn.is_/authenticated:
    auth_logout(req)
    return redirect('/')

def editShowaddWork(request, id=0):
    work = Work.objects.get(pk=id)
    rice_type = Rice_type.objects.all()
    money_status = Money_status.objects.all()
    work_status = Work_status.objects.all()
    if request.method == 'POST':
        form = TractorWorkForm(request.POST, request.FILES, instance=work)
        if form.is_valid():
            form.save()
            # print(form)
            # messages.success(request, 'Member was created successfully!')
            # return redirect('/editproduct/{<int:id>/')
        else:
            print("==== form.errors ====")
            print(form.errors)
    else:
        form = TractorWorkForm(work)
       
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

def deleteShowWork(req, id=0):
    work = Work.objects.get(pk=id)
    # product_types = Product_Type.objects.all()
    # product_statuss = Product_Status.objects.all()
    work.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))

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



# def productpage(request):
#     # list all users.
#     products = Product.objects.all()
#     page_number = request.GET.get('page', 1)
#     paginate_result = do_paginate(products, page_number)
#     product = paginate_result[0]
#     paginator = paginate_result[1]
#     base_url = '/api/product/?'
#     users = Users.objects.get(username=request.user.username)
#     return render(request, 'api/product.html',
#                       {'products': products, 'paginator' : paginator, 'base_url': base_url ,'users':users})
# #ค้นหาสินค้า
# def product(request):
#     product_name = request.POST.get('product_name', '').strip()
#     if len(product_name) == 0:
#         product_name = request.GET.get('product_name', '').strip()
#     product = Product.objects.filter(product_name__contains=product_name)
#     page_number = request.GET.get('page', 1)
#     paginate_result = do_paginate(product, page_number)
#     product = paginate_result[0]
#     paginator = paginate_result[1]
#     base_url = '/api/user_search/?product_name=' + product_name + "&"
#     users = Users.objects.get(username=request.user.username)
#     return render(request, 'api/product.html',
#                       {'product': product, 'paginator' : paginator, 'base_url': base_url, 'search_product_name': product_name,'users':users})

# def do_paginate(data_list, page_number):
#     ret_data_list = data_list
#     #  หน้า มี 5รายการ
#     result_per_page = 5
#     # build the paginator object.
#     paginator = Paginator(data_list, result_per_page)
#     try:
#         # get data list for the specified page_number.
#         ret_data_list = paginator.page(page_number)
#     except EmptyPage:
#         # get the lat page data if the page_number is bigger than last page number.
#         ret_data_list = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         # if the page_number is not an integer then return the first page data.
#         ret_data_list = paginator.page(1)
#     return [ret_data_list, paginator]

class CalendarView(generic.ListView):
    model = Event
    template_name = 'api/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('api:calendar'))
    return render(request, 'api/event.html', {'form': form})












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
