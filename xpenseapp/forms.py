
from django import forms
from .models import Account

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('balance',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['balance'].widget.attrs['step'] = '0.01'
        self.fields['balance'].widget.attrs['placeholder'] = 'P0.00'