from django.contrib import admin

from u.models import Category, States, Region, Iso, Site


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class StatesAdmin(admin.ModelAdmin):
    list_display = ['name']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']


class IsoAdmin(admin.ModelAdmin):
    list_display = ['name']


class SiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'category', 'states', 'region', 'iso', 'area_hectares', 'longitude', 'latitude',
                    'justification', 'description']


admin.site.register(Category, CategoryAdmin)
admin.site.register(States, StatesAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Iso, IsoAdmin)
admin.site.register(Site, SiteAdmin)
