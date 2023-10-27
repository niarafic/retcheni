from django.urls import path
from inicio.views import inicio, usuario
urlpatterns = [
    
    path('', inicio),
    path('usuario/', usuario)
]
