from django.contrib import admin
from .models import AfricaCountry

# Register your models here.
@admin.register(AfricaCountry)
class AfricaCountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital', 'population', 'area', 'currency', 'official_language', 'created_at', 'updated_at')
    search_fields = ('name', 'capital', 'currency', 'official_language')
    list_filter = ('currency', 'official_language')