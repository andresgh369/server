from .models import Perro
from rest_framework import viewsets
from blog.serializers import PerroSerializer

class PerroViewSet( viewsets.ModelViewSet ):
    queryset = Perro.objects.all().order_by( 'estado' )
    serializer_class = PerroSerializer
