from django.contrib import admin

from .models import Anime, Manga, Commentaire, Planning_Anime, Planning_Manga, Genre, Affiche, Cover

admin.site.register(Anime)
admin.site.register(Manga)
admin.site.register(Commentaire)
admin.site.register(Planning_Anime)
admin.site.register(Planning_Manga)
admin.site.register(Genre)
admin.site.register(Affiche)
admin.site.register(Cover)
