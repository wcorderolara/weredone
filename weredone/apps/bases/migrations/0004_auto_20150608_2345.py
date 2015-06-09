# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0003_claseobjetivo_estadosgenerales_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claseobjetivo',
            old_name='Description',
            new_name='Descripcion',
        ),
        migrations.RenameField(
            model_name='estadosgenerales',
            old_name='Description',
            new_name='Descripcion',
        ),
        migrations.RenameField(
            model_name='tipoobjetivo',
            old_name='Description',
            new_name='Descripcion',
        ),
        migrations.RenameField(
            model_name='tipoobjeto',
            old_name='Description',
            new_name='Descripcion',
        ),
    ]
