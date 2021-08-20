from django.shortcuts import render
from django.views import View
# Create your views here.

def home_page(request):
    return render(request,template_name='filmes/home_page.html')