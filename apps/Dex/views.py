from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Criatura, Usuario

# Create your views here.
def inicio(request):
    all = Criatura.objects.all()
    return render(request, 'Dex/ver_criaturas.html', {'all':all})


def criaturas_usuario(request):
    criaturas = Criatura.objects.filter(usuario=request.user.id)
    return render(request, 'Dex/ver_criaturas.html', {'all': criaturas})


def crear_criatura(request):
    return render(request, 'Dex/formulario_criatura.html')


def formulario_criatura(request):
    try:
        usuario = User.objects.get(username=request.user.username)
        Criatura.objects.create(usuario=usuario, nombre=request.POST['nombre'], edad=request.POST['edad'],
                                estatura=request.POST['estatura'], naturaleza=request.POST['naturaleza'],
                                origen=request.POST['origen'], imagen=request.FILES.get('avatar'))
        messages.success(request, 'Tu creacion se a creado con exito')
        return redirect('crear_criatura')
    except Exception as e:
        print(e.__cause__.__str__())
        messages.warning(request, 'Hubo un error con la creacion de tu creatura')
        return redirect('crear_criatura')


def registro_usuario(request):
    return render(request, 'Dex/registrase.html')


def formulario_registro_usuario(request):
    if request.POST['password'] == request.POST['password2']:
        usuario_nuevo = User.objects.create_user(username=request.POST['nombre'], email=request.POST['email'],
                                                 password=request.POST['password'])
        Usuario.objects.create(usuario=usuario_nuevo, codigo_seguridad=request.POST['code'],
                               biografia=request.POST['bio'])
        messages.success(request, 'El usuario se a creado con exito')
        return redirect('inicio_sesion')
    else:
        messages.success(request, 'Las contraseñas no coinciden')
        return redirect('registro_usuario')
