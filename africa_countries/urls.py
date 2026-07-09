from django.urls import path
from . import views

urlpatterns = [
    path('africa-capital/', views.africa_country, name='africal_country'),
    path('africa-countries/', views.AfricaCountryListCreateView.as_view(), name='africa_country_list_create'),
    path('africa-countries/<int:id>/', views.AfricaCountryRetrieveUpdateDestroyView.as_view(), name='africa_country_retrieve_update_destroy'),
]