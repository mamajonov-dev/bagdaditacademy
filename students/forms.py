from django import forms
from .models import *


class SudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'address', 'phone', 'birthday', 'course']

    def __init__(self, *args, **kwargs):
        super(SudentForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'note', 'sale', 'payment_check']

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )
