# Generated by Django 2.2.1 on 2019-06-26 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0004_auto_20190626_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='sexo',
            field=models.CharField(blank=True, choices=[('Hombre', 'H'), ('Mujer', 'M')], default=None, max_length=20, null=True),
        ),
    ]
