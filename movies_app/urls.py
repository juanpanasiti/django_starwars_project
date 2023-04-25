from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home-page'),
    path('list/', views.movies, name='movies-page'),
    path('form/', views.movie_form, name='movie-form'),
    path('form-api/', views.movie_form_api, name='movie-form-api'),
]
