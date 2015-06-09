# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reconocimientos', '0003_auto_20150608_2348'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0002_auto_20150608_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=100)),
                ('Email', models.EmailField(unique=True, max_length=200)),
                ('Password', models.CharField(unique=True, max_length=250)),
                ('Avatar', models.CharField(max_length=100, blank=True)),
                ('FechaCreacion', models.DateField()),
                ('UltimaVisita', models.DateField()),
                ('Status', models.BooleanField(default=True)),
                ('idTipoUsuario', models.ForeignKey(to='usuarios.TipoUsuario')),
                ('idUsuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='idTipoUsuario',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='idUsuario',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
