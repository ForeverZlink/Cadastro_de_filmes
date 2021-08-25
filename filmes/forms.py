from django.forms import ModelForm
from filmes.models import Filme

class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = ['user','name',
            'description','avaliation',
            'visto'

        ]
