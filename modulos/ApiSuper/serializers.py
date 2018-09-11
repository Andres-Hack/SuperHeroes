from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Sala, Sensores

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email')

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('name', 'id')

class SalaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sala
        fields = (
            'id',
            'nombre',
            'foco1',
            'foco2',
            'foco3',
            'foco4',
            'ventilador',
            'puerta',
            'fecha',
            'reporte',
        )

class SensoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensores
        fields = '__all__'
