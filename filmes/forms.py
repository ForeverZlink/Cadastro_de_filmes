from django.forms import ModelForm
from filmes.models import Filme

class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = ['user','name',
            'description','avaliation',
            'visto'

        ]
    def search_errors(self) -> str:
        some_errors = {'filme_ja_existe':
                "Filme with this Name already exists.",
                "nota_invalida":'Digite um nota entre 0 a 10.'
            }
        #pega os errors 
        error = self.errors.as_json()
        #verifica se o motivo do erro é o filme existir
        if some_errors['filme_ja_existe'] in error:
            #recebe o erro
            error = 'Já existe um filme com esse nome'
        if some_errors['nota_invalida'] in error:
            error = 'Digite um nota entre 0 a 10.'

        return error