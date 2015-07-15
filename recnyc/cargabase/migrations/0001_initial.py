# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('categoria', models.TextField(max_length=100)),
                ('descripcion', models.TextField(max_length=150, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coordenada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre', models.TextField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('imagen', models.TextField(max_length=100)),
                ('circuitos', models.TextField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecursoCultural',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre', models.TextField(max_length=100)),
                ('historia', models.TextField(max_length=300)),
                ('direccion', models.TextField(max_length=100)),
                ('imagen', models.TextField(max_length=100)),
                ('categoria', models.ForeignKey(to='cargabase.Categoria')),
                ('departamento', models.ForeignKey(to='cargabase.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoNatural',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre', models.TextField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('imagen', models.TextField(max_length=100)),
                ('categoria', models.ForeignKey(to='cargabase.Categoria')),
                ('departamento', models.ForeignKey(to='cargabase.Departamento')),
            ],
        ),
        migrations.AddField(
            model_name='coordenada',
            name='departamento',
            field=models.OneToOneField(to='cargabase.Departamento'),
        ),
        migrations.AddField(
            model_name='coordenada',
            name='recurso_nat',
            field=models.ForeignKey(blank=True, to='cargabase.RecursoNatural'),
        ),
        migrations.AddField(
            model_name='coordenada',
            name='resurso_cult',
            field=models.ForeignKey(blank=True, to='cargabase.RecursoCultural'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='departament',
            field=models.ForeignKey(to='cargabase.Departamento'),
        ),
    ]
