from django.db import models
from django.contrib.auth.models import User

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_cocina = models.CharField(max_length=100)
    capacidad_meses = models.IntegerField(default=0)

    def __str__(self):
        return "Restaurante: %s %s %d" % (self.nombre,
                self.tipo_cocina,
                self.capacidad_meses)


class Chef(models.Model):
    nombres = models.CharField(max_length=100)
    anios_experiencia = models.IntegerField(default=0)
    especialidad_culinaria = models.CharField(max_length=100)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE,
            related_name="chefs")

    def __str__(self):
        return "%s %d %s %s - (%s)" % (self.nombres, self.anios_experiencia,
                                self.especialidad_culinaria, self.restaurante,
                                self.restaurante.nombre)

class Plato(models.Model):
    nombre_plato = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio_plato = models.FloatField()
    ingredientes_principales = models.CharField(max_length=200)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE,
            related_name="platos")

    def __str__(self):
        return "%s %s %.2f - (%s)" % (self.nombre_plato, self.descripcion,
                                self.precio_plato,
                                self.chef.nombres)


class Comentario(models.Model):
    mensaje = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)