from django.shortcuts import render
from django.views.generic import DetailView
from filmes.models import Filme
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

class FilmeDetail(DetailView):
    model = Filme
    template_name = 'filmes/detail.html'
   




@login_required(login_url="/account/login")
def home_page(request):
    filmes = reversed  (Filme.objects.all()) 
    return render(request,
    template_name='filmes/home_page.html', context ={'filmes':filmes}
    )

    
@login_required(login_url='/account/login')
def create_new_movie(request):
    from filmes.forms import FilmeForm
    from django.http import HttpResponseRedirect

    if request.method == 'POST':
        #cria um instace do formulário
        filme=FilmeForm(request.POST)
        
        if filme.is_valid():
            filme.save()
            return HttpResponseRedirect(reverse('filmes:home_page'))
        else:
            #os errors que podem ser gerados
            some_errors = {'filme_ja_existe':
                "Filme with this Name already exists.",
                "nota_invalida":'Digite um nota entre 0 a 10.'
            }
            #pega os errors 
            error = filme.errors.as_json()

            #verifica se o motivo do erro é o filme existir
            if some_errors['filme_ja_existe'] in error:

                #recebe o erro
                error = 'Já existe um filme com esse nome'
            if some_errors['nota_invalida'] in error:
                error = 'Digite um nota entre 0 a 10.'

           
            return render(request,
            'filmes/new_movie.html',
            context={'form_errors':error})

            
           

    return render(request,'filmes/new_movie.html')