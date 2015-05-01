# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('valor', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tiempoEntrada', models.DateTimeField(auto_now_add=True)),
                ('largoEntrada', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tiempoSalida', models.DateTimeField(auto_now_add=True)),
                ('largoSalida', models.DecimalField(max_digits=10, decimal_places=2)),
                ('defectuoso', models.BooleanField(default=True)),
                ('costo', models.ForeignKey(to='AnalizadorSistemas.Costo', default=None)),
                ('entrada', models.ForeignKey(to='AnalizadorSistemas.Entrada', default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
