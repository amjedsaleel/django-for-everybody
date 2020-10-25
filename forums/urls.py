from django.urls import path, reverse_lazy

from . import views

app_name = 'forums'

urlpatterns = [
    path('', views.ForumListView.as_view(), name='all'),
    path('forum/<int:pk>', views.ForumDetailView.as_view(), name='forum_detail'),
    path('create', views.ForumCreateView.as_view(success_url=reverse_lazy('forums:all')), name='forum_create'),
    path('forum/<int:pk>/update',
         views.ForumUpdateView.as_view(success_url=reverse_lazy('forums:all')), name='forum_update'),
]
