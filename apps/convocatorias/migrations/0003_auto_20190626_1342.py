# Generated by Django 2.2.1 on 2019-06-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatorias', '0002_auto_20190626_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_usuarios/'),
        ),
    ]
