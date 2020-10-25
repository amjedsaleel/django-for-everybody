from django.db.transaction import commit
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from forums.models import Forum, Comment

# Create your views here.


class ForumListView(ListView):
    model = Forum
    template_name = 'forums/list.html'
    context_object_name = 'forum_list'


class ForumDetailView(DetailView):
    model = Forum
    template_name = 'forums/detail.html'
    # context_object_name = 'detail'


class ForumCreateView(LoginRequiredMixin, CreateView):
    model = Forum
    fields = ['title', 'text']
    template_name = 'forums/form.html'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(ForumCreateView, self).form_valid(form)
