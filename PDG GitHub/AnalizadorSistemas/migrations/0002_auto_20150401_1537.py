# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnalizadorSistemas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='costo',
            old_name='valor',
            new_name='costoValor',
        ),
    ]
