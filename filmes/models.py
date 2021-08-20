from django.db import models

# Create your models here.

class Filme(models.Model):
    name = models.CharField(
        max_length=40, unique=True, blank=False, null=False
        )
    description = models.TextField()
    avaliation = models.DecimalField(decimal_places=1,max_digits=1)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    