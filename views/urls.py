from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.sample, name='redirect'),
    path('url-route/', views.urlRoute, name='url-route'),
    path('url-route2/', views.urlRoute2, name='url-route2'),
]