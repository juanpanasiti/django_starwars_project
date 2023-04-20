from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home-page'),
    path('list/', views.movies, name='movies-page'),
]
