from django.contrib import admin
from .models import Recette, Ingredient, Commentaire, Note, Etape

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecetteAdmin(admin.ModelAdmin):
    model = Recette

class EtapeAdmin(admin.ModelAdmin):
    model = Etape

class NoteAdmin(admin.ModelAdmin):
    model = Note

class CommentaireAdmin(admin.ModelAdmin):
    model = Commentaire

admin.site.register(Recette, RecetteAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Etape, EtapeAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Note, NoteAdmin)