from django.shortcuts import render


# Create your views here.
def dictionnaire(request):
    dico = {'hello': 'nom', 'prenom': 'ID DICO'}
    return render(request, 'pendu/dico.html', {'dico': dico})


def home(request):
    home = {'hello': 'nom', 'prenom': 'ID Accueil'}
    return render(request, 'pendu/accueil.html', {'home': home})
