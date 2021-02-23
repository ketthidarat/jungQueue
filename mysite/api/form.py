from django import forms
from django.forms import DateInput
from .models import *

 
class TractorWorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = '__all__'

class FarmerWorkForm(forms.ModelForm):
    class Meta:
        model = Work
        # fields = '__all__'
        fields = [ 'area', 'rice_type', 'rice', 'workDetail' ]

class TractorForm(forms.ModelForm):

    class Meta:
        model = AddTractor
        fields = '__all__'

        # fields = [  'product_name','product_price', 'product_detail', 'product_img','product_type','product_status','product_amount' ]

class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


# class MechanicForm(forms.ModelForm):
#     class Meta:
#         model = Mechanic
#         fields = '__all__'


# class Order_ProductForm(forms.ModelForm):
#     class Meta:
#         model = Order_Product
#         fields = '__all__'

# class StorckForm(forms.ModelForm):
#     class Meta:
#         model = Storck
#         fields = '__all__'