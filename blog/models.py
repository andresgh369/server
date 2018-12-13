from django.db import models


class Usuario( models.Model ):
    nombre = models.CharField( max_length = 255 )
    email = models.CharField( max_length = 255 )
    contraseña = models.CharField( max_length = 255 )
    
    def __str__( self ):
        return self.name

class Lista( models.Model ):
    id = models.AutoField( primary_key = True )
    name = models.CharField( max_length = 255 )

    def __str__( self ):
        return self.name
		
class Producto(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 255)
	costop = models.CharField(max_length = 255)
	costor = models.CharField(max_length = 255)
	tienda = models.CharField(max_length = 255)
	notas = models.CharField(max_length = 255)
	
	def __str__(self):
		return self.name