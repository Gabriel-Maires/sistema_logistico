from django.contrib import messages
from django.shortcuts import redirect, render


def valida_cadastro(request, nome, sobrenome, senha, confirma_senha, username):
    if senha != confirma_senha:
        messages.add_message(
            request, messages.constants.ERROR, "As senhas inseridas não são iguais")
        return render(request, 'register.html')

    if len(nome.strip()) == 0:
        messages.add_message(
            request, messages.constants.ERROR, "Campo de nome não preenchido")
        return render(request, 'register.html')

    if len(sobrenome.strip()) == 0:
        messages.add_message(
            request, messages.constants.ERROR, "Campo de sobrenome não preenchido")
        return render(request, 'register.html')

    if len(username.strip()) == 0:
        messages.add_message(
            request, messages.constants.ERROR, "Campo de Email não preenchido")
        return render(request, 'register.html')

    if len(senha.strip()) == 0:
        messages.add_message(
            request, messages.constants.ERROR, "Campo de senha não preenchido")
        return render(request, 'register.html')

    if len(confirma_senha.strip()) == 0:
        messages.add_message(
            request, messages.constants.ERROR, "Campo de confirmar senha não preenchido")
        return render(request, 'register.html')

    return 'OK'
