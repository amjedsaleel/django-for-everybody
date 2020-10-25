from django.urls import path

from . import views

app_name = 'forums'

urlpatterns = [
    path('', views.ForumListView.as_view(), name='all'),
    path('forum/<int:pk>', views.ForumDetailView.as_view(), name='forum_detail')
]