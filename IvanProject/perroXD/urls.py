from django.urls import path
from .views import Inicio
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
path('',Inicio.as_view(), name ='inicio'),
]

urlpatterns += staticfiles_urlpatterns()