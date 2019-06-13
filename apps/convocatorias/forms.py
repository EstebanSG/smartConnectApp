from django import forms
from .models import *
from .choices import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget


class ConvocatoriaForm(forms.ModelForm):
    class Meta:
        model = Convocatorias
        fields = [
            'nombre',
            'informacion',
            'duracion',
            'video',
            'link'
            
        ]
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
        
class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
class AlumnosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlumnosForm, self).__init__(*args, **kwargs)

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidop = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellidom = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    foto = forms.ImageField()
    matricula = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    carrera = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = Alumnos
        fields =[
            'nombre',
            'apellidop',
            'apellidom',
            'foto',
            'matricula',
            'carrera',

        ]