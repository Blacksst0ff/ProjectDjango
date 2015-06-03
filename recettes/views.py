import django
from django.views import generic
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .models import Recette
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.context_processors import csrf


def index(request):
    return render(request, 'recettes/index.html')


def consulter(request):
    contexte = {
        'recette': Recette.objects.all(),
    }
    return render(request, 'recettes/consulter.html', contexte)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, "recettes/register.html", {'form': form, })


@login_required
def logged_in(request):
    return render_to_response('recettes/index.html', context_instance=RequestContext(request))


# def login(request):
#
#   contexte = {}
#    contexte.update(csrf(request))
#    return render_to_response('recettes/login.html', contexte)


#def auth_view(request):
#    username = request.POST.get('username', '')
#    password = request.POST.get('password', '')
#    user = auth.authenticate(username=username, password=password)

#    if user is not None:
#        auth.login(request, user)
#        return HttpResponseRedirect('/')
#    else:
#        return HttpResponseRedirect('/login/?error=true')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
