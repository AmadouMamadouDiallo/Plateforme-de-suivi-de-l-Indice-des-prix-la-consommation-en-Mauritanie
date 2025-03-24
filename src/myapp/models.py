from django.db import models


class TypeProduit(models.Model):
    code = models.CharField(max_length=45, unique=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Produit(models.Model):  # Produit générique
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    unite_mesure = models.CharField(max_length=45, default="kg", help_text="Unité de mesure du produit")
    type_produit = models.ForeignKey(TypeProduit, on_delete=models.CASCADE, related_name="produits")

    def __str__(self):
        return self.nom



class Wilaya(models.Model):
    code = models.CharField(max_length=45, unique=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Moughataa(models.Model):
    code = models.CharField(max_length=45, unique=True)
    nom = models.CharField(max_length=255)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name="moughataas")

    def __str__(self):
        return self.nom


class Commune(models.Model):
    code = models.CharField(max_length=45, unique=True)
    nom = models.CharField(max_length=255)
    moughataa = models.ForeignKey(Moughataa, on_delete=models.CASCADE, related_name="communes")

    def __str__(self):
        return self.nom


class PointDeVente(models.Model):
    code = models.CharField(max_length=45, unique=True)
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    gps_latitude = models.FloatField()
    gps_longitude = models.FloatField()
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name="points_de_vente")

    def __str__(self):
        return self.nom


class PrixProduit(models.Model):  # Relie Produits, PointDeVente et prix
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="prix_produits")
    point_de_vente = models.ForeignKey(PointDeVente, on_delete=models.CASCADE, related_name="prix_point_de_vente")
    valeur = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.produit.nom} - {self.valeur} MRU au {self.point_de_vente.nom} ({self.date})"


class PanierProduit(models.Model):  # Regroupement de produits avec pondération évolutive
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="panier_produits")
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    poid = models.FloatField(help_text="Pondération utilisée pour le calcul de l'INPC")

    def __str__(self):
        return f"Produit {self.produit.nom} - Poids {self.poids}"
