from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape
from django.views import View

# Create your views here.

def index(request):
    # response = """<h1>Hello""" + escape(request.GET['hello'])
    # print(parameter)
    return HttpResponse('helo')


def sample(request):
    return HttpResponseRedirect("https://www.google.com")


def urlRoute(request):
    # print(escape(request.GET['hello']))
    return render(request, 'url_route.html')


def urlRoute2(request):
    return render(request, 'url_route2.html')



