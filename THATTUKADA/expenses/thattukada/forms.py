from django import forms
from .models import Expenses
from django.conf import settings


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        exclude = ('balance',)
        date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date' ,'id': 'datefield'})
        }