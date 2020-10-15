from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    path('lookup/create', views.MakeCreate.as_view(), name='make_create')
]