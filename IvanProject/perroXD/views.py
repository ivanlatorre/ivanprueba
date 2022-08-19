from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render , HttpResponse

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView , CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy

class Inicio(ListView):
    template_name = 'inicio.html'
    ordering = ['-created_date']
