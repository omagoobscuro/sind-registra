from django.db import models
from core.models import Associado, Empresa

class Juridico(models.Model):
    ENTRADA = 'E'
    EM_ANDAMENTO = 'EA'
    AUDIENCIA = 'A'
    SENTENCA = 'S'
    RECURSO = 'R'
    EXECUCAO = 'E'
    STATUS= (
        (ENTRADA, 'Entrada'),
        (EM_ANDAMENTO, 'Em andamento'),
        (AUDIENCIA, 'audiencia'),
        (SENTENCA, 'Sentença'),
        (RECURSO, 'Recurso'),
        (EXECUCAO, 'Execução'),
        
    )

    processo = models.CharField(max_length=50)
    reclamante = models.ForeignKey(Associado, on_delete=models.CASCADE)
    cpf_reclamante = models.CharField(max_length=100)
    reclamado = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cnpj_reclamado = models.CharField(max_length=100)
    nome_advogado = models.CharField(max_length=100)
    forum = models.CharField(max_length=100)
    data_entrada = models.DateField()
    local_audiencia = models.CharField(max_length=100, null=True, blank=True)
    data_audiencia = models.DateField(null=True, blank=True)
    sentenca = models.CharField(max_length=100, null=True, blank=True)
    data_sentenca = models.DateField(null=True, blank=True)
    recurso = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(choices=STATUS, default=ENTRADA, max_length=2)

    class Meta:
      verbose_name_plural = "Juridico"

    def __str__(self):
        return self.processo
