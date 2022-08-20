from django.urls import path
from .views import juanapag, lobo, inicio
from django.views.generic import ListView, DetailView, TemplateView , CreateView , UpdateView, DeleteView

urlpatterns = [

    path('',inicio.as_view(), name= 'inicio'),
    path('juanii',juanapag.as_view(), name= 'juani'),
    path('lobitoo',lobo.as_view(), name= 'lobito'),

] 
