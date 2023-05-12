from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListCreateAPIView, UpdateAPIView
from .serializer import DriverSerializer


from rest_framework import status

from transporte.helpers import response
from conductor.models import Driver
# Create your views here.

# Clase para crear un conductor
class DriverCreateView(CreateAPIView):
    
    
    
    def post(self, request):

        try:
            data = request.data
            serializer_class = DriverSerializer(data=data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(response.success(serializer_class.data, status.HTTP_201_CREATED, 'El Conductor a sido creado'), status.HTTP_201_CREATED )
            else:
                return Response(response.serverError(serializer_class.errors, status.HTTP_409_CONFLICT, 'Datos incorrectos o faltantes'), status.HTTP_409_CONFLICT )

        except Exception as err :
            return Response(response.serverError(err, status.HTTP_500_INTERNAL_SERVER_ERROR, 'Algo salio mal' ), status.HTTP_500_INTERNAL_SERVER_ERROR)
            

# Clase para actualizar un conductor
class DriveUpdateView(UpdateAPIView):

    def update(self, request, pk):
        try:
            data = request.data
            driver = Driver.objects.filter(id= pk).first()
            serializer_class = DriverSerializer(driver, data=data )
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(response.success(serializer_class.data, status.HTTP_202_ACCEPTED, 'Conductor actualizado'), status.HTTP_202_ACCEPTED )
            else:
                return Response(response.serverError(serializer_class.errors, status.HTTP_406_NOT_ACCEPTABLE, 'Datos incorrectos o faltantes'), status.HTTP_406_NOT_ACCEPTABLE )
        except Exception as err:
            return Response(response.serverError(err, status.HTTP_500_INTERNAL_SERVER_ERROR, 'Algo salio mal' ), status.HTTP_500_INTERNAL_SERVER_ERROR)



class DriveListView(ListCreateAPIView):
    serializer_class = DriverSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.values()
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        try:
            if self.get_queryset():
                driver_serializer = self.serializer_class(self.get_queryset(), many=True)
    
                return Response(response.success(driver_serializer.data, status.HTTP_200_OK, 'Lista de vehículos'), status=status.HTTP_200_OK)
        except Exception as err:
            return Response(response.serverError(err, status.HTTP_500_INTERNAL_SERVER_ERROR, 'Algo salio mal'), status= status.HTTP_500_INTERNAL_SERVER_ERROR)
