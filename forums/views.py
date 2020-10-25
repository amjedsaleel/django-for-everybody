from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from forums.models import Forum, Comment

# Create your views here.


class ForumListView(ListView):
    model = Forum
    template_name = 'forums/list.html'
    context_object_name = 'forum_list'

