from django.urls import path
from inicio.views import inicio, staff
urlpatterns = [
    
    path('', inicio, name='Inicio'),
    path('staff/', staff, name='staff')
]
