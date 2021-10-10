from django.shortcuts import render
from django.views.generic import templateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
