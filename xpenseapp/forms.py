from django import forms
from .models import Account, Goal


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('balance',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['balance'].widget.attrs['step'] = '0.01'
        self.fields['balance'].widget.attrs['placeholder'] = 'P0.00'


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'timeline', 'required_savings', 'progress', 'complete']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Goal Name'}),
            'timeline': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'required_savings': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Required Savings'}),
            'progress': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Progress Percentage'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
