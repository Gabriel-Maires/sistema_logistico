from django.contrib import admin

from .models import Motorista, Produto

# Register your models here.
admin.site.register(Produto)
admin.site.register(Motorista)
