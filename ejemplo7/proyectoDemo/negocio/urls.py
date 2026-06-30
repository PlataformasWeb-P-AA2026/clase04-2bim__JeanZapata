from django.urls import path, include
# se importa las vistas de la aplicación
from negocio import views


urlpatterns = [
        path('', views.index, name='index'),
        path('lista/chefs', views.lista_chefs, name='lista_chefs'),
        path('lista/platos', views.lista_platos, name='lista_platos'),

        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),

        path('crear/restaurante', views.crear_restaurante,
            name='crear_restaurante'),
        path('crear/chef', views.crear_chef,
         name='crear_chef'),
        path('crear/plato', views.crear_plato,
         name='crear_plato'),

        path('editar/restaurante/<int:id>', views.editar_restaurante,
            name='editar_restaurante'),

        path('ver/restaurante/<int:id>', views.ver_restaurante,
            name='ver_restaurante'),
        path('ver/chef/<int:id>', views.ver_chef,
         name='ver_chef'),
        path('ver/plato/<int:id>', views.ver_plato,
         name='ver_plato'),
         path('crear/comentario', views.crear_comentario,
         name='crear_comentario'),
]