from django.contrib.gis.db import models

class Primary_substations(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    total_rev = models.FloatField()
    geom = models.MultiPointField(srid=4326)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Primary_substations"

class Urban_plot_points(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    daily_kwh = models.FloatField()
    f_tariff = models.FloatField()
    tariff_kwh = models.FloatField()
    d_revenue = models.FloatField()
    total_rev = models.FloatField()
    geom = models.MultiPointField(srid=4326)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Urban_plot_points"

class Urban_plots(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Urban_plots"

class Secondary_substations(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    revenue = models.FloatField()
    geom = models.MultiPointField(srid=4326)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Secondary_substations"

class MV_poles(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    geom = models.MultiPointField(srid=4326)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "MV_poles"

class MV_line_sections(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "MV_line_sections"

class LV_line_sections(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "LV_line_sections"

class LV_polests(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    geom = models.MultiPointField(srid=4326)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "LV_polests"

class LV_poles(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.IntegerField()
    altmode = models.IntegerField()
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    haslabel = models.IntegerField()
    labelid = models.IntegerField()
    geom = models.MultiPointField(srid=4326)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "LV_poles"
