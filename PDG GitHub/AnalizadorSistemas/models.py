from django.db import models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PDG.settings")
# Create your models here.

class Proceso(models.Model):
    tiempoPlaneado = models.DecimalField(max_digits=10, decimal_places=2)
    porcDisponibilidad = models.DecimalField(max_digits=10,decimal_places=2)
    valorInstalacion = models.DecimalField(max_digits=10,decimal_places=2)
    numOperarios = models.IntegerField()
    turnoTrabajo = models.IntegerField()
    anosMaquina = models.IntegerField()
    porcentajeSeguro = models.DecimalField(max_digits=10,decimal_places=2)
    mantenimiento = models.DecimalField(max_digits=10,decimal_places=2)
    valorKilowatts = models.DecimalField(max_digits=10,decimal_places=2)
    presupuestoMensual = models.DecimalField(max_digits=10,decimal_places=2)
    costoServicios = models.DecimalField(max_digits=10,decimal_places=2)
    costoHerramienta = models.DecimalField(max_digits=10,decimal_places=2)
    vidaMaquina = models.DecimalField(max_digits=10,decimal_places=2)
    estandarCiclo = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return str(self.id)


class Entrada(models.Model):
    tiempoEntrada = models.DateTimeField(auto_now_add=True)
    pesoEntradarada = models.DecimalField(max_digits=10, decimal_places=2)
    proceso = models.ForeignKey(Proceso, default=None)

    def __str__(self):
        return str(self.id)



class Salida(models.Model):

    tiempoSalida = models.DateTimeField(auto_now_add=True)
    pesoSalida = models.DecimalField(max_digits=10, decimal_places=2)
    defectuoso = models.BooleanField(default=True)
    costo = models.DecimalField(max_digits=15,decimal_places=2)
    proceso = models.ForeignKey(Proceso, default=None)

    def __str__(self):
        return str(self.id)


