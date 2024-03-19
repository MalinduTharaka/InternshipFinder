from django import forms
from dash.models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
