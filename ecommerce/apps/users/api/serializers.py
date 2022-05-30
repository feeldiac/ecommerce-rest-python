from dataclasses import fields
from http import server
from pyexpat import model
from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Todos los campos del modelo serán claves


class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        if 'develop' in value:
            raise serializers.ValidationError(
                'Error: no puede existir un usuario con ese nombre')
            # Siempre retornar el valor para evitar errores
        return value

    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError('Debe suministrar un correo')

        # Esta validacion es asignada al correo⬇
        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError(
                'El email no puede contenr el nombre')
        return value

    def validate(self, data):
        # Dentro de data puedo acceder a todos los campos que se validan en el serializer
        # Sin embargo desde aquí el error es general y no se asigna a ningún field
        # if data['name'] in data['email']:
        #     raise serializers.ValidationError(
        #         'El email no puede contenr el nombre')
        return data

    def create(self, validated_data):
        # validated_data (dicc) es toda la data validada (el data de validate)
        # Create debe retornar la instancia de un objeto. Como argumento se le pasa **validated data, se le asignan los valores no las llaves.
        # Se registra en la bd y se retorna la instancia
        return User.objects.create(**validated_data)
