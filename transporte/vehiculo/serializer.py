from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vehicle
        fields = '__all__'

class VehicleJoinSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vehicle
        fields = ['conductor_id']

    # def patch(self, instance, validated_data):
    #     print(validated_data)
    #     instance.driver_id = validated_data.get('driver_id')
    #     instance.save()
    #     return instance