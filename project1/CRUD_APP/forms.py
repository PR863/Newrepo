from django import forms
from .models import Custumor

class CustumerForm(forms.ModelForm):
    class Meta:
        model = Custumor
        fields = '__all__'