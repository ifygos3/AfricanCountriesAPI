from django.urls import path
from . import views

urlpatterns = [
    path('africa-capital/', views.africa_country, name='africal_country'),
]