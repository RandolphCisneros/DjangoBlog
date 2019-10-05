from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'RandyC',
        'title' : 'AlbumOfTheDayOct2',
        'content' : 'First Post Content',
        'date_posted' : 'Oct22019',
    },
    {
        'author' : 'RandolphC',
        'title' : 'AlbumOfTheDayOct3',
        'content' : 'Second Post Content',
        'date_posted' : 'Oct32019',
    }
]

def home(request):
    context = {
        'posts' : posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'Album Of the Day'})
