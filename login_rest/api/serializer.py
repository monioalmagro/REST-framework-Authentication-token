from rest_framework import serializer 
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Merta:
        model = Persona
        fields = {
            'id',
            'nombre',
            'apellido',
        }