from django.contrib import admin
from projetos.models import Projeto

# Register your models here.
@admin.register(Projeto)
class ProjetosAdmin(admin.ModelAdmin):
    search_fields = (
        'nome',
        'descricao',
        'cliente__nome'
    )
    list_display = (
        'nome',
        'descricao', 
        'cliente'
    )