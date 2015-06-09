# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20150608_2348'),
        ('reconocimientos', '0003_auto_20150608_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='reconocimientousuario',
            name='idUsuario',
            field=models.ForeignKey(to='usuarios.Usuario'),
        ),
    ]
