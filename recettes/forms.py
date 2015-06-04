from django import forms


class RecetteForm(forms.Form):

    type_recette = forms.CharField(max_length=15)
    titre = forms.CharField(max_length=50)
    difficulte = forms.CharField(max_length=15)
    cout = forms.IntegerField()
    photo = forms.CharField(max_length=250)
    temps_preparation = forms.IntegerField()
    temps_cuisson = forms.IntegerField()
    temps_repos = forms.IntegerField()
