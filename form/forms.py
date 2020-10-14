from django import forms
import django
from django.core.exceptions import ValidationError
from django.core import validators

class BasicForm(forms.Form):
    title = forms.CharField(validators=[
        validators.MinLengthValidator(2 ,'Please enter 2 or more')
    ])
    mileage = forms.IntegerField()
    purchase_date = forms.DateField()

    