from http.client import HTTPResponse
from django.shortcuts import render , HttpResponse
from django.views.generic import ListView, DetailView, TemplateView , CreateView , UpdateView, DeleteView

# Create your views here.

class inicio(TemplateView):
    template_name = 'inicio.html'
    
class juanapag(TemplateView):
    template_name = 'juana.html'

class lobo(TemplateView):
    template_name = 'lobito.html'

