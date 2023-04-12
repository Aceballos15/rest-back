from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User

# Create your views here.
from .models import Usuario 


from .serializers import UsuarioSerializer


# Register a new user. this function first creates a new user in the django table 
# and then creates it's in the users moddel created by us 
class RegisterView(APIView): 
    def post(self, request, format=None): 

        user = User.objects.create_user(request.data['Correo'], request.data['Correo'], request.data['Contrasena'])
        
        if user: 

            request.data['User'] = user.id
            serializer = UsuarioSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()


                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

# My profile view      
class MyProfileView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, doc):

        usuario = Usuario.objects.filter(Documento = doc) 

        serializer = UsuarioSerializer(usuario, many=True)

        return Response(serializer.data)
    


