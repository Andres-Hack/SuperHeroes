from django.contrib.auth.models import User, Group
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, SalaSerializer, SensoresSerializer
from rest_framework.decorators import detail_route, api_view, list_route
from .models import Sala, Sensores
from .raspberry import Rbpi
from .sensores import Estados

class UserViewSet(ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserView(ModelViewSet):
    model = Sala
    serializer_class = SalaSerializer

    def get_queryset(self):
        return  Sala.objects.filter(id=self.kwargs['user_pk'])

class SalaViewSet(ModelViewSet):
    model = Sala
    serializer_class = SalaSerializer

    def get_queryset(self):
        queryset = Sala.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save()

class SalaList(APIView):

    def get(self, request, format=None):
        snippets = Sala.objects.all()
        serializer = SalaSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SalaSerializer(data=request.data)
        estado = request.data
        if serializer.is_valid():
            serializer.save()
            Rbpi(estado)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensoresViewSet(ModelViewSet):
	model = Sensores
	serializer_class = SensoresSerializer
	
	def get_queryset(self):
		return Sensores.objects.all()

	def create(self, request, *args, **kwargs):
		super(SensoresViewSet, self).create(request, *args, **kwargs)
		sensores2 = request.data
		Estados(sensores2)
		return Response(request.data['mensaje'])
	
	def perform_create(self, serializer):
		serializer.save()

class SalaDetalle(APIView):

    def get_object(self, pk):
        try:
            return Sala.objects.get(id=pk)
        except Sala.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SalaSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SalaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReporteView(APIView):

    def get(self, request, pk, format=None):
        mensaje = pk
        return Response('Este es el mensaje : '+mensaje)
"""
ESTA SON LAS VISTAS PARA LOS REPORTES
"""
class SalaEstadosViewSet(ModelViewSet):
    model = Sala
    serializer_class = SalaSerializer

    def get_queryset(self):
        queryset = Sala.objects.all()
        return queryset

class SalaEstadoPorFecha(ModelViewSet):
    model = Sala
    serializer_class = SalaSerializer

    def get_queryset(self):
        fecha = self.kwargs['fecha']
        return  Sala.objects.filter(reporte=self.kwargs['fecha'])

class SensoresPorFecha(ModelViewSet):
    model = Sensores
    serializer_class = SensoresSerializer

    def get_queryset(self):
        fecha_sensor = self.kwargs['fecha_sensor']
        return  Sensores.objects.filter(reporte=self.kwargs['fecha_sensor'])
