from .models import Lista, Producto, Usuario
from rest_framework import viewsets
from blog.serializers import Listaserializer, Productoserializer, Usuarioserializer

class ListaViewSet( viewsets.ModelViewSet ):
    queryset = Lista.objects.all()
    serializer_class = Listaserializer
	
class ProductoViewSet( viewsets.ModelViewSet ):
    queryset = Producto.objects.all()
    serializer_class = Productoserializer

class UsuarioViewSet( viewsets.ModelViewSet ):
    queryset = Usuario.objects.all()
    serializer_class = Usuarioserializer