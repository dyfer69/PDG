from xbee import XBee
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PDG.settings")
from AnalizadorSistemas.Mundo.Calculador import Calculador
from AnalizadorSistemas.models import Proceso,Entrada,Salida
import serial
import django
django.setup()


__author__ = 'DiegoFernando'

class Recolector(object):




    def guardarEntrada(dato):
        entrada = Entrada(id=len(Entrada.objects.all())+1,pesoEntradarada = dato)
        totalProcesos = Proceso.objects.all()


        ultimo = totalProcesos[len(totalProcesos)-1]
        entrada.proceso = ultimo
        entrada.save()

    def guardarSalida(dato):

        salida = Salida(id=len(Salida.objects.all())+1,pesoSalida = dato)

        totalProcesos = Proceso.objects.all()
        ultimo = totalProcesos[len(totalProcesos)-1]

        salida.proceso =ultimo

        if (salida.pesoSalida<69):
            salida.defectuoso=True
        else:
            salida.defectuoso=False

        salida.costo = 1
        salida.save()


        instalaciones = float(ultimo.valorInstalacion)
        numOperarios = float(ultimo.numOperarios)
        turnoTrabajo = float(ultimo.turnoTrabajo)
        anosMaquina = float(ultimo.anosMaquina)
        porcentajeSeguro =  float(ultimo.porcentajeSeguro)
        valorKilowatts = float(ultimo.valorKilowatts)
        presupuestoMensual = float(ultimo.presupuestoMensual)
        costoServicio = float(ultimo.costoServicios)
        costoHerramienta = float(ultimo.costoHerramienta)
        vidaMaquina= float(ultimo.vidaMaquina)
        mantenimiento = float(ultimo.mantenimiento)

        salidas = Salida.objects.all()
        ultimaSalida = salidas[len(salidas)-1]

        entradas = Entrada.objects.all()
        ultimaEntrada = entradas[len(entradas)-1]

        tiempoSalida = ultimaSalida.tiempoSalida
        tiempoEntrada = ultimaEntrada.tiempoEntrada

        print("tiempo entrada:")
        print(tiempoEntrada)
        print("tiempo salida:")
        print(tiempoSalida)

        tiempociclo = tiempoSalida-tiempoEntrada
        deltaT  = tiempociclo.seconds + tiempociclo.microseconds/1000000
        print(deltaT)

        print(instalaciones)

        costillo = Calculador.darCostoSalida(instalaciones, numOperarios, turnoTrabajo , anosMaquina, porcentajeSeguro,
                                             valorKilowatts,mantenimiento, costoHerramienta, vidaMaquina,
                                             presupuestoMensual, costoServicio, deltaT)


        costillo = float("{0:.2f}".format(costillo))
        #print(costillo)
        ultimaSalida.costo = costillo

        ultimaSalida.save()



#Recolector.guardarEntrada(60)
#Recolector.guardarSalida(50)
#totalProcesos = Proceso.objects.all()
#print(totalProcesos)

