from django.urls import path
from . import views

urlpatterns = [
    
    path('lga-hq/', views.rivers_lga, name='lga_hq'),
    path('state-capital/', views.state_capital, name='state_capital'),
    # path('africa-capitals/', views.africa_capitals, name='africal_capitals'),
]