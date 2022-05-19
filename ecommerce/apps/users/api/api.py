from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import User
from apps.users.api.serializers import UserSerializer


class UserAPIView(APIView):
    # Retorna un json con todas la info de los users existentes
    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)

    