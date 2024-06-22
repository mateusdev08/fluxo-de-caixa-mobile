from django.db import models

# Create your models here.


class FLancamento(models.Model):
    classe = models.CharField(max_length=255)
    grupo = models.CharField(max_length=255)
    natureza = models.CharField(max_length=255)
    dt_movimento = models.DateField()
    dt_vencimento = models.DateField()
    centro_de_custo = models.CharField(max_length=255)
    movimentacao = models.CharField(max_length=255)
    conta = models.CharField(max_length=255)
    cartao = models.CharField(max_length=255)
    status_movimento = models.CharField(max_length=255)
    forma_pagamento = models.CharField(max_length=255)
    qtde_parcela = models.IntegerField()
    parcela = models.IntegerField(null=True, blank=True)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    valor_parcela = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.descricao}"
