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
            name='ReconocimientoUsuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Description', models.CharField(max_length=140)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoReconocimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Description', models.CharField(max_length=100)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='reconocimientousuarios',
            name='idReconocimiento',
            field=models.ForeignKey(to='reconocimientos.TipoReconocimiento'),
        ),
        migrations.AddField(
            model_name='reconocimientousuarios',
            name='idusuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
