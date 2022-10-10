from django.shortcuts import render

from .models import Motorista, Produto


def storage_page(request):
    motorista = Motorista.objects.all()
    produto = Produto.objects.all()
    return render(request, 'storage_homepage.html', {"motoristas": motorista, "produtos": produto})
