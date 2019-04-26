from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    endereco= models.CharField(max_length=100)
    telefone = models.CharField(max_length=12)
    cnpj = models.CharField(max_length=12)

    def __str__(self):
        return self.nome


class Associado(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=12)
    data_nascimento = models.DateField()
    data_filiacao = models.DateField()
    cpf = models.CharField(max_length=12)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=5, decimal_places=2)  
    data_pagamento = models.DateField()   
    enviar_comprovante = models.FileField(blank=True)

    def __unicode__(self):
        return self.empresa