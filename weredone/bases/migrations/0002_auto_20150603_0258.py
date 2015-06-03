# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipousuario',
            old_name='Desciption',
            new_name='Description',
        ),
    ]
