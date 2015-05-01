from django.contrib import admin

# Register your models here.
from AnalizadorSistemas.models import *

# Register your models here.

class EntradaAdmin(admin.ModelAdmin):
	list_display = ('id', 'tiempoEntrada')

class SalidaAdmin(admin.ModelAdmin):
	list_display = ('id','tiempoSalida', 'defectuoso', 'costo')

class ProcesoAdmin(admin.ModelAdmin):
	list_display = ('id','tiempoPlaneado','porcDisponibilidad','valorInstalacion', 'numOperarios', 'turnoTrabajo',
                    'porcentajeSeguro', 'valorKilowatts', 'presupuestoMensual', 'costoServicios', 'costoHerramienta',
                    'vidaMaquina','estandarCiclo', 'anosMaquina')


admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Salida, SalidaAdmin)
admin.site.register(Proceso,ProcesoAdmin)


