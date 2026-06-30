from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from negocio.models import Comentario, Restaurante, Chef, Plato

class RestauranteForm(ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nombre', 'tipo_cocina', 'capacidad_meses']

class ChefForm(ModelForm):
    class Meta:
        model = Chef
        fields = ['nombres', 'anios_experiencia', 'especialidad_culinaria',
                  'restaurante']

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre_plato', 'descripcion', 'precio_plato',
                  'ingredientes_principales', 'chef']
        
class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['mensaje']
        labels = {
            'mensaje': _('Ingrese su comentario por favor'),
        }

    def clean_mensaje(self):
        valor = self.cleaned_data['mensaje']

        if len(valor) > 25:
            raise forms.ValidationError("El comentario no puede tener más de 25 caracteres")

        return valor