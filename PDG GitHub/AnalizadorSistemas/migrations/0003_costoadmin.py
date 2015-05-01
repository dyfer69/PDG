# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnalizadorSistemas', '0002_auto_20150401_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tiempoPlaneado', models.DecimalField(max_digits=10, decimal_places=5)),
                ('porcDisponibilidad', models.DecimalField(max_digits=10, decimal_places=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
