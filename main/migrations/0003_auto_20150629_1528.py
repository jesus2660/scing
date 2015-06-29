# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150624_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='culminacion',
            name='fecha',
            field=models.DateField(null=True, verbose_name=b'Fecha de culminacion', blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estatus',
            field=models.CharField(default=b'I', max_length=1, choices=[(b'I', b'Inscrito'), (b'C', b'Culminado')]),
        ),
    ]
