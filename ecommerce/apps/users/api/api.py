from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, TestUserSerializer


@api_view(['GET', 'POST']) # The api_view decorator takes a list of HTTP methods that your view should respond to. 
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        test_data = {
            'name': 'develop',
            'email': 'dev@gmail.com'
        }
        test_user = TestUserSerializer(data = test_data)
        if test_user.is_valid():
            print('Pasó validaciones')
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST': # Al agregar POST me modifica la interfaz para poder agregar un body
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'Usuario creado correctamente.'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    user = User.objects.filter(id = pk).first() # Simulamos un get, evitando un try catch

    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data) # Instancia + Nueva data
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'Usuario eliminado correctamente.'}, status=status.HTTP_200_OK)
    
    return Response({'message': 'No se ha encontrado un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)