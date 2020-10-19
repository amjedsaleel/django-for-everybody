from django.urls import path
from django.views.generic import TemplateView

app_name = 'ads'

urlpatterns = [
    path('', TemplateView.as_view(template_name='base_bootstrap.html'))
]
