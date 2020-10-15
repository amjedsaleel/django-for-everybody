from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .forms import BasicForm
from django.views import View

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


class Validate(View):
    def get(self, request):
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(initial=old_data)
        context = {'form' : form}
        return render(request, 'form2.html', context)

