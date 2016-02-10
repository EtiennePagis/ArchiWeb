from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mangaListe', views.mangaListe, name='mangaListe'),
    url(r'^animeListe', views.animeListe, name='animeListe'),
    url(r'^manga/(?P<manga_id>\d*)/$', views.manga, name='manga'),
    url(r'^anime/(?P<anime_id>\d*)/$', views.anime, name='anime'),
    url(r'^ajoutPlanningManga/(?P<manga_id>\d*)/(?P<user_id>\d*)/$', views.ajoutPlanningManga , name="ajoutPlanningManga"),
    url(r'^ajoutPlanningAnime/(?P<anime_id>\d*)/(?P<user_id>\d*)/$', views.ajoutPlanningAnime , name="ajoutPlanningAnime"),
    url(r'^monCompte', views.monCompte, name='monCompte'),
    url(r'^planning/(?P<user_id>\d*)/$', views.planning, name='planning'),
    url(r'^connexion',views.connexion, name='connexion'),
    url(r'^inscription',views.inscription, name='inscription'),
    url(r'^deconnexion', views.deconnexion, name='deconnexion'),
]
