from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recette


def index(request):
    return render(request, 'recettes/index.html')

def consulter(request):
    contexte = {
        'recette': Recette.objects.all(),
    }
    return render(request, 'recettes/consulter.html', contexte)
