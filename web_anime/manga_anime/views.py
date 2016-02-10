from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf.urls import include, url
from .models import Manga, Anime, Planning_Anime , Planning_Manga
from django.contrib.auth.models import User
from .forms import InscriptionForm, ConnexionForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,'manga_anime/index.html')

def mangaListe(request):
    mangas = Manga.objects.all()
    return render(request, 'manga_anime/mangaListe.html', {'mangas':mangas})

def anime(request,anime_id):
    animes = Anime.objects.filter(id = anime_id)
    return render(request,'manga_anime/anime.html',{"animes":animes})


def animeListe(request):
    animes = Anime.objects.all()
    return render(request,'manga_anime/animeListe.html', {"animes" : animes})

def manga(request,manga_id):
    mangas = Manga.objects.filter(id = manga_id)
    animes = Anime.objects.filter(manga__id = manga_id)
    return render(request,'manga_anime/manga.html',{'mangas':mangas, "animes" : animes})

def monCompte(request):
    return render(request,'manga_anime/monCompte.html')

def team(request):
    return render(request,'manga_anime/team.html')

def contact(request):
    return render(request,'manga_anime/contact.html')

def planning(request, user_id):
        pa = Planning_Anime.objects.filter( user__id = user_id)
        pm = Planning_Manga.objects.filter( user__id = user_id)
        return render(request,'manga_anime/planning.html',{"pa":pa,"pm":pm})

def ajoutPlanningManga(request, manga_id, user_id):
        error = False
        planning = Planning_Manga.objects.filter(manga__id = manga_id )
        mangas = Manga.objects.get (id = manga_id)
        user = User.objects.get (id = user_id)
        if planning:
            print("Manga deja present dans le planning")
            error = True
            return render(request,'manga_anime/index.html')

        else:
            planning = Planning_Manga( user = user , manga = mangas)
            planning.save()
            return render(request,'manga_anime/index.html')

def ajoutPlanningAnime(request, anime_id, user_id):
        error = False
        planning = Planning_Anime.objects.filter(anime__id = anime_id )
        animes = Anime.objects.get(id = anime_id)
        user = User.objects.get (id = user_id)
        if planning:
            print("Anime deja present dans le planning")
            error = True
            return render(request,'manga_anime/index.html')

        else:
            planning = Planning_Anime( user = user , anime = animes)
            planning.save()
            return render(request,'manga_anime/index.html')


def inscription(request):
    error = False

    if request.method == "POST":

        form = InscriptionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            email = form.cleaned_data["email"]

            if password1 == password2:
                user = User.objects.create_user(username,email,password1)
                return redirect('index')
            else:
                return redirect('inscription')

    else:
        form = InscriptionForm()
    return render(request, 'manga_anime/inscription.html', {'form' : form})

def connexion(request):
    error = False
    print("Connexion en cours...")
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        print("RÃ©ponse du serveur...")
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username = username, password = password) # Nous vÃ©rifions si les donnÃ©es sont correctes
            print(user)
            print(username)
            print(password)

            print("Valide !")
            if user: # Si l'objet renvoyÃ© n'est pas None
                login(request, user) # nous connectons l'utilisateur
                print("Success !")
            else: # sinon une erreur sera affichÃ©e
                print("Login incorrect...")
                error = True
        else:
            print("Non valide...")

    else:
            print("Pas de requÃªte...")
            form = ConnexionForm()

    return render(request, 'manga_anime/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return render(request, 'manga_anime/connexion.html', locals())
