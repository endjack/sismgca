from django.db import models

# Create your models EQUIPAMENTOS.
class Situacao(models.Model):
    situacao_id = models.PositiveIntegerField(primary_key=True) 
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label
        
class Par2000T(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Consoles(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Radios(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class CentralAudio(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Diversos(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Ems(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Telefonia(models.Model):
    nome = models.CharField(max_length=100)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


