# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0002_auto_20150608_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaseObjetivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Description', models.CharField(max_length=25)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstadosGenerales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Description', models.CharField(max_length=25)),
                ('Status', models.BooleanField(default=True)),
                ('idTipoObjeto', models.ForeignKey(to='bases.TipoObjeto')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Descripcion', models.CharField(max_length=50)),
                ('ColorTag', models.CharField(max_length=7)),
                ('Status', models.BooleanField(default=True)),
                ('idTipoObjeto', models.ForeignKey(to='bases.TipoObjeto')),
            ],
        ),
    ]
