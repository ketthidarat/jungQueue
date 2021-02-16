from django import forms
from .models import *

 
class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = [ 'area', 'rice_type', 'rice', 'workDetail' ]
        # fields = '__all__'

class TractorForm(forms.ModelForm):
    class Meta:
        model = AddTractor
        fields = '__all__'
        # fields = [  'product_name','product_price', 'product_detail', 'product_img','product_type','product_status','product_amount' ]


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