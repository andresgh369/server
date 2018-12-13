from .models import Lista, Producto
from rest_framework import serializers

class Listaserializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Lista
        fields = ( 'id', 'name')
		
class Productoserializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Producto
        fields = ( 'id','name','costop','costor','tienda','notas')