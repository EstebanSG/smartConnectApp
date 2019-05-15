from django import forms

from .models import Convocatorias

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