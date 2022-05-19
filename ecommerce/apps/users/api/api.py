from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

# Al agregar POST me modifica la interfaz para poder agregar un body
@api_view(['GET', 'POST'])
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)

    # AssertionError at /usuario/usuario/
    # Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'NoneType'>`
    elif request.method == 'POST':
        print(request.data) 