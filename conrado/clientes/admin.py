from django.contrib import admin
from clientes.models import Cliente

# Register your models here.
@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):
    search_fields = (
        'nome',
        'cpf',
        'telefone',
        'email',
    )
    list_filter = (
        'sexo',
    )
    list_display = (
        'nome',
        'cpf',
        'telefone',
        'email',
    )
