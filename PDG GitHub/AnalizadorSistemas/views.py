from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from AnalizadorSistemas.models import *
from django.core import serializers
from django.http import HttpResponse
from AnalizadorSistemas.Mundo import Calculador
from django.template import RequestContext
import json
import csv
# Create your views here.

def login(request):

    template = "login.html"
    return render(request,template,context_instance=RequestContext(request))

@login_required(redirect_field_name='home')
def exportar(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datos.csv"'
    writer = csv.writer(response)
    totalSalidas = Salida.objects.all()
    lista = list(totalSalidas)
    matriz = Calculador.generarMatriz(lista)
    print(matriz[0])
    writer.writerow(['Producto', 'Fecha', 'Defectuoso', 'Costo'])
    for i in matriz:
        writer.writerow(i)



    return  response



def home(request):

    #Contenedores de datos
    totalSalidas = Salida.objects.all()
    totalEntradas = Entrada.objects.all()

    N = Calculador.obtenerN(totalSalidas)
    #Calculo de Calidad
    totalDatos = Calculador.contatTotal(totalSalidas)
    totalDefectuosos = Calculador.ContarMalos(totalSalidas)
    totalAceptados = Calculador.contarBuenos(totalSalidas)
    #Calculo Tiempo de Ciclo
    tiempoCiclo = Calculador.datosTiempoCiclo(totalEntradas,totalSalidas)
    ##Calculo indicadores
    info = Proceso.objects.all()
    porcentajes= Calculador.obtenerPorcentaje(info)
    disponibilidad = porcentajes[len(porcentajes)-1]
    dispo = str(disponibilidad)
    rendimiento = Calculador.RendimientoPromedio(totalEntradas,totalSalidas,info)
    rendi = float("{0:.2f}".format(rendimiento))
    calidad = Calculador.CalidadPromedio(totalEntradas,totalSalidas)
    calidad = float("{0:.2f}".format(calidad))
    #Calculo Rendimiento
    rendimiento = Calculador.datosRendimiento(totalEntradas,totalSalidas,0.03)
    #Costos
    costos = Calculador.datosCostos(totalSalidas)

    diccionario = {'malos':totalDefectuosos,'buenos':totalAceptados,
                                 'totalDatos':totalDatos,'N':N,'ciclo':tiempoCiclo,
                                 'calidad':str(calidad), 'dispo':dispo, 'rendimientoG':str(rendi), 'rendimientoU':rendimiento,
                    'costos':costos}


    template = "index.html"
    return render(request, template, diccionario, context_instance=RequestContext(request))

def actualizar(request):


    #Contenedores de datos
    totalSalidas = Salida.objects.all()
    totalEntradas = Entrada.objects.all()
    N = Calculador.obtenerN(totalSalidas)
    #Calculo de Calidad
    totalDatos = Calculador.contatTotal(totalSalidas)
    totalDefectuosos = Calculador.ContarMalos(totalSalidas)
    totalAceptados = Calculador.contarBuenos(totalSalidas)
    #Calculo Tiempo de Ciclo
    tiempoCiclo = Calculador.datosTiempoCiclo(totalEntradas,totalSalidas)
    ##Calculo indicadores
    info = Proceso.objects.all()
    porcentajes= Calculador.obtenerPorcentaje(info)
    disponibilidad = porcentajes[len(porcentajes)-1]
    dispo = str(disponibilidad)
    rendimiento = Calculador.RendimientoPromedio(totalEntradas,totalSalidas,info)
    rendi = float("{0:.2f}".format(rendimiento))
    calidad = Calculador.CalidadPromedio(totalEntradas,totalSalidas)
    calidad = float("{0:.2f}".format(calidad))
    #Calculo Rendimiento
    rendimiento = Calculador.datosRendimiento(totalEntradas,totalSalidas,0.03)
    #Costos
    costos = Calculador.datosCostos(totalSalidas)




    datos = {'malos':totalDefectuosos,'buenos':totalAceptados,
                                 'totalDatos':totalDatos,'N':N,'ciclo':tiempoCiclo,
                                 'calidad':str(calidad), 'dispo':dispo, 'rendimientoG':str(rendi), 'rendimientoU':rendimiento,
                                 'costos':costos}




    salida =  json.dumps(datos)
    return HttpResponse(salida, content_type='application/json')

def variables(request):
    template = "variables.html"
    return render(request,template,context_instance=RequestContext(request))

def subir(request):
    # if this is a POST request we need to process the form data
    vInstalaciones = request.POST.get("instalaciones")
    numOperario = request.POST.get("operarios")
    turnosTrabajo = request.POST.get("turnosTrabajo")
    anosMaquina = request.POST.get("anosAdquisicionMaquina")
    porcentajeSeguro = request.POST.get("porcentajeSeguro")
    valorKilowatts = request.POST.get("valorKiloWatts")
    costoHerramienta = request.POST.get("costoHerramienta")
    vidaMaquina = request.POST.get("vidaMaquina")
    presMensual = request.POST.get("presupuestoMensual")
    costoServicios = request.POST.get("CostoServicios")
    porcentajeDisponibilidad = request.POST.get("porcDisponibilidad")
    mantenimieno = request.POST.get("mantenimiento")
    tiempoPlaneado = request.POST.get("tiempoPlaneado")
    estandarCiclo = request.POST.get("estandarCiclo")

    proceso = Proceso(tiempoPlaneado=tiempoPlaneado, porcDisponibilidad= porcentajeDisponibilidad, valorInstalacion = vInstalaciones,
                       numOperarios=numOperario, turnoTrabajo= turnosTrabajo, porcentajeSeguro = porcentajeSeguro,
                       valorKilowatts = valorKilowatts, presupuestoMensual = presMensual, costoServicios= costoServicios,
                        costoHerramienta = costoHerramienta, vidaMaquina = vidaMaquina, estandarCiclo=estandarCiclo,
                        anosMaquina = anosMaquina, mantenimieno=mantenimieno)


    proceso.save()


    return HttpResponseRedirect("/")





