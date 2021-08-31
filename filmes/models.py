from django.db import models
from django.contrib.auth.models import User
from filmes.validators import validade_if_the_note_is_valid
# Create your models here.

    
class Filme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=40, unique=True, blank=False, null=False
        )
    description = models.TextField(default=None)
    avaliation = models.FloatField(default=0,null=True,validators=[validade_if_the_note_is_valid])
    visto = models.BooleanField(default=False)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
    

    