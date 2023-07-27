from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    telefone = models.CharField('Telefone', max_length=10)
    email = models.EmailField('E-mail', unique=True)
    sexo = models.IntegerField('Sexo', 
        choices=((1, 'Masculino'), (2, 'Feminino'), (3, 'Outros')), )
    def __str__(self):
        return self.nome