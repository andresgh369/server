from .models import Lista, Producto, Usuario
from rest_framework import serializers

class Listaserializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Lista
        fields = ( 'id', 'name')
		
class Productoserializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Producto
        fields = ( 'id','name','costop','costor','tienda','notas')

class Usuarioserializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Usuario
        fields = ( 'nombre','email','contraseña')