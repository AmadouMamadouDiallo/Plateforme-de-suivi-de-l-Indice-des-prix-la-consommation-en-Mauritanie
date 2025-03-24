from django.contrib import admin
from django.urls import path, include
from myapp.views import home  # Import de la vue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produits/', include('myapp.urls')),  # Routes spécifiques à l'application `myapp`
    path('', home, name="home"),  # Page d'accueil
    path('accounts/', include('myapp.auth_urls')),  # Routes pour l'authentification
]
