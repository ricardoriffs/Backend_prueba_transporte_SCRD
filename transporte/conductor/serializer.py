from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Driver
        fields = '__all__'

    

class DriverListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Driver
        fields = '__all__'

    def to_representation(self, instance):
        
        return {
            'id': instance['id'],
            'name': instance['name'],
            'lastname':instance['lastname'],
            'email': instance['email']
        }