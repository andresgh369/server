from django.db import models

class Perro( models.Model ):
    id = models.AutoField( primary_key = True )
    name = models.CharField( max_length = 255 )
    description = models.TextField( default= '' )
    estado = models.CharField( max_length = 255, default = 'disponible')
    imageUrl = models.CharField( max_length = 255, default = '' )

    def __str__( self ):
        return self.name