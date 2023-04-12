from rest_framework import serializers
from rest_framework.response import Response

from .models import Producto, ProductImage, Comentario 


# Serializer for images 
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'



# Serializer for a product and create many images for this
class ProductSerializer(serializers.ModelSerializer):

    images = ProductImageSerializer(many=True,  required=False, read_only=True)

    images = serializers.ListField(
        child=serializers.ImageField(max_length=1000, use_url = True)
    )
    
    class Meta:
        model = Producto
        fields = '__all__'


    #This function create a produict and create their respective images 
    # with their relationship in the images table 
    def create(self, validated_data): 


        images_data = validated_data.pop('images')
        product = Producto.objects.create(**validated_data)
      
        imagesArray = []

        for img in images_data:  
            ProductImage.objects.create(Producto=product, Imagen=img)

            imagesArray.append(img)

        data = {
                'Nombre': product.Nombre, 
                'id': product.id, 
                'images': imagesArray, 
                'Descripcion': product.Descripcion, 
                'Caracteristicas': product.Caracteristicas, 
                'Categoria': product.Categoria, 
                'Disponible': product.Disponible,
                'Precio_base': product.Precio_base, 
                'Porcentaje_plataforma': product.Porcentaje_plataforma, 
                'Portada': product.Portada, 
                'Porcentaje_venta': product.Porcentaje_venta, 
                'Precio_calculado': product.Precio_calculado, 
                'material': product.material, 
                'Estado': product.Estado,
                'Genero': product.Genero, 
                'Usuario': product.Usuario, 
                'Message': "Producto creado satisfactoriamente"
            }

        return data

# Serializer for a comment form 
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Comentario
        fields= '__all__'


