# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnalizadorSistemas', '0003_costoadmin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CostoAdmin',
            new_name='Variables',
        ),
    ]
