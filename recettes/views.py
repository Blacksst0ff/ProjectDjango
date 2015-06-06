import django
from django.views import generic
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .models import Recette
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from recettes.forms import RecetteForm
from django.core.context_processors import csrf


def index(request):
    return render(request, 'recettes/index.html')


# Partie Recette
def consulter(request):
    contexte = {
        'recette': Recette.objects.all(),
    }
    return render(request, 'recettes/consulter.html', contexte)


def addrecette(request):

    if request.method == 'POST':
        form = RecetteForm(request.POST)

        if form.is_valid():
            type_recette = form.cleaned_data['type_recette']
            titre = form.cleaned_data['titre']
            difficulte = form.cleaned_data['difficulte']
            cout = form.cleaned_data['cout']
            photo = form.cleaned_data['photo']
            temps_preparation = form.cleaned_data['temps_preparation']
            temps_cuisson = form.cleaned_data['temps_cuisson']
            temps_repos = form.cleaned_data['temps_repos']
            new_recette = form.save()
    else:
            form = RecetteForm()
    return render(request, 'recettes/addRecette.html', locals())


# Part Utilisateur
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, "recettes/register.html", {'form': form, })


@login_required
def logged_in(request):
    return render_to_response('recettes/index.html', context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
