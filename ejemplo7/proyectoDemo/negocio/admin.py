from django.contrib import admin
# Importar las clases del modelo
from negocio.models import Restaurante, Chef, Plato, Comentario

class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_cocina', 'capacidad_meses')
    search_fields = ('nombre',)

admin.site.register(Restaurante, RestauranteAdmin)

class ChefAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'anios_experiencia', 'especialidad_culinaria')
    search_fields = ('nombres',)

admin.site.register(Chef, ChefAdmin)

class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre_plato', 'descripcion', 'precio_plato',
                    'ingredientes_principales')
    search_fields = ('nombre_plato',)

admin.site.register(Plato, PlatoAdmin)
admin.site.register(Comentario)