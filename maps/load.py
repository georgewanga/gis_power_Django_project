import os
from django.contrib.gis.utils import LayerMapping
from .models import Primary_substations,Urban_plot_points,Urban_plots,Secondary_substations,MV_poles,MV_line_sections,LV_line_sections,LV_polests,LV_poles

primary_substations_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'total_rev': 'Total_Rev',
    'geom': 'MULTIPOINT25D',
}
model_array = [Primary_substations]
maps_shp = [os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Primary_substation.shp'))]
mapping_array = [primary_substations_mapping]

urban_plot_points_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'daily_kwh': 'Daily_Kwh',
    'f_tariff': 'F_tariff',
    'tariff_kwh': 'Tariff_kwh',
    'd_revenue': 'D_Revenue',
    'total_rev': 'Total_rev',
    'geom': 'MULTIPOINT25D',
}
model_array.append(Urban_plot_points)
maps_shp.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Urban_plot_point.shp')))
mapping_array.append(urban_plot_points_mapping)

urban_plots_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'clamped': 'Clamped',
    'extruded': 'Extruded',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON25D',
}
model_array.append(Urban_plots)
maps_shp.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Urban_plot.shp')))
mapping_array.append(urban_plots_mapping)

secondary_substations_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'revenue': 'Revenue',
    'geom': 'MULTIPOINT25D',
}
model_array.append(Secondary_substations)
maps_shp.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Secondary_substation.shp')))
mapping_array.append(secondary_substations_mapping)

mv_poles_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'geom': 'MULTIPOINT25D',
}
model_array.append(MV_poles)
maps_shp.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/MV_pole.shp')))
mapping_array.append(mv_poles_mapping)

mv_line_sections_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'clamped': 'Clamped',
    'extruded': 'Extruded',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING25D',
}
model_array.append(MV_line_sections)
maps_shp.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/MV_line_section.shp')))
mapping_array.append(mv_line_sections_mapping)

lv_line_sections_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'clamped': 'Clamped',
    'extruded': 'Extruded',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING25D',
}
model_array.append(LV_line_sections)
maps_shp.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/LV_line_section.shp')))
mapping_array.append(lv_line_sections_mapping)

lv_polests_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'geom': 'MULTIPOINT25D',
}
model_array.append(LV_polests)
maps_shp.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/LV_polest.shp')))
mapping_array.append(lv_polests_mapping)

lv_poles_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'folderpath': 'FolderPath',
    'symbolid': 'SymbolID',
    'altmode': 'AltMode',
    'base': 'Base',
    'snippet': 'Snippet',
    'popupinfo': 'PopupInfo',
    'haslabel': 'HasLabel',
    'labelid': 'LabelID',
    'geom': 'MULTIPOINT25D',
}
model_array.append(LV_poles)
maps_shp.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/LV_pole.shp')))
mapping_array.append(lv_poles_mapping)

def run(verbose=True):
    for i in range(9):
        lm = LayerMapping(model_array[i],maps_shp[i],mapping_array[i],transform=False,encoding='iso-8859-1',)
        lm.save(strict=True,verbose=verbose)