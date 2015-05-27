from django.views import generic
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .models import Recette
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf



def index(request):
    return render(request, 'recettes/index.html')

def consulter(request):
    contexte = {
        'recette': Recette.objects.all(),
    }
    return render(request, 'recettes/consulter.html', contexte)

def login(request):
    contexte = {}
    contexte.update(csrf(request))
    return render_to_response('recettes/login.html', contexte)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        form ={
            'errors': "Les Données sont invalides"
        }
        return render(request, 'recettes/login.html', form)

def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('recettes/index.html')
