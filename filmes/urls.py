from django.urls import path
from filmes.views import home_page, create_new_movie,FilmeDetail

app_name='filmes'
urlpatterns = [
    path('home_page/',home_page, name='home_page'),
    path('create_new_movie/',create_new_movie,name='new_movie'),
    path('detail_movie/<int:pk>',FilmeDetail.as_view(),name= 'detail_film')
]
