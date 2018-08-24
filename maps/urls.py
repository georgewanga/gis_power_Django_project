from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('Primary_substations/', views.Primary_substations_data, name="Primary_substationss_data"),  
    path('Urban_plot_points/', views.Urban_plot_points_data, name="Urban_plot_points_data"),  
    path('secondary_substations/', views.secondary_substations_data, name="secondary_substations_data"),        
]