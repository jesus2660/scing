# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semestre',
            name='fecha_final',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='semestre',
            name='fecha_inicio',
            field=models.DateField(null=True, blank=True),
        ),
    ]
