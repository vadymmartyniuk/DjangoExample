from django import forms

from .models import Lab4


class Lab4CreateForm(forms.ModelForm):
    class Meta:
        model = Lab4
        exclude = ['area1', 'area2', 'area3'] # specifying what fields should be omitted in form