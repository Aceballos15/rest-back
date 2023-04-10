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


    def create(self, validated_data): 

        images_data = validated_data.pop('images')
        product = Producto.objects.create(**validated_data)
      
   

        for img in images_data:  
            ProductImage.objects.create(Producto=product, Imagen=img)

        return product.name   

# Serializer for a comment form 
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Comentario
        fields= '__all__'


