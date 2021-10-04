from django.forms.forms import Form
from django.http import request
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import DetailView
from filmes.models import Filme
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from filmes.forms import FilmeForm, UserForm
from django.contrib.auth.models import User

# Create your views here.

def create_user(request):
    if request.method == 'POST':
        user = request.POST
        
        usuario = User.objects.create_user(username=user['username'],
                 password=user['password'],email=user['email']
                )
        usuario.save()
        return HttpResponseRedirect(reverse("login"))
    
    return  render (request, template_name="filmes/create_user.html")
        
        



def delete_film(request,pk):
    
    filme=Filme.objects.get(pk=pk)
    filme.delete()
    return HttpResponseRedirect(reverse("filmes:home_page"))



def film_detail_or_update(request,pk):
    filme=Filme.objects.get(pk=pk)
    
    if request.method == "POST":
        #ATUALIZA A INSTANCIA
        filme_updated=FilmeForm(request.POST,instance=filme)
        if filme_updated.is_valid():
            filme_updated.save()
            return HttpResponseRedirect(reverse('filmes:home_page'))
           

            
        else:
            error=filme_updated.search_errors()
            return render(request,'filmes/detail_or_update.html',
                context={"form_errors":error,'filme':filme}
                )



    return render(request,'filmes/detail_or_update.html',
        context={'filme':filme}
        )
    
   




@login_required(login_url="/account/login")
def home_page(request):
    filmes = reversed  (Filme.objects.all()) 
    return render(request,
    template_name='filmes/home_page.html', context ={'filmes':filmes}
    )

    
@login_required(login_url='/account/login')
def create_new_movie(request):
    
    from django.http import HttpResponseRedirect

    if request.method == 'POST' :
        #cria uma instanci ado formulário
        filme=FilmeForm(request.POST)
        
        if filme.is_valid():
            filme.save()
            return HttpResponseRedirect(reverse('filmes:home_page'))
        else:
            error = filme.search_errors()
            return render(request,
            'filmes/new_movie.html',
            context={'form_errors':error})

            
           

    return render(request,'filmes/new_movie.html')