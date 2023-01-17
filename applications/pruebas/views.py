from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .models import Prueba
from .forms import PruebaForm


class IndexView(TemplateView):
    template_name = 'pruebas/home.html'


class List(ListView):
    template_name = 'pruebas/listar.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'obj'


class ListaPrueba(ListView):
    model = Prueba
    template_name = "pruebas/listaPrueba.html"
    context_object_name = 'obj'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "pruebas/crear.html"
    form_class = PruebaForm
    success_url = '.'

    




