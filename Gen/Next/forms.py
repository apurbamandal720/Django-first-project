from django import forms  
from .models import *

class BannerForm(forms.ModelForm): 
  
    class Meta: 
        model = Banner 
        fields = ['name', 'banner_image'] 