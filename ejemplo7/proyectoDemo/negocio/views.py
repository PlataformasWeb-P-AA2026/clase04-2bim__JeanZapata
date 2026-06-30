from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# importar las clases de models.py
from negocio.models import Chef, Plato, Restaurante, Comentario

# importar los formularios de forms.py
from negocio.forms import RestauranteForm, ChefForm, PlatoForm,ComentarioForm

def ingreso(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(index)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'registration/login.html', informacion_template)

def logout_view(request):
    logout(request)
    messages.info(request, "Has salido del sistema")
    return redirect(index)

def index(request):
    """
    """
    restaurantes = Restaurante.objects.all()
    informacion_template = {'restaurantes': restaurantes,
                            'numero': len(restaurantes)}
    return render(request, 'index.html', informacion_template)

def lista_chefs(request):
    """
    """
    chefs = Chef.objects.all()
    informacion_template = {'chefs': chefs,
                            'numero': len(chefs)}
    return render(request, 'lista_chefs.html', informacion_template)

def lista_platos(request):
    """
    """
    platos = Plato.objects.all()
    informacion_template = {'platos': platos,
                            'numero': len(platos)}
    return render(request, 'lista_platos.html', informacion_template)

@login_required(login_url='/entrando/login/')
def crear_restaurante(request):
    """
    """
    if request.method=='POST':
        formulario = RestauranteForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = RestauranteForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_restaurante.html', diccionario)

@login_required(login_url='/entrando/login/')
def crear_chef(request):
    """
    """
    if request.method=='POST':
        formulario = ChefForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = ChefForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_chef.html', diccionario)

@login_required(login_url='/entrando/login/')
def crear_plato(request):
    """
    """
    if request.method=='POST':
        formulario = PlatoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = PlatoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_plato.html', diccionario)

@login_required(login_url='/entrando/login/')
def crear_comentario(request):
    """
    Permite crear un comentario solo si el usuario está logeado.
    """
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST)
        print(formulario.errors)

        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.usuario = request.user
            comentario.save()
            return redirect(index)

    else:
        formulario = ComentarioForm()

    diccionario = {'formulario': formulario}

    return render(request, 'crear_comentario.html', diccionario)

@login_required(login_url='/entrando/login/')
def editar_restaurante(request, id):
    """
    """
    restaurante = Restaurante.objects.get(pk=id)
    if request.method=='POST':
        formulario = RestauranteForm(request.POST, instance=restaurante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = RestauranteForm(instance=restaurante)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_restaurante.html', diccionario)

@login_required(login_url='/entrando/login/')
def ver_restaurante(request, id):
    """
    """
    restautante = Restaurante.objects.get(pk=id)
    informacion_template = {'objeto': restautante}
    return render(request, 'ver_restaurante.html',
                  informacion_template)

@login_required(login_url='/entrando/login/')
def ver_chef(request, id):
    """
    """
    chef = Chef.objects.get(pk=id)
    informacion_template = {'objeto': chef}
    return render(request, 'ver_chef.html',
                  informacion_template)
@login_required(login_url='/entrando/login/')
def ver_plato(request, id):
    """
    """
    plato = Plato.objects.get(pk=id)
    informacion_template = {'objeto': plato}
    return render(request, 'ver_plato.html',
                  informacion_template)