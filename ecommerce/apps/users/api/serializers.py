from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Si utilizas fields no utilizas
        fields = '__all__'
        
