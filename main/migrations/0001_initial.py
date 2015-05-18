# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprobacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('formato_proyecto', models.FileField(upload_to=b'proyectos')),
            ],
            options={
                'verbose_name_plural': 'Aprobaciones',
            },
        ),
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', main.models.TruncatingCharField(max_length=64)),
                ('ci', main.models.TruncatingCharField(max_length=10, verbose_name=b'CI', blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefono_institucional', main.models.TruncatingCharField(max_length=12)),
                ('telefono_celular', main.models.TruncatingCharField(max_length=12)),
                ('cargo', main.models.TruncatingCharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Asesores',
            },
        ),
        migrations.CreateModel(
            name='Cierre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('formato_proyecto', models.FileField(upload_to=b'proyectos')),
                ('informe_cierre', models.FileField(upload_to=b'proyectos')),
            ],
        ),
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', main.models.TruncatingCharField(max_length=128)),
                ('rif', main.models.TruncatingCharField(max_length=16)),
                ('sector', main.models.TruncatingCharField(max_length=64)),
                ('parroquia', main.models.TruncatingCharField(max_length=64)),
                ('municipio', main.models.TruncatingCharField(max_length=64)),
                ('estado', main.models.TruncatingCharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Comunidades',
            },
        ),
        migrations.CreateModel(
            name='Culminacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oficio', models.FileField(upload_to=b'culminaciones')),
                ('fecha_cesc_csscfi', models.DateField(verbose_name=b'Fecha de tr\xc3\xa1mite CESC ante CSSCFI')),
                ('fecha_csscfi_ccscula', models.DateField(verbose_name=b'Fecha de tr\xc3\xa1mite CSSCFI ante CCSCULA')),
                ('numero_oficio', main.models.TruncatingCharField(max_length=16, verbose_name=b'n\xc3\xbamero de oficio')),
                ('estatus', main.models.TruncatingCharField(max_length=1, choices=[(b'P', b'Pendiente'), (b'C', b'Culminado'), (b'P', b'En proceso')])),
            ],
            options={
                'verbose_name_plural': 'Culminaciones',
            },
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', main.models.TruncatingCharField(max_length=64)),
                ('codigo', main.models.TruncatingCharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', main.models.TruncatingCharField(max_length=32)),
                ('apellidos', main.models.TruncatingCharField(max_length=32)),
                ('ci', main.models.TruncatingCharField(max_length=10, verbose_name=b'CI')),
                ('email_ula', models.EmailField(max_length=254, blank=True)),
                ('email_alternativo', models.EmailField(max_length=254)),
                ('telefono_habitacion', main.models.TruncatingCharField(max_length=12)),
                ('telefono_celular', main.models.TruncatingCharField(max_length=12)),
                ('asesor', models.ForeignKey(blank=True, to='main.Asesor', null=True)),
                ('comunidad', models.ForeignKey(blank=True, to='main.Comunidad', null=True)),
                ('escuela', models.ForeignKey(to='main.Escuela')),
            ],
        ),
        migrations.CreateModel(
            name='Exoneracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('estudiante', models.ForeignKey(to='main.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', main.models.TruncatingCharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Facultades',
            },
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_cesc_csscfi', models.DateField(verbose_name=b'Fecha de tr\xc3\xa1mite CESC ante la CSSCFI')),
                ('fecha_csscfi_orefi', models.DateField(verbose_name=b'Fecha de tr\xc3\xa1mite CSSCFI ante OREFI', blank=True)),
                ('numero_oficio', main.models.TruncatingCharField(max_length=16, verbose_name=b'n\xc3\xbamero de oficio')),
                ('carta_aceptacion_tutor', models.FileField(upload_to=b'inscripciones', verbose_name=b'carta de aceptacion del tutor')),
                ('carta_aceptacion_comunidad', models.FileField(upload_to=b'inscripciones', verbose_name=b'carta de aceptacion de la comunidad')),
                ('programa_actividades', models.FileField(upload_to=b'inscripciones', verbose_name=b'programa de actividades del estudiante')),
                ('aval_ce_induccion', models.FileField(upload_to=b'inscripciones', null=True, verbose_name=b'Aval del CE para cursar Induccion y SC', blank=True)),
                ('aval_ce_proyecto', models.FileField(upload_to=b'inscripciones', null=True, verbose_name=b'Aval del CE para realizar proyecto externo', blank=True)),
                ('estudiante', models.ForeignKey(to='main.Estudiante')),
            ],
            options={
                'verbose_name_plural': 'Inscripciones',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', main.models.TruncatingCharField(max_length=32)),
                ('apellidos', main.models.TruncatingCharField(max_length=32)),
                ('ci', main.models.TruncatingCharField(max_length=10, verbose_name=b'CI')),
                ('numero_induccion', main.models.TruncatingCharField(max_length=10, verbose_name=b'n\xc3\xbamero de inducci\xc3\xb3n')),
                ('estatus', main.models.TruncatingCharField(max_length=1, choices=[(b'I', b'Inactivo'), (b'A', b'Activo')])),
                ('email_ula', models.EmailField(max_length=254)),
                ('email_alternativo', models.EmailField(max_length=254)),
                ('telefono_oficina', main.models.TruncatingCharField(max_length=12)),
                ('telefono_celular', main.models.TruncatingCharField(max_length=12, blank=True)),
                ('escuela', models.ForeignKey(blank=True, to='main.Escuela', null=True)),
                ('facultad', models.ForeignKey(blank=True, to='main.Facultad', null=True)),
            ],
            options={
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', main.models.TruncatingCharField(max_length=4)),
                ('titulo', main.models.TruncatingCharField(max_length=256)),
                ('fecha_aprobacion', models.DateField(verbose_name=b'fecha de aprobaci\xc3\xb3n')),
                ('numero_acta_aprobacion', main.models.TruncatingCharField(max_length=16)),
                ('archivo', models.FileField(null=True, upload_to=b'proyectos', blank=True)),
                ('estatus', main.models.TruncatingCharField(max_length=1, choices=[(b'A', b'Aprobado'), (b'R', b'Renovado'), (b'C', b'Cerrado')])),
                ('facultad_adscripcion', models.ForeignKey(to='main.Facultad')),
                ('responsable', models.ForeignKey(related_name='responsable_set', to='main.Profesor')),
                ('tutores', models.ManyToManyField(related_name='tutor_set', to='main.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Reestructuracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('formato_proyecto', models.FileField(upload_to=b'proyectos')),
                ('informe_tutor', models.FileField(upload_to=b'proyectos')),
                ('proyecto', models.ForeignKey(to='main.Proyecto')),
            ],
            options={
                'verbose_name_plural': 'Reestructuraciones',
            },
        ),
        migrations.CreateModel(
            name='Renovacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('formato_proyecto', models.FileField(upload_to=b'proyectos')),
                ('informe_tutor', models.FileField(upload_to=b'proyectos')),
                ('proyecto', models.ForeignKey(to='main.Proyecto')),
            ],
            options={
                'verbose_name_plural': 'Renovaciones',
            },
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', main.models.TruncatingCharField(max_length=16)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('fecha_final', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadAcademica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', main.models.TruncatingCharField(max_length=64)),
                ('codigo', main.models.TruncatingCharField(max_length=16)),
            ],
            options={
                'verbose_name_plural': 'Unidades Academicas',
            },
        ),
        migrations.AddField(
            model_name='profesor',
            name='unidad_academica',
            field=models.ForeignKey(blank=True, to='main.UnidadAcademica', null=True),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='semestre',
            field=models.ForeignKey(to='main.Semestre'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='proyecto',
            field=models.ForeignKey(blank=True, to='main.Proyecto', null=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='semestre_culminacion',
            field=models.ForeignKey(related_name='culminacion_est_set', blank=True, to='main.Semestre', null=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='semestre_induccion',
            field=models.ForeignKey(related_name='induccion_est_set', blank=True, to='main.Semestre', null=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='semestre_inscripcion',
            field=models.ForeignKey(related_name='inscripccion_est_set', blank=True, to='main.Semestre', null=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='tutor',
            field=models.ForeignKey(blank=True, to='main.Profesor', null=True),
        ),
        migrations.AddField(
            model_name='culminacion',
            name='estudiante',
            field=models.ForeignKey(to='main.Estudiante'),
        ),
        migrations.AddField(
            model_name='culminacion',
            name='semestre',
            field=models.ForeignKey(related_name='culminacion_set', to='main.Semestre'),
        ),
        migrations.AddField(
            model_name='cierre',
            name='proyecto',
            field=models.ForeignKey(to='main.Proyecto'),
        ),
        migrations.AddField(
            model_name='asesor',
            name='comunidad',
            field=models.ForeignKey(to='main.Comunidad'),
        ),
        migrations.AddField(
            model_name='aprobacion',
            name='proyecto',
            field=models.ForeignKey(to='main.Proyecto'),
        ),
    ]
