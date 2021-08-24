from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class Filme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=40, unique=True, blank=False, null=False
        )
    description = models.TextField()
    avaliation = models.FloatField()
    visto = models.BooleanField(default=False)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

    