from django.urls import path
from filmes.views import home_page

app_name='filmes'
urlpatterns = [
    path('home_page/',home_page, name='home_page')
]
