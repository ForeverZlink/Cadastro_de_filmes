from django.test import TestCase
from django.contrib.auth.models import User
from filmes.models import Filme
from filmes.forms import FilmeForm
from datetime import datetime
# Create your tests here.
class TestQueriesFilme (TestCase):
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
    def test_create_new_film(self):
        url='/create_new_movie/'
        responser=self.client.post(url,{'user':self.user.pk,'name':'ola','description':'zen'
            ,"avaliation":3.1}
            )
        print(Filme.objects.all())
        print(responser)

    
class TestFilmePagesWorks(TestCase):
    def test_If_home_page_works(self):
        url = '/home_page/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_if_new_movie_page_works(self):
        url = '/create_new_movie/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        
