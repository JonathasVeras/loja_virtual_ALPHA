from django.shortcuts import render
from rest_framework import generics
from localizacoes.models import *
from localizacoes.serializers import *
# Create your views here.

class PaisList(generics.ListAPIView):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer


class EstadoList(generics.ListAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class CidadeList(generics.ListAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
