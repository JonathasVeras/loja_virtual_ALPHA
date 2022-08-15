from localizacoes.models import *
from rest_framework import serializers

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'sigla', 'nome']


class CidadeSerializer(serializers.ModelSerializer):
    #estado = serializers.HyperlinkedRelatedField(view_name='estado-detail', read_only=True)
    class Meta:
        model = Cidade
        fields = ['id', 'nome']
        #depth = 1


class EstadoSerializer(serializers.ModelSerializer):
    cidades = CidadeSerializer(read_only=True, many=True)

    class Meta:
        model = Estado
        fields = ['id', 'sigla', 'nome', 'cidades']
        depth = 1
