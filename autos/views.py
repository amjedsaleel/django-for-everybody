from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from autos.models import Make, Auto
from autos.forms import MakeForm

# Create your views here.


def index(request):
    return HttpResponse('hello')


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        makes_count = Make.objects.all().count()
        autos = Auto.objects.all()
        context = {
            'makes_count': makes_count,
            'autos': autos
        }
        return render(request, 'autos/auto_list.html', context)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        makes = Make.objects.all()
        context = {'makes': makes}
        return render(request, 'autos/make_list.html', context)


class MakeCreate(LoginRequiredMixin, View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('all')

    def get(self, request):
        form = MakeForm()
        context = {'form':form}
        return render(request, self.template, context)

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)

        form = form.save()
        return redirect(self.success_url)


class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    template = 'autos/make_form.html'
    success_url = reverse_lazy('all')

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        context = {
            'form': form
        }
        return render(request, self.template, context)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template, context)

        form = form.save()
        return redirect(self.success_url)


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('all')
