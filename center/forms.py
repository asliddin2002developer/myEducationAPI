from django import forms
 
from .models import Center

class CenterRegistration(forms.ModelForm):
    class Meta:
        models = Center
        fields = '__all__'