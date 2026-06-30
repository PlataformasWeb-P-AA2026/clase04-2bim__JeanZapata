from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from administrativo.models import Contacto

from administrativo.models import Estudiante, \
        NumeroTelefonico

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'correo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'apellido': _('Ingrese apellido por favor'),
            'cedula': _('Ingrese cédula por favor'),
            'correo': _('Ingrese correo por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())
        """
        """

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos nombre por favor")
        return valor

    def clean_apellido(self):
        valor = self.cleaned_data['apellido']
        num_palabras = len(valor.split())

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos apellidos por favor")
        return valor

    def clean_cedula(self):
        valor = self.cleaned_data['cedula']
        if len(valor) != 10:
            raise forms.ValidationError("Ingrese cédula con 10 dígitos")
        return valor

    def clean_correo(self):
        valor = self.cleaned_data['correo']
        if "@" not in valor or "utpl.edu.ec" not in valor:
            raise forms.ValidationError("Ingrese correo válido para la Universidad")
        return valor


class NumeroTelefonicoForm(ModelForm):
    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']
        labels = {
            'telefono': _('Ingrese número de teléfono por favor'),
            'tipo': _('Ingrese tipo de teléfono por favor'),
            'estudiante': _('Ingrese estudiante por favor'),
        }


class NumeroTelefonicoEstudianteForm(ModelForm):

    def __init__(self, estudiante, *args, **kwargs):
        super(NumeroTelefonicoEstudianteForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        print(estudiante)

    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']





class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['username', 'correo', 'comentario']
        labels = {
            'username': _('Ingrese nombre de usuario por favor'),
            'correo': _('Ingrese correo electrónico por favor'),
            'comentario': _('Ingrese comentario por favor'),
        }
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})}

    def clean_comentario(self):
        valor = self.cleaned_data['comentario']

        if len(valor) > 25:
            raise forms.ValidationError("El comentario no puede tener más de 25 caracteres")

        return valor