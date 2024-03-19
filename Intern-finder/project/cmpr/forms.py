from django import forms
from dash.models import company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = '__all__'
