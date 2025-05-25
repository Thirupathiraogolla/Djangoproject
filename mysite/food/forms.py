from django import forms
from .models import items
class item_form(forms.ModelForm):
    class Meta:
        model = items
        fields = ['id','item_name','item_desc','item_price','item_image'] 
