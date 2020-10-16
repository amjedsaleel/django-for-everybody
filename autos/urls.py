from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    path('lookup/create', views.MakeCreate.as_view(), name='make_create'),
    path('lookup/<int:pk>/update', views.MakeUpdate.as_view(), name='make_update'),
    path('lookup/<int:pk>/delete', views.MakeDelete.as_view(), name='make_delete')
]