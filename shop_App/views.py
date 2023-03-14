from rest_framework import generics, mixins
from rest_framework import generics
from .models import Producto, Comentario, ProductImage
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer, ComentarioSerializer, ProductImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 


#Create a new product 
class ProductListCreateView(generics.ListCreateAPIView):

    queryset = Producto.objects.all()
    serializer_class = ProductSerializer


#Ver todos los productos    
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
        

#Ver detalle de un producto
class ProductoDetalleView(APIView): 
    def get(self, request, id): 

        producto = get_object_or_404(Producto, id= id)
        serializer = ProductSerializer(producto)
        return Response(serializer.data)
    
    def put(self, request, id):

        producto = get_object_or_404(Producto, id= id)
        serializer = ProductSerializer(producto, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    


#Ver los primeros 6 productos
class FirstProducts(APIView):

    def get(self, request): 
        productos = Producto.objects.order_by('-id')[:6]

        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data)
    


#Obtener productos por categoria 
class ProductCategoria(APIView): 
    def get(self, request, category, *args, **kwargs): 

        producto =Producto.objects.filter(Categoria= category)
        serializer = ProductSerializer(producto, many=True)
        return Response(serializer.data)
    


#Autorizar producto
class AutorizarProducto(generics.UpdateAPIView, mixins.UpdateModelMixin):
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

#Agregar comentario 
class ComentarView(APIView): 

    def post(self, request, *args, **kwargs):
        

        serializer = ComentarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

#Ver los comentarios de un producto
class VerComentarios(APIView):

    def get(self, request, id):
        Comentarios = Comentario.objects.filter(Producto=id)
        serializer = ComentarioSerializer(Comentarios, many=True)

        return Response(serializer.data)
    

    def put(self, request, id):

        Comentarios = get_object_or_404(Comentario, id= id)
        serializer = ComentarioSerializer(Comentarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    