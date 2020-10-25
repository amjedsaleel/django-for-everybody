from django.db.transaction import commit
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from forums.forms import CommentForm
from forums.models import Forum, Comment
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

# Create your views here.


class ForumListView(ListView):
    model = Forum
    template_name = 'forums/list.html'
    context_object_name = 'forum_list'


class ForumDetailView(DetailView):
    model = Forum
    template_name = 'forums/detail.html'
    # context_object_name = 'detail'

    def get(self, request, pk):
        forum = Forum.objects.get(id=pk)
        comments = Comment.objects.filter(forum=forum).order_by('-updated_at')
        comment_form = CommentForm()
        context = {'forum': forum, 'comments': comments, 'comment_form': comment_form}
        return render(request, self.template_name, context)


class ForumCreateView(LoginRequiredMixin, CreateView):
    model = Forum
    fields = ['title', 'text']
    template_name = 'forums/form.html'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(ForumCreateView, self).form_valid(form)


class ForumUpdateView(OwnerUpdateView):
    model = Forum
    fields = ['title', 'text']
    template_name = 'forums/form.html'


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Forum, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, forum=f)
        comment.save()
        return redirect(reverse('forums:forum_detail', args=[pk]))
