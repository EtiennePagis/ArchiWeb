#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
#Fixtures pour tester !!!


class Genre(models.Model):
    nom_genre = models.CharField(max_length=30)
    description = models.TextField()
    def __str__(self):
        return self.nom_genre

class Affiche(models.Model):
    nom_affiche = models.CharField(max_length=30)
    lien = models.TextField()
    def __str__(self):
        return self.nom_affiche


class Cover(models.Model):
    nom_cover = models.CharField(max_length=30)
    lien = models.TextField()
    lien_a_venir = models.TextField()
    def __str__(self):
        return self.nom_cover


class Manga(models.Model):

    titre = models.CharField(max_length=30)
    auteur = models.CharField(max_length=40)
    nb_tome_paru = models.IntegerField()
    nb_tome_tot = models.IntegerField()
    date_tome = models.DateField()
    synopsis = models.TextField()
    note = models.FloatField()
    nb_vote = models.IntegerField()
    tags = models.TextField()
    cover = models.ForeignKey(
    Cover,
    on_delete = models.CASCADE,
    )
    genre = models.ForeignKey(
    Genre,
    on_delete = models.CASCADE, null=True,
    )
    def __str__(self):
        return self.titre

class Anime(models.Model):
    titre = models.CharField(max_length=30)
    studio = models.CharField(max_length=30)
    nb_episode_diffuse = models.IntegerField()
    nb_episode_tot = models.IntegerField()
    date_episode = models.DateField()
    synopsis = models.TextField()
    note = models.FloatField()
    nb_vote = models.IntegerField()
    tags = models.TextField()
    genre = models.ForeignKey(
    Genre,
    on_delete = models.CASCADE,
    )
    manga = models.ForeignKey(
    Manga,
    on_delete = models.CASCADE,
    )
    affiche = models.ForeignKey(
    Affiche,
    on_delete = models.CASCADE,
    )
    def __str__(self):
        return self.titre

class Commentaire(models.Model):

    contenu = models.TextField()
    user = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    )

class Planning_Anime(models.Model):
    anime = models.ForeignKey(
    Anime,
    on_delete = models.CASCADE,
    )
    user = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    )


class Planning_Manga(models.Model):
    manga = models.ForeignKey(
    Manga,
    on_delete = models.CASCADE,
    )
    user = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    )
    
