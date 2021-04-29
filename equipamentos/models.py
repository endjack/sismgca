from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import datetime

# Create your models EQUIPAMENTOS.
class Situacao(models.Model):
    situacao_id = models.PositiveIntegerField(primary_key=True) 
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label

    def get_class_bootstrap(self):
        if self.situacao_id == 1:
            return "btn btn-success"
        elif self.situacao_id == 2:
            return "btn btn-warning"
        elif self.situacao_id == 3:
            return "btn btn-danger"
        elif self.situacao_id == 4:
            return "btn btn-secondary"
        else:
            return "btn btn-light"

               
class Par2000T(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True,null=True)
    ultimo_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Consoles(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True,null=True)
    ultimo_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Radios(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True,null=True)
    ultimo_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class CentralAudio(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True,null=True)
    ultimo_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Diversos(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True,null=True)
    ultimo_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Ems(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True,null=True)
    ultimo_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Telefonia(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True,null=True)
    ultimo_registro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome



