from usuarios.models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class usuarioCompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioComprador
        fields = [
            'id',
            'nome',
            'user',
            'isAtivo',
            'cpf',
            'celular',
            'email',
            'endereco',
            'cidade',
            'estado'
            ]
        depth = 1
