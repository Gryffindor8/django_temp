from django import forms
from .models import *


class CreateTransactionForm(forms.ModelForm):
    class Meta:
        model = transaction
        exclude = ('is_active',)
        widgets = {
            'file': forms.HiddenInput(),
            'assigned_to': forms.Select({'label': 'Assign To:', }),
        }


class CreateFile(forms.ModelForm):
    class Meta:
        model = files
        fields = '__all__'
