from django.db import models

# Create your models here.

class Listing(models.Model):
    listing_uls = models.CharField(max_length=100)
    listing_type = models.CharField(max_length=100)
    listing_price = models.CharField(max_length=100)
    listing_address = models.CharField(max_length=100)
    listing_piece = models.CharField(max_length=100)
    listing_chambre = models.CharField(max_length=100)
    listing_nb_salle_de_bain = models.CharField(max_length=100)
    listing_dimensions = models.CharField(max_length=100)
    listing_year = models.CharField(max_length=100)
    listing_energetique = models.CharField(max_length=100)
    listing_fenestration = models.CharField(max_length=100)
    listing_revetement = models.CharField(max_length=100)
    listing_revetement_toiture = models.CharField(max_length=100)
    listing_laveuse_secheuse = models.CharField(max_length=100)
    listing_garage = models.CharField(max_length=100)
    listing_armoire = models.CharField(max_length=100)
    listing_salle_de_bain = models.CharField(max_length=100)
    listing_sous_sol = models.CharField(max_length=100)
    listing_renovation = models.CharField(max_length=100)
    listing_topographie = models.CharField(max_length=100)
    listing_vue = models.CharField(max_length=100)
    listing_alle = models.CharField(max_length=100)
    listing_stationnement = models.CharField(max_length=100)
    listing_chauffage = models.CharField(max_length=100)
    listing_energie = models.CharField(max_length=100)
    #listing_images
    listing_desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.listing_uls