from django.test import TestCase
from django.contrib.auth.models import User
from filmes.models import Filme
from datetime import datetime
# Create your tests here.
class TestQueries (TestCase):
    @classmethod
    def setUp(self):
        self.filme = Filme
        self.user = User.objects.create_user(username='carlos',password='123')

    def test_criar_filme(self):
        hora_date = datetime.now()
        self.filme.objects.create(
            user=self.user,name='ola',description='zen'
            ,avaliation=3.1,date_of_creation=hora_date
            )
        