from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
from .models import Usuario 


from .serializers import UsuarioSerializer


# Register a new user 
class RegisterView(APIView): 
    def post(self, request, format=None): 

        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# Login view -> obtain a token 
class LoginView(APIView):

    def post(self, request, format=None):
        
        info = request.data

        user = Usuario.objects.filter(Correo = info['correo'], Contrasena = info['password'])

        if user: 
            refresh = RefreshToken.for_user(user[0])

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response({'error': 'Credenciales inválidas.'}, status=400)  


# My profile view 
      
class MyProfileView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, doc):

        usuario = Usuario.objects.filter(Documento = doc) 


        serializer = UsuarioSerializer(usuario, many=True)

        return Response(serializer.data)
    


