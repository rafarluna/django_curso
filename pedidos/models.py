from django.db import models
import datetime

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=150, default="")
    cantidad = models.DecimalField(max_digits=10, decimal_places=4)
    descripcion = models.CharField(max_length=400, default="")
    activo = models.BooleanField()

class Tenant(models.Model):
    name= models.CharField(max_length=150, default="")
    RFC=models.CharField(max_length=18, default="000-000-000")
    email= models.CharField(max_length=150, default="")

class Pedido(models.Model):
    cliente= models.ForeignKey(Cliente, 
                             related_name='clientes',
                             on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=4)
    fecha_pedido = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return 'Pedido de cliente'