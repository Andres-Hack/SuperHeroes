from django.db import models

class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    foco1 = models.BooleanField()
    foco2 = models.BooleanField()
    foco3 = models.BooleanField()
    foco4 = models.BooleanField()
    ventilador = models.BooleanField()
    puerta = models.BooleanField()
    fecha = models.DateTimeField(auto_now_add=True)
    reporte = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Sensores(models.Model):
	mensaje = models.CharField(max_length=100)
	corriente1 = models.CharField(max_length=20)
	humedad = models.CharField(max_length=20)
	humo = models.BooleanField()
	movimiento = models.CharField(max_length=20)
	temperatura = models.CharField(max_length=20)
	reporte = models.DateField(auto_now_add=True)
	
	def __str__(self):
		return self.mensaje
