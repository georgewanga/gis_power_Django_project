from django.shortcuts import render
from .models import Posts

# Create your views here.


def index(request):
    posts = Posts.objects.all()[:10]
    context = {
        'pg_title': 'GISPower-Forum',
        'posts': posts
    }
    return render(request, 'forum/index.html', context)

def details(request, id):
    posts = Posts.objects.get(id=id)
    context = {
        'pg_title': 'GISPower-post-details',
        'posts': posts
    }
    return render(request, 'forum/details.html', context)
