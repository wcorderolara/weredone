# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('reconocimientos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reconocimientousuarios',
            old_name='Description',
            new_name='Descripcion',
        ),
        migrations.RenameField(
            model_name='tiporeconocimiento',
            old_name='Description',
            new_name='Descripcion',
        ),
        migrations.RemoveField(
            model_name='reconocimientousuarios',
            name='idusuario',
        ),
        migrations.AddField(
            model_name='reconocimientousuarios',
            name='idUsuario',
            field=models.ForeignKey(default=1, to='usuarios.Usuarios'),
            preserve_default=False,
        ),
    ]
