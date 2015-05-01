import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PDG.settings")
from django.conf.global_settings import DATETIME_FORMAT
from AnalizadorSistemas.models import Proceso,Entrada,Salida
import datetime, decimal



__author__ = 'DiegoFernando'



def obtenerTiemposSalidas(arregloBD):
    tiempoSalidas = []
    for salida in arregloBD:
        tiempoSalidas.append(salida.tiempoSalida)
    return tiempoSalidas

def obtenerTiemposEntrada(arregloBD):
    tiempoEntradas = []
    for entrada in arregloBD:
        tiempoEntradas.append(entrada.tiempoEntrada)
    return tiempoEntradas

def obtenerN(arregloBD):
    N = []
    for i in arregloBD:
        N.append(i.id)
    return N

def obtenerPorcentaje(arregloBD):
    N = []
    for i in arregloBD:
        N.append(i.porcDisponibilidad)
        #print(i.porcDisponibilidad)
    return N

def obtenerPlaneados(arregloBD):
    N = []
    for i in arregloBD:
        N.append(i.tiempoPlaneado)

    return N

def obtenerBuenos(salidas):

    goods= []
    for salida in salidas:
        salidaActual = salida
        if (salidaActual.defectuoso == False):
            goods.append(salidaActual)
    return salidaActual

def obtenerEntrada(index, Entrada):
    resp = 0
    for i in Entrada:
        if(i==index):
            resp = i
        return Entrada[resp]

def CalidadPromedio(Entrada,Salida):

    ciclo = calculoTiempoCiclo(Entrada,Salida)
    if (len(ciclo)>0):
        tiempoInd = sum(ciclo)/len(ciclo)
        bueno = contarBuenos(Salida)
        tiempoProductivo= bueno*tiempoInd
        if len(Salida) > 0:
            tiempoFuncionamiento = Salida[len(Salida)-1].tiempoSalida - Entrada[0].tiempoEntrada
            tiempoFuncionamiento = tiempoFuncionamiento.seconds + tiempoFuncionamiento.microseconds/1000000
            calidad = tiempoProductivo/tiempoFuncionamiento
            print(calidad)
            return calidad
        else:
            return 0
    else:
        return 0

def calculoTiempoCiclo(tiempoEntrada, tiempoSalidas):
    contenedorSalidas = obtenerTiemposSalidas(tiempoSalidas)
    contenedorEntrada = obtenerTiemposEntrada(tiempoEntrada)
    contenedorTiempoCiclo = []
    for i in range(len(contenedorSalidas)):
        tiempo1 = contenedorSalidas[i]
        tiempo2 = contenedorEntrada[i]
        tiempociclo = tiempo1-tiempo2
        total = tiempociclo.seconds + tiempociclo.microseconds/1000000


        contenedorTiempoCiclo.append(total)

    return contenedorTiempoCiclo

def RendimientoPromedio(Entrada, Salida, CostoAdmin):
    if(len(Salida)>0):
        tiempoFuncionamiento = Salida[len(Salida)-1].tiempoSalida - Entrada[0].tiempoEntrada
        tiempoFuncionamiento = tiempoFuncionamiento.seconds + tiempoFuncionamiento.microseconds/1000000
        N=[]
        N = obtenerPorcentaje(CostoAdmin)
        M = obtenerPlaneados(CostoAdmin)
        tOperativo = N[0]*M[0]
        tFun = decimal.Decimal(str(tiempoFuncionamiento))
        rendimiento = tOperativo/tFun
        #print(rendimiento)
        return rendimiento
    else:
        return 0

def calculoRendimiento(tiempoEntrada, tiempoSalida, estandar):
    tiempoCiclo = calculoTiempoCiclo(tiempoEntrada,tiempoSalida)
    rendimientos = []
    for i in tiempoCiclo:
        rendActual = estandar/i
        rendimientos.append(rendActual)
    return rendimientos


def calculoCalidad(salidas):
    totalSalidas = len(salidas)
    calidad = contarBuenos(salidas)/totalSalidas
    return  calidad


def contarBuenos(salidas):
    contador = 0
    for salida in salidas:
        salidaActual = salida
        if (salidaActual.defectuoso == False):
            contador= contador+1
    return contador

def ContarMalos(salidas):
    contador = 0
    for salida in salidas:
        salidaActual = salida
        if (salidaActual.defectuoso == True):
            contador= contador+1
    return contador

def contatTotal(salidas):
    return len(salidas)

def costoHora(info,porcentajeSeguro, vKiloWa, mantenimiento, costoHerramienta, horasHerra, presuMensual,CosAS):
    #Tiempo disponible (TD) = No. SEM / ANO X (No. DIAS / SEM) X No. HORAS / DIA)
    tDisponible = info[6]*info[7]*info[8]

    #Factor de eficiencia (Fe)
    Fe = 1 - (info[9]/tDisponible)

    # Tiempo laborable operario TL =TD*Fe
    tL = tDisponible*Fe

    #Salario Mensual operario (SM) = Factor presatacional*Salario basico

    sM = info[2]*info[3]

    # Costo anual mano de obra directa (kamod) = 12*sM
    kamod = 12*sM

    #Costo mano de obra directa (kmod)
    kmod = kamod/tL

    #Valor Comercial maquina (VC) (1+inflacion)^n *(costo de adquisicion)
    vC = (info[10] + 1)**info[1]*info[0]

    #Costo reposicion maquina (KRM) :
    #si (7<a<10) krm = 0.5*vC
    #si (4<a<7) krm = 0.5*vC
    #si (0<a<4) krm = vC
    if(7<=info[1] < 10):
        krm = vC*0.5
    elif (4<=info[1] < 7):
        krm = vC*0.7
    elif(0<=info[1] < 4):
        krm = vC
    else:
        krm = vC*0.2


    #Tiempo laborable maquinaria (TLM) = NT*TL
    tLM = info[4]*tL

    #Tiempo paro maquina (TPM) = TLM*0.66
    tPM = tLM*0.66

    #Factor de uso (FU) = TPM/TLM
    fU = tPM/tLM

    #Depreciacion maquina (DM) = FU<= 0.4? 10:20
    if(fU<=0.4):
        dM = 10
    else:
        dM = 20

    #Vida Util (VU) = tLM*DM*FU

    vU = tLM*dM*fU
    #Costo depreciacion (KD)
    kD = krm/vU

    #Seguro anual maquinaria (vASM)
    vASM = porcentajeSeguro*vC
    #Seguro hora maquina (vHSM) = VASM/TLM
    vHSM = vASM/tLM

    #Potencia Normal = Segun maquina
    pN = 10

    #Valor KW/hora (VKWH)
    vKWH = vKiloWa

    #Costo energia (KE)
    kE = pN*vKWH

    #Valor Mantenimiento (VM)
    vM = mantenimiento

    #Costo Mantenimiento (KM)
    kM = vM/tLM
    #Costo Herramienta (KH)
    kH = costoHerramienta/horasHerra
    #Gastos de funcionamiento (GF)
    gFM = kD+vASM+kE+kM+kH
    #Presupuesto mensual M.O.I (PMMOI)
    pMMOI = presuMensual
    #Costo Anual M.O Indirecta (KAMOI)
    kAMOI = pMMOI*info[3]
    #Costo por hora de mano de obra indirecta (KHMOI)
    kHMOI = kAMOI/tLM
    #Costo anual de servicios (KAS)
    kAS = CosAS
    #Depreciacion edificacion e instalacion (DE)
    dE = info[11]/20

    #Valor de depreciacion edif einstal (kDE)
    kDE = dE/tLM

    #Costo anual servicios (kS) Datos de la empresa (Sumatoria de valores)
    kS = 10000000
    #Costos financieros anuales (kF) intereses de los prestamos
    #kF = cosFiA
    #costo anual carga fabril
    #kCF = pMMOI+kAMOI + kHMOI + kAS+ dE + kS + kF
    kCF = pMMOI+kAMOI + kHMOI + kAS+ dE + kS
    #Carga Fabril (cF)
    cF = kCF/(tL*info[5])

    #Gastos de fabricacion
    gF = cF + gFM

    #TARIFA HORA MAQUINA
    tMq = kmod + gF

    return tMq

def darCostoSalida(instalaciones, operarios, turnosTrabajo, anos, porcentajeSeguro, vKiloWa, mantenimiento,
                   costoHerramienta, horasHerra, presuMensual,CosAS, deltaTiempo):

    info = generarInfo(instalaciones,operarios,turnosTrabajo,anos)
    print(info[0])
    costoHorari = costoHora(info, porcentajeSeguro, vKiloWa, mantenimiento, costoHerramienta, horasHerra, presuMensual,CosAS)
    costoProducto = costoHorari/3600*deltaTiempo
    return costoProducto

def generarInfo(instalaciones, operarios, turnosTrabajo, anos):

    info = []
    #costo de adquisicion de maquina
    info.append(250000000)
    #Numero de anos de adquisicion
    info.append(anos)
    #salirio basico del operario
    info.append(670000)
    #Factor Prestacional
    info.append(1.55)
    #numero de turnos de trabajo
    info.append(turnosTrabajo)
    #Numero de operarios
    info.append(operarios)
    #Numero de semanas al ano
    info.append(52)
    #Numero de dias por semana
    info.append(6)
    #Numero de horas por turno
    info.append(8)
    #ausentismo remunerado al ano
    info.append((24- info[8])*info[6])

    #inflacion
    info.append(0.05)
    #valor instalaciones
    info.append(instalaciones)

    return info





def datosTiempoCiclo(tiempoEntrada, tiempoSalida):
    ciclo = calculoTiempoCiclo(tiempoEntrada,tiempoSalida)
    N = obtenerN(tiempoSalida)
    datos = []
    for i in range(len(N)):
        valor = [N[i],ciclo[i]]
        datos.append(valor)
    return datos

def datosRendimiento(tiempoEntrada, tiempoSalida, estandar):
    rendimientos = calculoRendimiento(tiempoEntrada,tiempoSalida, estandar)
    N = obtenerN(tiempoSalida)
    datos = []
    for i in range(len(N)):
        valor = [N[i],rendimientos[i]]
        datos.append(valor)
    return datos

def obtenerCostoSalida(arregloBD):
    costoSalida = []
    for salida in arregloBD:
        costoSalida.append(float(salida.costo))
    return costoSalida

def datosCostos(salidas):
    costoSalida = obtenerCostoSalida(salidas)
    N = obtenerN(salidas)
    datos = []
    for i in range(len(N)):
        valor = [N[i],costoSalida[i]]
        datos.append(valor)
    return datos

def generarMatriz(lista):
    matriz= []
    cont = 0
    for i in lista:
        matriz.append([str(i.id) + "," + str(i.tiempoSalida) + "," + str(i.defectuoso) + "," + str(i.costo)])




    return matriz

    #def datosEntrada(entrada):
    #    N = []
    #    entradas = entrada
    #    for i in range(len(entrada)):
    #        valor = [i+1 , float(entradas[i].largoEntrada)]
    #        N.append(valor)
    #    return N
