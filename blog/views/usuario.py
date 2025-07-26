from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from ..models import Perfil
from ..forms import UserRegisterForm


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect('inicio')

        # Si el form no es válido o user es None, volvemos al login mostrando errores
        return render(request, "blog/usuario/login.html", {"form": form})

    else:
        form = AuthenticationForm()
    return render(request, "blog/usuario/login.html", {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # guarda el usuario
            edad = form.cleaned_data['edad']
            # Creamos el perfil asociado al usuario
            perfil = Perfil(usuario=user, edad=edad)
            perfil.save()
            return render(request, 'blog/usuario/usuario_creado.html', {'username': user.username})
    else:
        form = UserRegisterForm()    
    return render(request, 'blog/usuario/register.html', {'form': form})