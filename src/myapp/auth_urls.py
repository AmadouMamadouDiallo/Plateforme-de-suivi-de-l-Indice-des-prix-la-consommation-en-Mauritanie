from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Route pour la connexion
    path('logout/', views.logout_view, name='logout'),  # Route pour la déconnexion
    path('register/', views.register, name='register'),  # Route pour l'inscription
]
