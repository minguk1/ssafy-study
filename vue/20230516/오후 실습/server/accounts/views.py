from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):

    print(request.data)
    if request.data['password1'] == request.data['password2']:
        serial = {'username' : request.data['username'], 'password' : request.data['password1']}
        serializer = UserSerializer(data=serial)
        print(serializer)
    

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)