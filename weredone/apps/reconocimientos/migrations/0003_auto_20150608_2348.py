# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reconocimientos', '0002_auto_20150608_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReconocimientoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Descripcion', models.CharField(max_length=140)),
                ('Status', models.BooleanField(default=True)),
                ('idReconocimiento', models.ForeignKey(to='reconocimientos.TipoReconocimiento')),
            ],
        ),
        migrations.RemoveField(
            model_name='reconocimientousuarios',
            name='idReconocimiento',
        ),
        migrations.RemoveField(
            model_name='reconocimientousuarios',
            name='idUsuario',
        ),
        migrations.DeleteModel(
            name='ReconocimientoUsuarios',
        ),
    ]
