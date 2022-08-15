from django.db import models

# Create your models here.

from django.db import models

##########################################################
# Models de Localização
##########################################################


class Pais(models.Model):
    def __str__(self):
        return self.nome
    class Meta:
        """Classe feita para definir o plural da models na página de ADMIN do DJANGO"""
        verbose_name_plural = "Paises"

    id = models.AutoField(primary_key=True)
    sigla = models.CharField(max_length=100, null=False, blank=False, default="")
    nome = models.CharField(max_length=500, null=False, blank=False)


class Estado(models.Model):
    def __str__(self):
        return self.nome

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, null=False, blank=False)
    sigla = models.CharField(max_length=500, null=False, blank=False)


class Cidade(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=500, null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=False, blank=False, related_name='cidades')
