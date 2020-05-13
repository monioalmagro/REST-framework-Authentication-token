from django.shortcuts import render
from rest_framework import generics
from . models import Persona
from .serializer import PersonaSerializer


class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
