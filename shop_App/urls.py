from django.urls import path 
from . import views 


urlpatterns = [
    #Products url's
     path('products/create/', views.ProductListCreateView.as_view()),
     path('products/', views.ProductosView.as_view()),
     path('products/<int:id>', views.ProductoDetalleView.as_view()),
     path('productsDestacados/', views.FirstProducts.as_view()),
     path('products/<str:category>', views.ProductCategoria.as_view()),

     #Coments url's
     path('comentarios/create/', views.ComentarView.as_view()),
     path('comentarios/<int:id>', views.VerComentarios.as_view()),

     #Administration url's
     path('admin/assign/<int:id>', views.CalculatePriceView.as_view())
]










