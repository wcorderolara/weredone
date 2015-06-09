# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=100)),
                ('Email', models.EmailField(unique=True, max_length=200)),
                ('Password', models.CharField(unique=True, max_length=250)),
                ('Avatar', models.CharField(max_length=100, blank=True)),
                ('FechaCreaacion', models.DateField()),
                ('UltimaVisita', models.DateField()),
                ('Status', models.BooleanField(default=True)),
                ('idTipoUsuario', models.ForeignKey(to='usuarios.TipoUsuario')),
                ('idUsuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
