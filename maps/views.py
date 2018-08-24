from django.shortcuts import render
from django.core.serializers import serialize
from . models import Secondary_substations, Primary_substations, Urban_plot_points
from django.http import HttpResponse

def index(request):
    context = {
        'pg_title': 'GISPower-maps',
    }
    return render(request, 'maps/index.html', context)
    
def Primary_substations_data(request):
    pri_substations = serialize('geojson', Primary_substations.objects.all(),geometry_field='point',fields=('name',))
    return HttpResponse(pri_substations,content_type='json')
    
def Urban_plot_points_data(request):
    Urban_plot_pts = serialize('geojson', Urban_plot_points.objects.all(),geometry_field='point',fields=('name',))
    return HttpResponse(Urban_plot_pts,content_type='json')
    
def secondary_substations_data(request):
    Sec_substations = serialize('geojson', Secondary_substations.objects.all(),geometry_field='point',fields=('name',))
    return HttpResponse(Sec_substations,content_type='json')
