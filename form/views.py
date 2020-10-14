from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .forms import BasicForm

# Create your views here.

def index(request):
    old_data = {
        'title': 'Amjed',
        'mileage': 42,
        'purchase_date': '2018-08-7'
    }
    form = BasicForm(old_data)
    context = {
        'form': form
    }
    return render(request, 'forms.html', context)