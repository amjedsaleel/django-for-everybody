from django.urls import path, reverse_lazy

from . import views

app_name = 'myarts'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),
    path('ads/<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('ads/create', views.AdCreate.as_view(), name='ad_create'),
    path('ads/<int:pk>/update', views.AdUpdateView.as_view(), name='ad_update'),
    path('ads/<int:pk>/delete', views.AdDeleteView.as_view(), name='ad_delete')
]