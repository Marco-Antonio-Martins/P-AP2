from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    telefone = models.PositiveIntegerField() 

class Inquilino(Pessoa):
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True, blank=True)

class Proprietario(Pessoa):
    inquilino = models.ForeignKey(Inquilino, on_delete=models.SET_NULL, null=True, blank=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True, blank=True)

class Sindico(Proprietario):
    salario = models.PositiveIntegerField(default=0, blank=True)

class Condominio(models.Model):
    cnpj = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    sindico = models.ForeignKey(Sindico, on_delete=models.SET_NULL, null=True, blank=True)


class Unidade(models.Model):
    numero = models.PositiveIntegerField()
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.SET_NULL, null=True, blank=True)