from django.urls import path
from filmes.views import home_page, create_new_movie, film_detail_or_update

app_name='filmes'
urlpatterns = [
    path('',home_page, name='home_page'),
    path('create_new_movie/',create_new_movie,name='new_movie'),
    path('detail_movie/<int:pk>/',film_detail_or_update,name= 'detail_or_update_film')
]
