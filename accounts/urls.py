from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),    
    path('acc_created/', views.acc_created, name='acc_created'),    
]