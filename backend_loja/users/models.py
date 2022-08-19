from django.db import models
from django.contrib.auth.models import User, Group
from django.forms import BooleanField
from locations.models import *
import hashlib



class UsuarioComprador(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Usuarios compradores"

    
        # Chave estrangeira da tabela auth_user padrão do django related_name='usuario'
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default='', null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    isAtivo = models.BooleanField(default=False)
    phone = models.CharField(max_length=13, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    adress = models.CharField(max_length=500, null=True)
    city = models.ForeignKey(Cidade, null=True, on_delete=models.CASCADE)
    state = models.ForeignKey(Estado, null=True, on_delete=models.CASCADE)
      
    hash_confirm_register = models.CharField(
        max_length=128, null=True, blank=True, default="")
    hash_confirm_senha = models.CharField(
        max_length=128, null=True, blank=True, default="")
    def hash(self):
        # Gerando hash
        return hashlib.sha512((self.nome + self.user.email).encode('utf-8')).hexdigest()
