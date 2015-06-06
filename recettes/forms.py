from django.forms import ModelForm
from recettes.models import Recette



class RecetteForm(ModelForm):
    class Meta:
        model = Recette
