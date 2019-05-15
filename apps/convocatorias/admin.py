from django.contrib import admin
from django.contrib.auth.models import User, Group, AbstractUser
from django.contrib.admin.models import LogEntry
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from django.contrib.auth.models import Permission
from django.core.mail import send_mail
from django import forms
from .models import *


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidop','apellidom','matricula','carrera','foto')
    list_filter  = ('matricula','carrera')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-nombre', 'user')
        return queryset

    user_info.short_description = 'Info'

admin.site.register(Alumnos, UserProfileAdmin)

class SendEmailNotification(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ('Subject')}))
    message = forms.CharField(widget=forms.Textarea)
    users = forms.ModelMultipleChoiceField(label="To", queryset=User.objects.all(), widget=forms.SelectMultiple())

def send_email(self, request, queryset):
    for i in queryset:
        if i.correo:
            send_mail('Invitacion a ', 'Cuerpo de mensaje', 'from@example.com',[i.correo], fail_silently=False)
        else:
            self.message_user(request, "Correos enviados!") 
send_email.short_description = "Enviar correo a los usuarios seleccionados"


class convocatoria_TABLA(ImportExportModelAdmin):
    list_display = ('nombre','duracion','video','link','Categoria')
    list_filter  = ('Categoria','Ingenieria','Ciencias','Energia_Recursos','Etica_Sociedad','Salud_Belleza','Tecnologia','Artes_Cultura','Idiomas','Negocios')
    def get_export_formats(self):
        formats = (
                base_formats.CSV,
                base_formats.XLS,

            )
        return [f for f in formats if f().can_export()]
    def get_import_formats(self):
        formats = (
                base_formats.CSV,
                base_formats.XLS,

            )
        return [f for f in formats if f().can_import()]

admin.site.register(Convocatorias, convocatoria_TABLA)
admin.site.index_title = ""