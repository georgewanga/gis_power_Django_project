from django.urls import path, include
from django.contrib import admin
 
urlpatterns = [
    path('', include('home.urls')), #home page
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('installation/', include('installation.urls')),
    path('contactus/', include('contactus.urls')),
    path('maps/', include('maps.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('forum/', include('forum.urls')),
]
