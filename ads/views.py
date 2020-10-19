from django.shortcuts import render
from django.urls import reverse_lazy

from .owner import OwnerListView, OwnerCreateView, OwnerDetailView, OwnerUpdateView, OwnerDeleteView
from .models import Ad

# Create your views here.


class AdListView(OwnerListView):
    model = Ad
    template_name = 'ads/ad_list.html'


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreate(OwnerCreateView):
    model = Ad
    template_name = 'ads/ad_form.html'
    fields = ['title', 'price', 'text']
    success_url = reverse_lazy('ads:all')


class AdUpdateView(OwnerUpdateView):
    model = Ad
    template_name = 'ads/ad_form.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('ads:all')


class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = 'ads/ad_confirm_delete.html'
    success_url = reverse_lazy('ads:all')
