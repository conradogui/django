from django.db import models

# Create your models here.
class Projeto(models.Model):
    nome = models.CharField('Nome', max_length=200)
    descricao = models.TextField('Descrição')
    
    cliente = models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.CASCADE,
    )