from django.urls import path
from filmes.views import home_page, create_new_movie, film_detail_or_update,delete_film,create_user

app_name='filmes'
urlpatterns = [
    path('',home_page, name='home_page'),
    path('create_new_movie/',create_new_movie,name='new_movie'),
    path('delete_movie/<int:pk>/',delete_film,name='delete_filme'),
    path('detail_movie/<int:pk>/',film_detail_or_update,name= 'detail_or_update_film'),
    path('create_user/',create_user,name="criar_user")
]
