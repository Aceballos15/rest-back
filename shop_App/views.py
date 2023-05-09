from rest_framework import generics, mixins
from .models import Producto, Comentario, ProductImage
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer, ComentarioSerializer, ProductImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

#Create a new product 
class ProductListCreateView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Producto.objects.all()
    serializer_class = ProductSerializer



# This function returns all products where status is false
class InactiveProuctsView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        prod = []
        productos = Producto.objects.filter(Estado = False)

        print (productos.count())
        for pr in productos: 
            ImageArray = []
            imagenes = ProductImage.objects.filter(Producto = pr)
            for i in imagenes: 
                ImageArray.append(i.Imagen)

            data = {
                'Nombre': pr.Nombre, 
                'id': pr.id, 
                'images': ImageArray, 
                'Descripcion': pr.Descripcion, 
                'Caracteristicas': pr.Caracteristicas, 
                'Categoria': pr.Categoria, 
                'Disponible': pr.Disponible,
                'Precio_base': pr.Precio_base, 
                'Porcentaje_plataforma': pr.Porcentaje_plataforma, 
                'Portada': pr.Portada, 
                'Porcentaje_venta': pr.Porcentaje_venta, 
                'Precio_calculado': pr.Precio_calculado, 
                'material': pr.material, 
                'Estado': pr.Estado,
                'Genero': pr.Genero, 
                'Usuario': pr.Usuario
            }
            prod.append(data)

        serializer = ProductSerializer(prod, many=True)

        return Response(serializer.data)
        



#View all products  
class ProductosView(APIView): 
    def get(self, request, *args, **kwargs):

        prod = []
        productos = Producto.objects.all()

        for pr in productos: 
            ImageArray = []
            imagenes = ProductImage.objects.filter(Producto = pr)
            for i in imagenes: 
                ImageArray.append(i.Imagen)

            data = {
                'Nombre': pr.Nombre, 
                'id': pr.id, 
                'images': ImageArray, 
                'Descripcion': pr.Descripcion, 
                'Caracteristicas': pr.Caracteristicas, 
                'Categoria': pr.Categoria, 
                'Disponible': pr.Disponible,
                'Precio_base': pr.Precio_base, 
                'Porcentaje_plataforma': pr.Porcentaje_plataforma, 
                'Portada': pr.Portada, 
                'Porcentaje_venta': pr.Porcentaje_venta, 
                'Precio_calculado': pr.Precio_calculado, 
                'material': pr.material, 
                'Estado': pr.Estado,
                'Genero': pr.Genero, 
                'Usuario': pr.Usuario
            }
            prod.append(data)

        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)
        

#View a product detail or edit a product
class ProductoDetalleView(generics.UpdateAPIView, mixins.UpdateModelMixin): 
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
   
    def get(self, request, id): 

        prod = []
        producto = get_object_or_404(Producto, id= id)


        ImageArray = []
        imagenes = ProductImage.objects.filter(Producto = producto)
        for i in imagenes: 
            ImageArray.append(i.Imagen)

        data = {
            'Nombre': producto.Nombre, 
            'id': producto.id, 
            'images': ImageArray, 
            'Descripcion': producto.Descripcion, 
            'Caracteristicas': producto.Caracteristicas, 
            'Categoria': producto.Categoria, 
            'Disponible': producto.Disponible,
            'Precio_base': producto.Precio_base, 
            'Porcentaje_plataforma': producto.Porcentaje_plataforma, 
            'Portada': producto.Portada, 
            'Porcentaje_venta': producto.Porcentaje_venta, 
            'Precio_calculado': producto.Precio_calculado, 
            'material': producto.material, 
            'Estado': producto.Estado,
            'Genero': producto.Genero, 
            'Usuario': producto.Usuario
        }
        prod.append(data)      

        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)
    


#Edit a product 
class EditProductView(generics.UpdateAPIView, mixins.UpdateModelMixin): 
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'  

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # Edit a product by id 
    def put(self, request, id):

        instance = self.get_object()
        
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({ "Message": "Producto actualizado satisfactoriamente"})


#View first six products 
class FirstProducts(APIView):
    def get(self, request): 
        prod = []
        productos = Producto.objects.order_by('-id')[:6]

        for pr in productos: 
            ImageArray = []
            imagenes = ProductImage.objects.filter(Producto = pr)
            for i in imagenes: 
                ImageArray.append(i.Imagen)

            data = {
                'Nombre': pr.Nombre, 
                'id': pr.id, 
                'images': ImageArray, 
                'Descripcion': pr.Descripcion, 
                'Caracteristicas': pr.Caracteristicas, 
                'Categoria': pr.Categoria, 
                'Disponible': pr.Disponible,
                'Precio_base': pr.Precio_base, 
                'Porcentaje_plataforma': pr.Porcentaje_plataforma, 
                'Portada': pr.Portada, 
                'Porcentaje_venta': pr.Porcentaje_venta, 
                'Precio_calculado': pr.Precio_calculado, 
                'material': pr.material, 
                'Estado': pr.Estado,
                'Genero': pr.Genero, 
                'Usuario': pr.Usuario
            }
            prod.append(data)
        
        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)
    


#get products for category  
class ProductCategoria(APIView): 
    def get(self, request, category, *args, **kwargs): 

        prod = []
        producto =Producto.objects.filter(Categoria= category)

        for pr in producto: 
            ImageArray = []
            imagenes = ProductImage.objects.filter(Producto = pr)
            for i in imagenes: 
                ImageArray.append(i.Imagen)

            data = {
                'Nombre': pr.Nombre, 
                'id': pr.id, 
                'images': ImageArray, 
                'Descripcion': pr.Descripcion, 
                'Caracteristicas': pr.Caracteristicas, 
                'Categoria': pr.Categoria, 
                'Disponible': pr.Disponible,
                'Precio_base': pr.Precio_base, 
                'Porcentaje_plataforma': pr.Porcentaje_plataforma, 
                'Portada': pr.Portada, 
                'Porcentaje_venta': pr.Porcentaje_venta, 
                'Precio_calculado': pr.Precio_calculado, 
                'material': pr.material, 
                'Estado': pr.Estado,
                'Genero': pr.Genero, 
                'Usuario': pr.Usuario
            }
            prod.append(data)

        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)
    


# Assign % for a pruduct and calculate his total and partial price 
class CalculatePriceView(generics.UpdateAPIView, mixins.UpdateModelMixin): 

    queryset = Producto.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.Porcentaje_plataforma = float(request.data['Porcentaje_plataforma'])
        instance.Porcentaje_venta = float(request.data['Porcentaje_venta'])
        instance.Precio_base = float(instance.Precio_base)


        instance.Precio_calculado = float(instance.Precio_base) + ((instance.Precio_base * instance.Porcentaje_plataforma / 100 )+ (instance.Precio_base * instance.Porcentaje_venta / 100 ))
        instance.Estado = True

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({ "message": "Porcentajes agregados correctamente"})

        

#Add comment of a product 
class ComentarView(APIView): 

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        

        serializer = ComentarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

#View all comments of a product and edit a comment 
class VerComentarios(APIView):

    def get(self, request, id):
        Comentarios = Comentario.objects.filter(Producto=id)
        serializer = ComentarioSerializer(Comentarios, many=True)

        return Response(serializer.data)
    

# Update a coment
    def put(self, request, id):

        Comentarios = get_object_or_404(Comentario, id= id)
        serializer = ComentarioSerializer(Comentarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    
