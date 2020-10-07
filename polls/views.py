from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	return render(request, 'polls4.html')


def owner(request):
	return render(request, 'owner.html')


def vote(request):
	return render(request, 'vote.html')


def results(request):
	return render(request, 'vote_result.html')