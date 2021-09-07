from django.http import request
from django.test import TestCase
from django.contrib.auth.models import User
from filmes.models import Filme
from filmes.forms import FilmeForm
from datetime import datetime
from django.shortcuts import reverse
# Create your tests here.
class TestQueriesFilme (TestCase):
    @classmethod
    def setUp(self):
        self.hora_date = datetime.now()
        self.filme = Filme
        self.user = User.objects.create_user(username='carlos',password='123')

    def test_criar_filme(self):
        self.filme.objects.create(
            user=self.user,name='ola',description='zen'
            ,avaliation=3.1,date_of_creation=self.hora_date
            )
    def test_create_new_film_in_page(self):
        self.client.login(username= 'carlos',password='123')
        url='/create_new_movie/'
        responser=self.client.post(url,{'user':self.user.pk,'name':'ola','description':'zen'
            ,"avaliation":3.1}
            )
        
        responser=self.client.post(url,{'user':self.user.pk,'name':'ola','description':'zen'
            ,"avaliation":3.1}
            )
        
        print(Filme.objects.all())
        print(responser)
    
    def test_update_film(self):
        
        self.filme.objects.create(
            user=self.user,name='ola',description='zen'
            ,avaliation=3.1,date_of_creation=self.hora_date
            )
        filmes = self.filme.objects.all()
        print(filmes)
        filme_for_update=self.filme.objects.get(pk=1).name
        print(filme_for_update)
        url = reverse('filmes:detail_or_update_film',args=(1,))
    
        print(url)
    
        responser=self.client.post(url,{
            'user':self.user.pk,'name':'carlos',"description":'zonn',
            'avaliation':1.1
            })
        filmes_already_update=self.filme.objects.get(pk=1).name
        print(filmes_already_update)
        self.assertNotEqual(filme_for_update,filmes_already_update)
        
        

        


    def test_if_filme_already_exist(self):
        
        self.filme.objects.create(
            user=self.user,name='ola',description='zen'
            ,avaliation=3.1,date_of_creation=self.hora_date
            )
        
        self.filme.objects.create(
            user=self.user,name='zne',description='dkjn'
            ,avaliation=2.1,date_of_creation=self.hora_date
          )  
        

        
        
        
    
    

    
class TestFilmePagesWorks(TestCase):
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(username='carlos',password='123')

    def test_If_home_page_works(self):
        self.client.login(username= 'carlos',password='123')
        url = '//'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_if_new_movie_page_works(self):
        self.client.login(username= 'carlos',password='123')
        url = '/create_new_movie/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code,200)

    def test_detail_or_update_film_page_works(self):
        hora_date = datetime.now()
        
        Filme.objects.create(
            user=self.user,name='ola',description='zen'
            ,avaliation=3.1,date_of_creation=hora_date
            )
        
        url = reverse('filmes:detail_or_update_film',args=(1,))
        
        response =self.client.get(url)
        
        self.assertEqual(response.status_code,200)
    
        
    
