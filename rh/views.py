from django.shortcuts import render
from rh.models import Pessoa
from rest_framework import viewsets, permissions
from rh.serializers import PessoaSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer