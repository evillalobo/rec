from django.contrib import admin
from .models import RecursoCultural, RecursoNatural, Departamento, Categoria, Coordenada
# Register your models here.
admin.site.register(RecursoCultural)
admin.site.register(RecursoNatural)
admin.site.register(Categoria)
admin.site.register(Departamento)
admin.site.register(Coordenada)