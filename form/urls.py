from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='form-index'),
    path('validate/', views.Validate.as_view())
]
