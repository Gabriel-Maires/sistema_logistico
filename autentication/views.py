from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from storage.models import Motorista


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Motorista.objects.filter(nome=username)

        if user:
            
            return redirect('/')
        else:
            messages.add_message(
                request, messages.constants.ERROR, "Email ou senha inválidos")
            return redirect('login.html')


def logout(request):
    logout_django(request)
    return redirect('login')


@login_required(login_url="/auth/login/")
def plataforma(request):
    return render(request, '/')
