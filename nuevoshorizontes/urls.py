from django.urls import path
from .views import home, login, nosotros, sedes, noticias

urlpatterns = [
    path('', home, name="home"),
    path('nosotros', nosotros, name="nosotros"),
    path('sedes', sedes, name="sedes"),
    path('noticias', noticias, name="noticias"),
    path('login', login, name="login"),
]