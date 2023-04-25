from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .models import Movie
from .forms import MovieForm

# Create your views here.


def index(request):
    context = {
        'home_page_active': 'active'
    }
    return render(request, 'home.html', context)

def movies(request):
    search_str = request.GET.get('search')
    if search_str:
        all_movies = Movie.objects.filter(title__icontains=search_str)
    else:
        all_movies = Movie.objects.all()

    context = {
        'movies_page_active': 'active',
        'movies': all_movies,
    }
    return render(request, 'movies.html', context)

def movie_form(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        movie = Movie(
            order=int(request.POST['order']),
            title=request.POST['title'],
            description=request.POST['description'],
        )
        movie.save()
        return redirect('movies-page')

    return render(request, 'movie_form.html', {'title_h1': 'Movie Form'})

def movie_form_api(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form_data = MovieForm(request.POST)

        if form_data.is_valid:
            data = form_data.cleaned_data

            movie = Movie(
                order=data['order'],
                title=data['title'],
                description=data['description'],
            )
        movie.save()
        return redirect('movies-page')

    return render(request, 'movie_form.html', {'title_h1': 'Movie Form (API)'})
