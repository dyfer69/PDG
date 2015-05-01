# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnalizadorSistemas', '0004_auto_20150420_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tiempoPlaneado', models.DecimalField(max_digits=10, decimal_places=5)),
                ('porcDisponibilidad', models.DecimalField(max_digits=10, decimal_places=5)),
                ('valorInstalacion', models.DecimalField(max_digits=10, decimal_places=5)),
                ('numOperarios', models.IntegerField()),
                ('turnoTrabajo', models.IntegerField()),
                ('porcentajeSeguro', models.DecimalField(max_digits=10, decimal_places=5)),
                ('valorKilowatts', models.DecimalField(max_digits=10, decimal_places=5)),
                ('presupuestoMensual', models.DecimalField(max_digits=10, decimal_places=5)),
                ('costoServicios', models.DecimalField(max_digits=10, decimal_places=5)),
                ('costoHerramienta', models.DecimalField(max_digits=10, decimal_places=5)),
                ('vidaMaquina', models.DecimalField(max_digits=10, decimal_places=5)),
                ('estandarCiclo', models.DecimalField(max_digits=10, decimal_places=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Variables',
        ),
        migrations.RenameField(
            model_name='entrada',
            old_name='largoEntrada',
            new_name='pesoEntradarada',
        ),
        migrations.RenameField(
            model_name='salida',
            old_name='largoSalida',
            new_name='pesoSalida',
        ),
        migrations.RemoveField(
            model_name='salida',
            name='entrada',
        ),
        migrations.AddField(
            model_name='entrada',
            name='proceso',
            field=models.ForeignKey(default=None, to='AnalizadorSistemas.Proceso'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='salida',
            name='proceso',
            field=models.ForeignKey(default=None, to='AnalizadorSistemas.Proceso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salida',
            name='costo',
            field=models.DecimalField(max_digits=10, decimal_places=5),
            #preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Costo',
        ),
    ]
