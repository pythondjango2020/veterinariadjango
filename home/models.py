from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length= 45)
    password = models.CharField(max_length= 45)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    dueño = models.CharField(max_length=45)
    nombre = models.CharField(max_length= 45)
    edad = models.IntegerField()
    raza = models.CharField(max_length=45)


class Servicio(models.Model):
    nombre = models.CharField(max_length= 45)
    descripcion = models.TextField(max_length=1000)
    precio = models.IntegerField()


estado =(
    ('cotizacion','cotizacion'),
    ('ejecucion','ejecucion'),
    ('terminada','termiada'),
    ('confirmada_veterinario','confirmada_veterinario'),
)
class Servicio_Mascota(models.Model):
    id_mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)
    id_servicio = models.ForeignKey(Servicio, on_delete= models.PROTECT)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    costo = models.IntegerField()
    estado = models.CharField(choices= estado,max_length=30)


class Promocion(models.Model):
    nombre = models.CharField(max_length= 45)
    descripcion = models.TextField(max_length=1000)
    porcentaje = models.IntegerField()

    def __str__(self):
        return self.nombre


class Promocion_Servicio(models.Model):
    servicio_id_servicio = models.ForeignKey(Servicio,on_delete= models.PROTECT)
    id_promocion = models.ForeignKey(Promocion,on_delete= models.PROTECT)


class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    categoria = models.CharField(max_length=45)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre
    

class Producto_Promocion(models.Model):
    producto_id_producto = models.ForeignKey(Producto, on_delete= models.PROTECT)
    promocion_id_promocion = models.ForeignKey(Promocion,on_delete= models.PROTECT)       



    