from django.db import models

# Create your models here.
# Tabla Tipo de mascota
class TipoMascota(models.Model):
    mascota = models.CharField(max_length=255)
    estado = models.IntegerField()

    def __str__(self):
        return self.mascota

# Tabla de la raza de la mascota
class Raza(models.Model):
    raza = models.CharField(max_length=255)
    estado = models.IntegerField()
    id_tipo = models.ForeignKey(TipoMascota, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.raza

# Tabla de la cita
class Citas(models.Model):
    mascota = models.CharField(max_length=255)
    edad = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    dueño = models.CharField(max_length=255)
    estado = models.IntegerField()
    raza = models.ForeignKey(Raza, on_delete=models.PROTECT)

    def __str__(self):
        return self.mascota + ' ' +str(self.id)