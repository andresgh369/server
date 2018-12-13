from .models import Lista, Producto
from rest_framework import viewsets
from blog.serializers import Listaserializer, Productoserializer

class ListaViewSet( viewsets.ModelViewSet ):
    queryset = Lista.objects.all()
    serializer_class = Listaserializer
	
class ProductoViewSet( viewsets.ModelViewSet ):
    queryset = Producto.objects.all()
    serializer_class = Productoserializer