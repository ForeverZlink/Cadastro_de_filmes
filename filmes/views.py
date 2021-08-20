from django.shortcuts import render
from django.views import View
from filmes.models import Filme
from django.shortcuts import reverse
# Create your views here.

def home_page(request):
    filmes = Filme.objects.all()
    return render(request,
    template_name='filmes/home_page.html', context ={'filmes':filmes}
    )

def create_new_movie(request):
    from filmes.forms import FilmeForm
    from django.http import HttpResponseRedirect

    if request.method == 'POST':
        filme=FilmeForm(request.POST)
        if filme.is_valid():
            filme.save()
        return HttpResponseRedirect(reverse('filmes:home_page'))
        

    return render(request,'filmes/new_movie.html')