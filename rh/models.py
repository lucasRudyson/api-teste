from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=250,blank=False,null=False)
    cpf = models.CharField(max_length=11,blank=False,null=False)
    email = models.EmailField(blank=False,null=True)
    telefone = models.CharField(max_length=12)
    cidade = models.CharField(max_length=200)
    status = models.BooleanField(blank=False,null=False)

