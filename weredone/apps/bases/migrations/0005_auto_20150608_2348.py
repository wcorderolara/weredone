# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0004_auto_20150608_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadosGenerale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Descripcion', models.CharField(max_length=25)),
                ('Status', models.BooleanField(default=True)),
                ('idTipoObjeto', models.ForeignKey(to='bases.TipoObjeto')),
            ],
        ),
        migrations.RemoveField(
            model_name='estadosgenerales',
            name='idTipoObjeto',
        ),
        migrations.DeleteModel(
            name='EstadosGenerales',
        ),
    ]
