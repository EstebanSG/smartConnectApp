from django.db import models
from multiselectfield import MultiSelectField
from tinymce import models as tinymce_models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from tinymce import models as tinymce_models

# Create your models here.
class Convocatorias(models.Model):
     CATEGORIA_CHOICES=(('Ninguna','Ninguna'),('Ingeniería','Ingeniería'),('Ciencias','Ciencias'),('Energía y Recurosos','Energía y Recurosos')
     ,('Ética y Sociedad','Ética y Sociedad'),('Salud y Belleza','Salud y Belleza'),('Tecnología','Tecnología'),('Artes y Cultura','Artes y Cultura')
     ,('Idiomas','Idiomas'),('Negocios','Negocios'),)
     
     INGENIERIA_CHOICES=(('Ninguna','Ninguna'),('Electrónica','Electrónica'),('Mecánica','Mecánica') ,('Construcción','Construcción'),('Computación','Computación'),('Industría','Industría'),)

     CIENCIAS_CHOICES=(('Ninguna','Ninguna'),('Física','Física'),('Química','Química'),('Biología','Biología'),)

     ENERGIA_RECURSOS=(('Ninguna','Ninguna'),('Sostenibilidad','Sostenibilidad'),('Medio ambiente','Medio ambiente'),('Recursos naturales','Recursos naturales')
     ,('Energia','Energia'),)

     ETICA_SOCIEDAD_CHOICES=(('Ninguna','Ninguna'),('ONU','ONU'),('Valores','Valores')
     ,('Sociedad','Sociedad'),('Política','Política'),('Cultura','Cultura'),)
     
     SALUD_BELLEZA_CHOICES=(('Ninguna','Ninguna'),('Deportes','Deportes'),('Salud','Salud'),('Belleza','Belleza'),)
     
     TECNOLOGIA_CHOICES=(('Ninguna','Ninguna'),('Aplicaciones','Aplicaciones')
     ,('StartUp','StartUp')
     ,('Financiamiento','Financiamiento'),('Interdiciplinario','Interdiciplinario'),('Innovación','Innovación'),)
     
     ARTES_CULTURA_CHOICES=(('Ninguna','Ninguna'),('Teatro','Teatro'),('Danza','Danza'),('Arquitectura','Arquitectura')
     ,('Escultura','Escultura'),('Pintura','Pintura'),('Música','Música')
     ,('Poesía/Literatura','Poesía/Literatura'),('Cine','Cine'),)
     
     IDIOMAS_CHOICES=(('Ninguna','Ninguna'),('Internacionales','Internacionales')
     ,('Nacionales','Nacionales'),)
     
     NEGOCIOS_CHOICES=(('Ninguna','Ninguna'),('Finanzas','Finanzas')
     ,('Comercio','Comercio'),('Économia','Économia'),('Creación de empresas','Creación de empresas'),)

     id = models.AutoField(primary_key=True)
     nombre = models.CharField(max_length = 100, default=None, blank=True, null=True)
     informacion = models.TextField( blank = True, null = True)
     duracion = models.CharField(max_length = 200, default=None)
     video = models.CharField(max_length = 200, default=None, null=True)
     link = models.CharField(max_length = 200, default=None, null=False)
     Categoria = models.CharField(max_length = 200,choices=CATEGORIA_CHOICES,default=None)
     Ingenieria = models.CharField(max_length = 200,choices=INGENIERIA_CHOICES,default=None)
     Ciencias = models.CharField(max_length = 200,choices=CIENCIAS_CHOICES,default=None)
     Energia_Recursos = models.CharField(max_length = 200,choices=ENERGIA_RECURSOS,default=None)
     Etica_Sociedad = models.CharField(max_length = 200,choices=ETICA_SOCIEDAD_CHOICES,default=None)
     Salud_Belleza = models.CharField(max_length = 200,choices=SALUD_BELLEZA_CHOICES,default=None)
     Tecnologia = models.CharField(max_length = 200,choices=TECNOLOGIA_CHOICES,default=None)
     Artes_Cultura = models.CharField(max_length = 200,choices=ARTES_CULTURA_CHOICES,default=None)
     Idiomas = models.CharField(max_length = 200,choices=IDIOMAS_CHOICES,default=None)
     Negocios = models.CharField(max_length = 200,choices=NEGOCIOS_CHOICES,default=None)

     def get_registros(self):
          return " , ".join([str(p) for p in self.registros.all()])
     get_registros.short_description = "registros"

     class Meta:
          verbose_name_plural = "Convocatorias"
     def __str__(self):
          return self.nombre

class Alumnos(models.Model):
     on_delete=models.DO_NOTHING
     user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)

     convocatorias = models.ManyToManyField(Convocatorias, blank = True)

     id = models.AutoField(primary_key=True)
     nombre = models.CharField(max_length = 100,null=False)
     apellidop = models.CharField(max_length = 200,null=False)
     apellidom = models.CharField(max_length = 200,null=False)
     foto = models.ImageField(null=False, blank=True, upload_to = "fotos_usuarios")
     matricula = models.CharField(max_length = 100,null=False)
     carrera = models.CharField(max_length = 100,null=False)
     #correo = models.EmailField(default=None,null=True)
     #correo = tinymce_models.HTMLField()

     def get_eventos(self):
          return " , ".join([str(p) for p in self.eventos.all()])
     
     objects = models.Manager()

     class Meta:
          verbose_name_plural = "Alumnos"
     def __str__(self):
          return self.nombre
def create_profile(sender, **kwargs):
     if kwargs['created']:
          user_profile = Alumnos.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)








    