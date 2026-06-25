from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s %s %s" % (self.nombre, self.apellido, self.cedula)

    def obtener_numeros_telefonicos(self):
        return self.numeros_telefonicos.count()
    

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,
            related_name="numeros_telefonicos")

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)

    def obtener_operadora(self):
        if self.telefono.startswith("099"):
            return "Claro"
        elif self.telefono.startswith("098"):
            return "Movistar"
        else:
            return "Convencional"
