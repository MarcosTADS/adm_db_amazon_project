from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Endereco)
admin.site.register(Perfil)
admin.site.register(Item)
admin.site.register(FormaPagamento)
admin.site.register(Pedido)