from django.shortcuts import render
from django.views import View
from filmes.models import Filme
# Create your views here.

def home_page(request):
    filmes = Filme.objects.all()
    return render(request,
    template_name='filmes/home_page.html', context ={'filmes':filmes}
    )

def create_new_movie(request):

    return render(request,'filmes/new_movie.html')