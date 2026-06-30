from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.cedula,
                self.correo)

    def get_provincia(self):
        """
        """
        dato = self.cedula[0:2]
        valor = "Sin Provincia"
        if dato == "11":
            valor = "Loja"
        else:
            if dato == "17":
                valor = "Pichincha"
        return valor

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,
            related_name="numeros_telefonicos")

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)

class Contacto(models.Model):
    username = models.CharField(max_length=30)
    correo = models.EmailField()
    comentario = models.CharField(max_length=25)
    
    def __str__(self):
        return "%s %s %s %s" % (self.username,
                self.correo,
                self.comentario,
                self.mensaje)
    
