from django.urls import path

from .import views

urlpatterns = [
	path('', views.index, name='index'),
	path('owner/', views.owner, name='owner'),
	path('1/', views.vote, name='vote'),
	path('1/results/', views.results, name='results'),
]