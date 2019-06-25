# Generated by Django 2.2.1 on 2019-06-25 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('informacion', models.TextField(blank=True, null=True)),
                ('duracion', models.CharField(default=None, max_length=200)),
                ('video', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('link', models.CharField(default=None, max_length=200)),
                ('Categoria', models.CharField(choices=[('Ninguna', 'Ninguna'), ('Ingeniería', 'Ingeniería'), ('Ciencias', 'Ciencias'), ('Energía y Recurosos', 'Energía y Recurosos'), ('Ética y Sociedad', 'Ética y Sociedad'), ('Salud y Belleza', 'Salud y Belleza'), ('Tecnología', 'Tecnología'), ('Artes y Cultura', 'Artes y Cultura'), ('Idiomas', 'Idiomas'), ('Negocios', 'Negocios')], default=None, max_length=200)),
                ('Ingenieria', models.CharField(choices=[('Ninguna', 'Ninguna'), ('Electrónica', 'Electrónica'), ('Mecánica', 'Mecánica'), ('Construcción', 'Construcción'), ('Computación', 'Computación'), ('Industría', 'Industría')], default=None, max_length=200)),
                ('Ciencias', models.CharField(choices=[('Ninguna', 'Ninguna'), ('Física', 'Física'), ('Química', 'Química'), ('Biología', 'Biología')], default=None, max_length=200)),
                ('Energia_Recursos', models.CharField(choices=[('Ninguna', 'Ninguna'), ('Sostenibilidad', 'Sostenibilidad'), ('Medio ambiente', 'Medio ambiente'), ('Recursos naturales', 'Recursos naturales'), ('Energia', 'Energia')], default=None, max_length=200)),
                ('Etica_Sociedad', models.CharField(choices=[('Ninguna', 'Ninguna'), ('ONU', 'ONU'), ('Valores', 'Valores'), ('Sociedad', 'Sociedad'), ('Política', 'Política'), ('Cultura', 'Cultura')], default=None, max_length=200)),
                ('Salud_Belleza', models.CharField(choices=[('Ninguna', 'Ninguna'), ('Deportes', 'Deportes'), ('Salud', 'Salud'), ('Belleza', 'Belleza')], default=None, max_length=200)),
                ('Tecnologia', models.CharField(choices=[('Ninguna', 'Ninguna'), ('Aplicaciones', 'Aplicaciones'), ('StartUp', 'StartUp'), ('Financiamiento', 'Financiamiento'), ('Interdiciplinario', 'Interdiciplinario'), ('Innovación', 'Innovación')], default=None, max_length=200)),
                ('Artes_Cultura', models.CharField(choices=[('Ninguna', 'Ninguna'), ('Teatro', 'Teatro'), ('Danza', 'Danza'), ('Arquitectura', 'Arquitectura'), ('Escultura', 'Escultura'), ('Pintura', 'Pintura'), ('Música', 'Música'), ('Poesía/Literatura', 'Poesía/Literatura'), ('Cine', 'Cine')], default=None, max_length=200)),
                ('Idiomas', models.CharField(choices=[('Ninguna', 'Ninguna'), ('Internacionales', 'Internacionales'), ('Nacionales', 'Nacionales')], default=None, max_length=200)),
                ('Negocios', models.CharField(choices=[('Ninguna', 'Ninguna'), ('Finanzas', 'Finanzas'), ('Comercio', 'Comercio'), ('Économia', 'Économia'), ('Creación de empresas', 'Creación de empresas')], default=None, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Convocatorias',
            },
        ),
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=200)),
                ('foto', models.FileField(blank=True, default='static/images/team/1.jpg', null=True, upload_to='fotos_usuarios')),
                ('matricula', models.CharField(max_length=100)),
                ('carrera', models.CharField(max_length=100)),
                ('interes', models.CharField(blank=True, choices=[('Ninguna', 'Ninguna'), ('Ingeniería', 'Ingeniería'), ('Ciencias', 'Ciencias'), ('Energía y Recurosos', 'Energía y Recurosos'), ('Ética y Sociedad', 'Ética y Sociedad'), ('Salud y Belleza', 'Salud y Belleza'), ('Tecnología', 'Tecnología'), ('Artes y Cultura', 'Artes y Cultura'), ('Idiomas', 'Idiomas'), ('Negocios', 'Negocios')], default=None, max_length=200, null=True)),
                ('interes2', models.CharField(blank=True, choices=[('Ninguna', 'Ninguna'), ('Ingeniería', 'Ingeniería'), ('Ciencias', 'Ciencias'), ('Energía y Recurosos', 'Energía y Recurosos'), ('Ética y Sociedad', 'Ética y Sociedad'), ('Salud y Belleza', 'Salud y Belleza'), ('Tecnología', 'Tecnología'), ('Artes y Cultura', 'Artes y Cultura'), ('Idiomas', 'Idiomas'), ('Negocios', 'Negocios')], default=None, max_length=200, null=True)),
                ('convocatorias', models.ManyToManyField(blank=True, to='convocatorias.Convocatorias')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Alumnos',
            },
        ),
    ]
