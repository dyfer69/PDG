# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnalizadorSistemas', '0005_auto_20150421_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='anosMaquina',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proceso',
            name='costoHerramienta',
            field=models.DecimalField(decimal_places=2, max_digits=10),
            #preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proceso',
            name='costoServicios',
            field=models.DecimalField(decimal_places=2, max_digits=10),
           # preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proceso',
            name='estandarCiclo',
            field=models.DecimalField(decimal_places=2, max_digits=10),
           # preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proceso',
            name='porcDisponibilidad',
            field=models.DecimalField(decimal_places=2, max_digits=10),
            #preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proceso',
            name='porcentajeSeguro',
            field=models.DecimalField(decimal_places=2, max_digits=10),
            #preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proceso',
            name='presupuestoMensual',
            field=models.DecimalField(decimal_places=2, max_digits=10),
            #preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proceso',
            name='tiempoPlaneado',
            field=models.DecimalField(decimal_places=2, max_digits=10),
            #preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proceso',
            name='valorInstalacion',
            field=models.DecimalField(decimal_places=2, max_digits=10),
            #preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proceso',
            name='valorKilowatts',
            field=models.DecimalField(decimal_places=2, max_digits=10),
           # preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proceso',
            name='vidaMaquina',
            field=models.DecimalField(decimal_places=2, max_digits=10),
            #preserve_default=True,
        ),
    ]
