from django import forms
from django.forms import DateInput
from .models import *

class FarmerForm(forms.ModelForm):
    # quantity = forms.IntegerField(initial='1')
    # farmer_id = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Farmer 
        fields = [ 'farmer_name' ,'image', 'address', 'phone','email', 'username','password' ]

class OwnerForm(forms.ModelForm):

    class Meta:
        model = Owner 
        fields = [ 'owner_name' ,'image', 'address', 'phone','email', 'username','password', ]

class EditFarmerForm(forms.ModelForm):

    class Meta:
        model = Farmer 
        fields = [ 'farmer_name' ,'image',  'address', 'phone','email' ]

class TractorWorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = [ 'start_time', 'price', 'money_status', 'work_status' ]

class FarmerWorkForm(forms.ModelForm):
    class Meta:
        model = Work
        # fields = '__all__'
        fields = [ 'area', 'rice_type', 'rice', 'workDetail' ]

class TractorForm(forms.ModelForm):

    class Meta:
        model = AddTractor
        fields = '__all__'


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
  
class ProfileDetailFrom(forms.ModelForm):
   
        model = Farmer
        fields = '__all__'