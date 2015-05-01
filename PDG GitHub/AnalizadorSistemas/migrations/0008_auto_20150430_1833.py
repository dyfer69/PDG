# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnalizadorSistemas', '0007_proceso_mantenimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salida',
            name='costo',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
    ]
