from django.urls import path
from . import views


urlpatterns = [
    # Produits
    path('', views.liste_produits, name="liste_produits"),
    path('ajouter/', views.ajouter_produit, name="ajouter_produit"),
    path('modifier/<int:pk>/', views.modifier_produit, name="modifier_produit"),
    path('supprimer/<int:pk>/', views.supprimer_produit, name="supprimer_produit"),
    
    # TypeProduit (Nouveau CRUD)
    path('types/', views.liste_types_produits, name="liste_types_produits"),
    path('types/ajouter/', views.ajouter_type_produit, name="ajouter_type_produit"),
    path('types/modifier/<int:pk>/', views.modifier_type_produit, name="modifier_type_produit"),
    path('types/supprimer/<int:pk>/', views.supprimer_type_produit, name="supprimer_type_produit"),
    path('dashboard/', views.dashboard, name='dashboard'),

     # Wilaya (Nouveau CRUD)
    path('wilayas/', views.liste_wilayas, name="liste_wilayas"),
    path('wilayas/ajouter/', views.ajouter_wilaya, name="ajouter_wilaya"),
    path('wilayas/modifier/<int:pk>/', views.modifier_wilaya, name="modifier_wilaya"),
    path('wilayas/supprimer/<int:pk>/', views.supprimer_wilaya, name="supprimer_wilaya"),

    # Moughataa
    path('moughataas/', views.liste_moughataas, name="liste_moughataas"),
    path('moughataas/ajouter/', views.ajouter_moughataa, name="ajouter_moughataa"),
    path('moughataas/modifier/<int:pk>/', views.modifier_moughataa, name="modifier_moughataa"),
    path('moughataas/supprimer/<int:pk>/', views.supprimer_moughataa, name="supprimer_moughataa"),

    # Communes
    path('communes/', views.liste_communes, name="liste_communes"),
    path('communes/ajouter/', views.ajouter_commune, name="ajouter_commune"),
    path('communes/modifier/<int:pk>/', views.modifier_commune, name="modifier_commune"),
    path('communes/supprimer/<int:pk>/', views.supprimer_commune, name="supprimer_commune"),

    # Points de Vente
    path('points_de_vente/', views.liste_points_de_vente, name="liste_points_de_vente"),
    path('points_de_vente/ajouter/', views.ajouter_point_de_vente, name="ajouter_point_de_vente"),
    path('points_de_vente/modifier/<int:pk>/', views.modifier_point_de_vente, name="modifier_point_de_vente"),
    path('points_de_vente/supprimer/<int:pk>/', views.supprimer_point_de_vente, name="supprimer_point_de_vente"),

    # Prix des Produits
    path('prix_produits/', views.liste_prix_produits, name="liste_prix_produits"),
    path('prix_produits/ajouter/', views.ajouter_prix_produit, name="ajouter_prix_produit"),
    path('prix_produits/modifier/<int:pk>/', views.modifier_prix_produit, name="modifier_prix_produit"),
    path('prix_produits/supprimer/<int:pk>/', views.supprimer_prix_produit, name="supprimer_prix_produit"),

    path('paniers/', views.liste_paniers, name="liste_paniers"),
    path('paniers/ajouter/', views.ajouter_panier, name="ajouter_panier"),
    path('paniers/modifier/<int:pk>/', views.modifier_panier, name="modifier_panier"),
    path('paniers/supprimer/<int:pk>/', views.supprimer_panier, name="supprimer_panier"),
    path('wilayas/importer/', views.importer_wilayas, name="importer_wilayas"),
    path('wilayas/exporter/', views.exporter_wilayas, name="exporter_wilayas"),
    path('moughataas/importer/', views.importer_moughataas, name="importer_moughataas"),
    path('moughataas/exporter/', views.exporter_moughataas, name="exporter_moughataas"),
    path('communes/importer/', views.importer_communes, name="importer_communes"),
    path('communes/exporter/', views.exporter_communes, name="exporter_communes"),
    path('types_produits/importer/', views.importer_types_produits, name="importer_types_produits"),
    path('types_produits/exporter/', views.exporter_types_produits, name="exporter_types_produits"),
    path('produits/exporter/', views.exporter_produits, name="exporter_produits"),
    path('produits/importer/', views.importer_produits, name="importer_produits"),
    path('points_de_vente/importer/', views.importer_points_de_vente, name="importer_points_de_vente"),
    path('points_de_vente/exporter/', views.exporter_points_de_vente, name="exporter_points_de_vente"),
    path('prix_produits/importer/', views.importer_prix_produits, name="importer_prix_produits"),
    path('prix_produits/exporter/', views.exporter_prix_produits, name="exporter_prix_produits"),
    path('paniers/importer/', views.importer_paniers, name="importer_paniers"),
    path('paniers/exporter/', views.exporter_paniers, name="exporter_paniers"),
    path('dashboard_produits/', views.dashboard_produits, name="dashboard_produits"),
    path('dashboard_prix_produits/', views.dashboard_prix_produits, name="dashboard_prix_produits"),
    path('dashboard_paniers/', views.dashboard_paniers, name="dashboard_paniers"),
    path('dashboard_inpc/', views.dashboard_inpc, name='dashboard_inpc'),


]
