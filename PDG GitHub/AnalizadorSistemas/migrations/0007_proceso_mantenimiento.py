# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnalizadorSistemas', '0006_auto_20150421_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='mantenimiento',
            field=models.DecimalField(max_digits=10, default=956, decimal_places=2),
            preserve_default=False,
        ),
    ]
