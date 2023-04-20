from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'home_page_active': 'active'
    }
    return render(request, 'home.html', context)

def movies(request):
    context = {
        'movies_page_active': 'active'
    }
    return render(request, 'movies.html', context)