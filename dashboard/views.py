from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'pg_title': 'GISPower-dashboard',
    }
    return render(request, 'dashboard/index.html', context)