# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='estatus',
            field=models.CharField(default='I', max_length=1, choices=[(b'I', b'Inscrito'), (b'C', b'Culminado')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aprobacion',
            name='formato_proyecto',
            field=models.FileField(upload_to=b'proyectos/aprobaciones', blank=True),
        ),
        migrations.AlterField(
            model_name='cierre',
            name='formato_proyecto',
            field=models.FileField(upload_to=b'proyectos/cierres/', blank=True),
        ),
        migrations.AlterField(
            model_name='cierre',
            name='informe_cierre',
            field=models.FileField(upload_to=b'proyectos/cierres/', blank=True),
        ),
        migrations.AlterField(
            model_name='reestructuracion',
            name='formato_proyecto',
            field=models.FileField(upload_to=b'proyectos/reestructuraciones/', blank=True),
        ),
        migrations.AlterField(
            model_name='reestructuracion',
            name='informe_tutor',
            field=models.FileField(upload_to=b'proyectos/reestructuraciones/', blank=True),
        ),
        migrations.AlterField(
            model_name='renovacion',
            name='formato_proyecto',
            field=models.FileField(upload_to=b'proyectos/renovaciones/', blank=True),
        ),
        migrations.AlterField(
            model_name='renovacion',
            name='informe_tutor',
            field=models.FileField(upload_to=b'proyectos/renovaciones/', blank=True),
        ),
    ]
