from django.urls import path 
from . import views 


urlpatterns = [
    #Productos
     path('products/create/', views.ProductListCreateView.as_view()),
     path('products/', views.ProductosView.as_view()),
     path('products/<int:id>', views.ProductoDetalleView.as_view()),
     path('productsDestacados/', views.FirstProducts.as_view()),
     path('products/<str:category>', views.ProductCategoria.as_view()),
     path('products/autorizar/<int:id>', views.AutorizarProducto.as_view()),

     #Comentarios
     path('comentarios/create/', views.ComentarView.as_view()),
     path('comentarios/<int:id>', views.VerComentarios.as_view()),

     #Carro de compras 
     path('carrito/create/', views.VerComentarios.as_view()),
]










