from users.models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class usuarioCompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioComprador
        fields = [
            'id',
            'name',
            'user',
            'isAtivo',
            'cpf',
            'phone',
            'email',
            'adress',
            'city',
            'state'
            ]
        depth = 1
