__author__ = 'DiegoFernando'
from xbee import Zi
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PDG.settings")
from AnalizadorSistemas.Mundo import Calculador
from AnalizadorSistemas.models import Proceso,Entrada,Salida
import serial
import django
from AnalizadorSistemas.Mundo.Recolector import *
django.setup()

from xbee import XBee
import serial

ser = serial.Serial('COM3', 9600)

xbee = ZigBee(ser)

# Continuously read and print packets
while True:
    try:
        print(1)
        response = xbee.wait_read_frame()

        dataIn = response['rf_data']
        decodificacion = dataIn.decode()


        print(decodificacion)

        contenedor = decodificacion.split(";")




        print(contenedor[1])

        if(contenedor[1]=='A'):
            lola = float(contenedor[0])
            #print(lola)
            Recolector.guardarEntrada(lola)
        else:
            lola = float(contenedor[0])
            #print(lola)
            Recolector.guardarSalida(lola)


    except KeyboardInterrupt:
        break

ser.close()