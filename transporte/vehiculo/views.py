from django.http import QueryDict
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework import status
from .serializer import VehicleSerializer, VehicleJoinSerializer
from .models import Vehicle
from conductor.models import Driver
from transporte.helpers import response
# Create your views here.

#Clase para crear los vehículos
class VehicleCreateView(CreateAPIView):
    
    
    # Método post
    # Se encarga de recibir la data enviada en la petición post y validar por medio del serializador que los datos sean correctos  
    def post(self, request):

        try:
            data = request.data
            serializer_class = VehicleSerializer(data=data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(response.success(serializer_class.data, status.HTTP_201_CREATED, 'Vehículo creado'), status.HTTP_201_CREATED )
            else:
                return Response(response.serverError(serializer_class.errors, status.HTTP_409_CONFLICT, 'Datos incorrectos o faltantes'), status.HTTP_409_CONFLICT )

        except Exception as err :
            return Response(response.serverError(err, status.HTTP_500_INTERNAL_SERVER_ERROR, 'Algo salio mal' ), status.HTTP_500_INTERNAL_SERVER_ERROR)


# Clase para listar los vehículos que no tienen un conductor asignado
class VehicleNoneListView(ListCreateAPIView):
    
    queryset = Vehicle.objects.all().filter(conductor_id=None)
    serializer_class = VehicleSerializer
    
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        try:
            queryset = self.get_queryset()
            serializer = VehicleSerializer(queryset, many=True)
            return Response(response.success(serializer.data, 200, 'Lista de vehículos'))
        except Exception as err:
            return Response(response.serverError(err, status.HTTP_500_INTERNAL_SERVER_ERROR, 'Algo salio mal'), status= status.HTTP_500_INTERNAL_SERVER_ERROR)

# Clase para listar los vehículos que ya están asignados a un conductor  
class VehicleListView(ListCreateAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self, id):
        return self.get_serializer().Meta.model.objects.values().filter(conductor_id=id)
    
    def list(self, request, id):
        
        try:
            
            
            vehicle_serializer = self.serializer_class(self.get_queryset(id), many=True)
            return Response(response.success(vehicle_serializer.data,  status.HTTP_200_OK, 'Lista de vehículos'), status= status.HTTP_200_OK)
        except Exception as err:
            return Response(response.serverError(err, status.HTTP_500_INTERNAL_SERVER_ERROR, 'Algo salio mal'), status= status.HTTP_500_INTERNAL_SERVER_ERROR)

 

# Clase para listar todos los vehículos
class VehicleAllListView(ListCreateAPIView):
    
    queryset = Vehicle.objects.all().values()
    serializer_class = VehicleSerializer
    
    def list(self, request):
        
        try:
            queryset = self.get_queryset()
            serializer = VehicleSerializer(queryset, many=True)
            return Response(response.success(serializer.data, 200, 'Lista de vehículos'))
        except Exception as err:
            return Response(response.serverError(err, status.HTTP_500_INTERNAL_SERVER_ERROR, 'Algo salio mal'), status= status.HTTP_500_INTERNAL_SERVER_ERROR)

# Clase para asociar un conductor a un vehículo
class VehicleJoinDriverView(UpdateAPIView):
    serializer_class = VehicleJoinSerializer

    def get_queryset(self, id):
        return self.get_serializer().Meta.model.objects.filter(id=id).first() 
    
    
    

    def put(self, request, id=None):
        driver = Driver.objects.values().filter(id=request.data.get('conductor_id')).first()
        if not driver:
            return Response(response.serverError({}, status.HTTP_404_NOT_FOUND, 'No se encuentra conductor'), status.HTTP_404_NOT_FOUND )
        if self.get_queryset(id):
            vehicle_serializer = self.serializer_class(self.get_queryset(id), data=request.data, partial=True)
            if vehicle_serializer.is_valid():
                vehicle_serializer.save()
                return Response(response.success(vehicle_serializer.data, status.HTTP_200_OK, 'Vehículo actualizado'))
            return Response(response.serverError(vehicle_serializer.errors, status.HTTP_404_NOT_FOUND, 'No se encuentra vehículo con estos datos'), status.HTTP_404_NOT_FOUND )