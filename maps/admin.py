from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from . models import Primary_substations

# Register your models here.
class Primary_substationsAdmin(LeafletGeoAdmin):
    pass
    
admin.site.register(Primary_substations, Primary_substationsAdmin)