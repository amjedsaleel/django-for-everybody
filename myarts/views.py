from django.shortcuts import render
from django.urls import reverse_lazy

from .owner import OwnerListView, OwnerCreateView, OwnerDetailView, OwnerUpdateView, OwnerDeleteView
from .models import Article

# Create your views here.


class ArticleListView(OwnerListView):
    model = Article
    template_name = 'myarts/article_list.html'


class ArticleDetailView(OwnerDetailView):
    model = Article


class ArticleCreate(OwnerCreateView):
    model = Article
    template_name = 'myarts/article_form.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('myarts:all')


class ArticleUpdateView(OwnerUpdateView):
    model = Article
    template_name = 'myarts/article_form.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('myarts:all')


class ArticleDeleteView(OwnerDeleteView):
    model = Article
    template_name = 'myarts/article_confirm_delete.html'
    success_url = reverse_lazy('myarts:all')
