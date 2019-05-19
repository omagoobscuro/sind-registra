from django.db import models
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db.models import Avg, Count, Min, Sum, Max, F
from django.db.models.manager import Manager
import math

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    endereco= models.CharField(max_length=100)
    telefone = models.CharField(max_length=12)
    cnpj = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    

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

class Lancamento(models.Model):
    STATUS_PAGAMENTO = (
        ('P','Pago'),
        ('N','Não Pago'),    
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2)  
    vencimento = models.DateField()
    data_envio = models.DateField(null=True, blank=True) 
    status = models.CharField('Pago',max_length=1,choices=STATUS_PAGAMENTO)
     
    def __str__(self):
        return str(self.empresa) if self.empresa else ''

class LancamentoTotal(models.Model):
    valor = models.DecimalField(max_digits=6, decimal_places=2)  
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
      verbose_name_plural = "lançamentos Totais"

    def __str__(self):
        return str(self.valor) if self.valor else ''

class DebitoTotal(models.Model):
    valor = models.DecimalField(max_digits=6, decimal_places=2)  
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
      verbose_name_plural = "Debitos Totais"

    def __str__(self):
        return str(self.valor) if self.valor else ''

class Debito(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2) 
    vencimento = models.DateField()
    
    def save(self, *args, **kwargs):
            super(Debito, self).save(*args, **kwargs)

            send_mail(
    'Debito em aberto',
    'Voce possui debitos em nosso sistema.',
    'acelinofernandessilva@hotmail.com',
    ['celticfolkmetal@hotmail.com'],
    fail_silently=False,
)
    def __str__(self):
        return str(self.empresa) if self.empresa else ''

class Financeiro(models.Model):
    debito = models.ForeignKey(DebitoTotal, on_delete=models.CASCADE)
    lancamento = models.ForeignKey(LancamentoTotal, on_delete=models.CASCADE)
    consulta = models.DateTimeField(auto_now=False, auto_now_add=False,)

    def total(self):
        return (self.lancamento.valor - self.debito.valor)

class Agendamento(models.Model):
    ATENDIDO = 'A'
    NAO_ATENDIDO = 'NA'
    NAO_COMPARECEU = 'NC'
    STATUS= (
        (ATENDIDO, 'Atendido'),
        (NAO_ATENDIDO, 'Nao atendido'),
        (NAO_COMPARECEU, 'Nao compareceu'),
        
    )

    nome = models.CharField(max_length=100)
    data = models.DateField()
    inicio = models.TimeField(unique=True)
    fim = models.TimeField()
    assunto = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS, default=ATENDIDO, max_length=2)

    def __str__(self):
        return self.nome
     