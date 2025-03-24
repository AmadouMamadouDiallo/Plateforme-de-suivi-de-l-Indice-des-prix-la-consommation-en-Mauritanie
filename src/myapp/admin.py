from django.contrib import admin
from .models import Produit, Wilaya, Moughataa, Commune, PointDeVente, PrixProduit, PanierProduit

# Enregistrez vos modèles
admin.site.register(Produit)
admin.site.register(Wilaya)
admin.site.register(Moughataa)
admin.site.register(Commune)
admin.site.register(PointDeVente)
admin.site.register(PrixProduit)
admin.site.register(PanierProduit)
