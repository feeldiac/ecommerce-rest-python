from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # Todos los campos del modelo serán claves
        
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self, value):
        print(value)
        return value

    def validate_email(self, value):
        print(value)
        return value

    def validate(self, data):
        print
        return data